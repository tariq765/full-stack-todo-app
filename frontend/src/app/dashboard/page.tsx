'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Navbar from '@/components/Navbar';
import { useAuth } from '@/context/AuthContext';
import {
  getUserTasks as getUserTasksApi,
  createTask as createTaskApi,
  toggleTaskCompletion as toggleTaskCompletionApi,
  deleteTask as deleteTaskApi,
  updateTask as updateTaskApi
} from '@/lib/task-api';
import { getUserIdFromToken } from '@/lib/jwt-utils';

// Define TypeScript interfaces
interface Task {
  id: number | string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

interface EditingTask {
  id: string | number | null;
  title: string;
  description: string;
}

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTask, setNewTask] = useState({ title: '', description: '' });
  const [editingTask, setEditingTask] = useState<EditingTask | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const router = useRouter();
  const { logout } = useAuth();
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    if (!token) {
      router.push('/login');
      return;
    }

    const extractedUserId = getUserIdFromToken(token);
    if (!extractedUserId) {
      router.push('/login');
      return;
    }

    setUserId(extractedUserId);
  }, [router]);

  useEffect(() => {
    if (userId) {
      const token = localStorage.getItem('auth_token');
      if (token) {
        fetchTasks(token, userId);
      } else {
        router.push('/login');
      }
    }
  }, [userId, router]);

  const fetchTasks = async (token: string, userId: string) => {
    if (!userId) {
      router.push('/login');
      setLoading(false);
      return;
    }

    try {
      const response = await getUserTasksApi(userId, token);

      if (response.data) {
        setTasks(response.data);
      } else if (response.status === 401) {
        // Unauthorized - redirect to login
        router.push('/login');
      } else {
        setError(response.error || 'Failed to load tasks');
      }
    } catch (err) {
      setError('An error occurred while loading tasks');
      console.error('Fetch tasks error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!newTask.title.trim()) {
      setError('Task title is required');
      return;
    }

    const token = localStorage.getItem('auth_token'); // Or however you store the JWT
    if (!token || !userId) {
      router.push('/login');
      return;
    }

    try {
      // Ensure the completed field is included with default value of false
      const taskData = {
        ...newTask,
        completed: false
      };

      // Log the data being sent for debugging
      console.log('Creating task with data:', taskData);
      console.log('Using userId:', userId);

      const response = await createTaskApi(userId, taskData, token);

      if (response.data) {
        setTasks([response.data, ...tasks]);
        setNewTask({ title: '', description: '' });
        setError('');
        console.log('Task created successfully:', response.data);
      } else if (response.status === 401) {
        router.push('/login');
      } else {
        setError(response.error || 'Failed to create task');
        console.error('API response error:', response);
      }
    } catch (err) {
      setError('An error occurred while creating task');
      console.error('Create task error:', err);
    }
  };

  const toggleTaskCompletion = async (taskId: string, currentStatus: boolean) => {
    const token = localStorage.getItem('auth_token'); // Or however you store the JWT
    if (!token || !userId) {
      router.push('/login');
      return;
    }

    try {
      const response = await toggleTaskCompletionApi(userId, taskId, !currentStatus, token);

      if (response.data) {
        setTasks(tasks.map(task =>
          task.id === taskId ? { ...task, completed: !currentStatus } : task
        ));
      } else if (response.status === 401) {
        router.push('/login');
      }
    } catch (err) {
      console.error('Toggle task error:', err);
    }
  };

  const deleteTask = async (taskId: string) => {
    const token = localStorage.getItem('auth_token'); // Or however you store the JWT
    if (!token || !userId) {
      router.push('/login');
      return;
    }

    try {
      const response = await deleteTaskApi(userId, taskId, token);

      if (response.status === 200 || response.status === 204) {
        setTasks(tasks.filter(task => task.id !== taskId));
      } else if (response.status === 401) {
        router.push('/login');
      }
    } catch (err) {
      console.error('Delete task error:', err);
    }
  };

  const startEditing = (task: Task) => {
    setEditingTask({
      id: task.id,
      title: task.title,
      description: task.description || ''
    });
  };

  const cancelEditing = () => {
    setEditingTask(null);
  };

  const saveEditedTask = async (taskId: string | number) => {
    if (!editingTask) return;

    const token = localStorage.getItem('auth_token');
    if (!token || !userId) {
      router.push('/login');
      return;
    }

    try {
      const taskIdStr = typeof taskId === 'string' ? taskId : taskId.toString();

      console.log('Updating task with ID:', taskIdStr);
      console.log('Update data:', {
        title: editingTask.title,
        description: editingTask.description,
      });

      const response = await updateTaskApi(
        userId,
        taskIdStr,
        {
          title: editingTask.title,
          description: editingTask.description,
        },
        token
      );

      if (response.data) {
        setTasks(tasks.map(task =>
          task.id.toString() === taskIdStr ? { ...task, ...response.data } : task
        ));
        setEditingTask(null);
        console.log('Task updated successfully:', response.data);
      } else if (response.status === 401) {
        router.push('/login');
      } else {
        setError(response.error || 'Failed to update task');
        console.error('Update task API response:', response);
      }
    } catch (err) {
      setError('An error occurred while updating task');
      console.error('Update task error:', err);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <div className="flex justify-center items-center h-screen">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          {error && (
            <div className="mb-4 text-sm text-red-600 bg-red-50 p-3 rounded-md">
              {error}
            </div>
          )}

          {/* Task Creation Form */}
          <div className="mb-8">
            <form onSubmit={handleCreateTask} className="bg-white shadow overflow-hidden sm:rounded-lg p-6">
              <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                <div className="sm:col-span-4">
                  <label htmlFor="title" className="block text-sm font-medium text-gray-700">
                    Task Title *
                  </label>
                  <div className="mt-1">
                    <input
                      type="text"
                      id="title"
                      value={newTask.title}
                      onChange={(e) => setNewTask({...newTask, title: e.target.value})}
                      className="shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md"
                      placeholder="What needs to be done?"
                    />
                  </div>
                </div>

                <div className="sm:col-span-6">
                  <label htmlFor="description" className="block text-sm font-medium text-gray-700">
                    Description
                  </label>
                  <div className="mt-1">
                    <textarea
                      id="description"
                      rows={3}
                      value={newTask.description}
                      onChange={(e) => setNewTask({...newTask, description: e.target.value})}
                      className="shadow-sm focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md"
                      placeholder="Add details..."
                    />
                  </div>
                </div>

                <div className="sm:col-span-6">
                  <button
                    type="submit"
                    className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                  >
                    Add Task
                  </button>
                </div>
              </div>
            </form>
          </div>

          {/* Task List */}
          <div className="bg-white shadow overflow-hidden sm:rounded-md">
            <ul className="divide-y divide-gray-200">
              {tasks.length === 0 ? (
                <li className="px-4 py-6 sm:px-6">
                  <p className="text-gray-500 text-center">No tasks yet. Add your first task above!</p>
                </li>
              ) : (
                tasks.map((task) => (
                  <li key={task.id} className="px-4 py-6 sm:px-6 hover:bg-gray-50">
                    {editingTask && editingTask.id === task.id ? (
                      // Edit mode
                      <div className="mb-4">
                                              <div className="flex items-center mb-2">
                                                <input
                                                  type="checkbox"
                                                  checked={task.completed}
                                                  onChange={() => toggleTaskCompletion(task.id.toString(), task.completed)}
                                                  className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                                                />                          <input
                            type="text"
                            value={editingTask?.title || ''}
                            onChange={(e) => setEditingTask(editingTask ? {...editingTask, title: e.target.value} : null)}
                            className="ml-3 flex-1 px-2 py-1 border rounded text-lg font-medium"
                          />
                        </div>
                        <textarea
                          value={editingTask?.description || ''}
                          onChange={(e) => setEditingTask(editingTask ? {...editingTask, description: e.target.value} : null)}
                          className="w-full px-2 py-1 border rounded mt-2 text-sm"
                          rows={2}
                          placeholder="Description..."
                        />
                        <div className="flex space-x-2 mt-2">
                          <button
                            onClick={() => saveEditedTask(task.id)}
                            className="text-green-600 hover:text-green-900 font-medium"
                          >
                            Save
                          </button>
                          <button
                            onClick={cancelEditing}
                            className="text-gray-600 hover:text-gray-900 font-medium"
                          >
                            Cancel
                          </button>
                        </div>
                      </div>
                    ) : (
                      // View mode
                      <div>
                        <div className="flex items-center justify-between">
                          <div className="flex items-center">
                            <input
                              type="checkbox"
                              checked={task.completed}
                              onChange={() => toggleTaskCompletion(task.id.toString(), task.completed)}
                              className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                            />
                            <span className={`ml-3 text-lg font-medium ${task.completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                              {task.title}
                            </span>
                          </div>
                          <div className="flex space-x-2">
                            <button
                              onClick={() => startEditing(task)}
                              className="text-blue-600 hover:text-blue-900"
                            >
                              Edit
                            </button>
                            <button
                              onClick={() => deleteTask(task.id.toString())}
                              className="text-red-600 hover:text-red-900"
                            >
                              Delete
                            </button>
                          </div>
                        </div>
                        {task.description && (
                          <p className="mt-1 ml-7 text-sm text-gray-500">{task.description}</p>
                        )}
                        <p className="mt-1 ml-7 text-xs text-gray-400">
                          Created: {new Date(task.created_at).toLocaleString()}
                        </p>
                      </div>
                    )}
                  </li>
                ))
              )}
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
}