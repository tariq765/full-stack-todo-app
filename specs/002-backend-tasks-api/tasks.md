---
description: "Task list for Backend API & Database feature"
---

# Tasks: Backend API & Database

**Input**: Design documents from `/specs/002-backend-tasks-api/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit test requirements mentioned in spec - focusing on implementation tasks only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/src/`, `backend/tests/`
- Following the project structure from plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for backend API

- [X] T001 Create backend folder structure and initialize FastAPI application in backend/src/main.py
- [X] T002 [P] Set up requirements.txt with FastAPI, SQLModel, PyJWT, python-multipart, uvicorn
- [X] T003 [P] Prepare router-based architecture in backend/src/api/
- [X] T004 Create README.md with backend setup instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core backend infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Configure SQLModel engine and load DATABASE_URL from environment variables in backend/src/core/config.py
- [X] T006 [P] Create database session dependency in backend/src/db/session.py
- [X] T007 [P] Create Task SQLModel class with required fields in backend/src/models/task.py
- [X] T008 Implement auto-create tables on app startup logic in backend/src/main.py
- [X] T009 Ensure compatibility with Neon Serverless PostgreSQL in backend/src/core/config.py
- [X] T010 Create base model for database entities in backend/src/models/base.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure Task Management (Priority: P1) 🎯 MVP

**Goal**: Enable authenticated users to create, read, update, and delete their own tasks through the backend API, while ensuring users can only access their own data and cannot see tasks belonging to other users

**Independent Test**: An authenticated user can create tasks, view only their own tasks, update their tasks, and delete their tasks while being prevented from accessing any tasks belonging to other users

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement GET /api/{user_id}/tasks endpoint requiring authentication dependency from Spec 1 in backend/src/api/tasks.py
- [X] T012 [US1] Implement POST /api/{user_id}/tasks endpoint validating request payload and assigning user_id from authenticated user in backend/src/api/tasks.py
- [X] T013 [US1] Query tasks filtered by user_id and return list of tasks in backend/src/api/tasks.py
- [X] T014 [US1] Validate {user_id} against authenticated user in backend/src/api/tasks.py
- [X] T015 [US1] Implement database session dependency injection for task operations in backend/src/api/tasks.py
- [X] T016 [US1] Add proper error handling for unauthorized access in backend/src/api/tasks.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Task Operations (Priority: P1)

**Goal**: Allow authenticated users to perform various operations on their tasks (create, read, update, delete, toggle completion) through the API, with the system maintaining data integrity and proper authorization checks

**Independent Test**: An authenticated user can perform all task operations (create, read, update, delete, toggle completion) on their own tasks successfully

### Implementation for User Story 2

- [X] T017 [P] [US2] Implement GET /api/{user_id}/tasks/{id} endpoint enforcing authentication and querying task by id AND user_id in backend/src/api/tasks.py
- [X] T018 [US2] Implement PUT /api/{user_id}/tasks/{id} endpoint validating ownership and updating title/description only in backend/src/api/tasks.py
- [X] T019 [US2] Implement DELETE /api/{user_id}/tasks/{id} endpoint validating ownership and removing task from database in backend/src/api/tasks.py
- [X] T020 [US2] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint validating ownership and toggling completed boolean in backend/src/api/tasks.py
- [X] T021 [US2] Prevent user_id modification in update operations in backend/src/api/tasks.py
- [X] T022 [US2] Return 404 if task not found or not owned in backend/src/api/tasks.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Data Persistence & Integrity (Priority: P2)

**Goal**: Ensure tasks created by users are reliably stored in Neon PostgreSQL database with proper schema validation and data integrity, ensuring data persistence across application restarts

**Independent Test**: Tasks created by users persist in the database and maintain their properties after application restarts

### Implementation for User Story 3

- [X] T023 [P] [US3] Inject auth dependency into all routes and compare JWT user_id with {user_id} path param in backend/src/api/deps.py
- [X] T024 [US3] Reject mismatches with 401 Unauthorized in backend/src/api/deps.py
- [X] T025 [US3] Use correct HTTP status codes (401, 404, 400) consistently across all endpoints in backend/src/api/tasks.py
- [X] T026 [US3] Avoid leaking internal errors and standardize error responses in backend/src/api/tasks.py
- [X] T027 [US3] Validate data format and return 400 Bad Request for invalid input in backend/src/models/task.py
- [X] T028 [US3] Ensure idempotent behavior for table creation in backend/src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T029 [P] Generate .env.example file with DATABASE_URL and BETTER_AUTH_SECRET in .env.example
- [X] T030 Add inline documentation comments to configuration files
- [X] T031 Simulate valid authenticated request for validation
- [X] T032 [P] Simulate cross-user access attempt and confirm 401 Unauthorized response
- [X] T033 Simulate missing resource access and confirm 404 Not Found response
- [X] T034 Confirm data persistence and ownership enforcement in Neon PostgreSQL
- [X] T035 Map implementation back to sp.specify requirements and confirm compliance
- [X] T036 Run complete validation of backend functionality against spec requirements

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 task foundation
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Builds on US1/US2 task foundation

### Within Each User Story

- Authentication dependencies before API endpoints
- Data models before services
- Services before API endpoints
- Authentication validation integrated throughout
- Security measures implemented at each step

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement GET /api/{user_id}/tasks endpoint requiring authentication dependency from Spec 1 in backend/src/api/tasks.py"
Task: "Implement POST /api/{user_id}/tasks endpoint validating request payload and assigning user_id from authenticated user in backend/src/api/tasks.py"
Task: "Query tasks filtered by user_id and return list of tasks in backend/src/api/tasks.py"
Task: "Validate {user_id} against authenticated user in backend/src/api/tasks.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence