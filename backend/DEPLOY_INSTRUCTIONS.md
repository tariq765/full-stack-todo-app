# Instructions to Deploy Backend on Hugging Face Spaces

## Step 1: Prepare Files
All necessary files are in the zip file `todo-backend-hf.zip` located at:
`C:\Users\Hp\OneDrive\Desktop\TODO WEB PHASE2\backend\todo-backend-hf.zip`

## Step 2: Upload to Hugging Face
1. Go to https://huggingface.co/spaces
2. Click "Duplicate a Space" or create a new one
3. Choose any name for your space
4. Select SDK: "Docker" (important!)
5. Upload all files from the zip file:
   - app.py
   - requirements.txt
   - Dockerfile
   - api/ folder
   - core/ folder
   - db/ folder
   - models/ folder
   - SPACE_README.md

## Step 3: Environment Variables (Optional but Recommended)
In your Hugging Face Space settings, add these environment variables:
- SECRET_KEY: (generate a strong random key)
- ACCESS_TOKEN_EXPIRE_MINUTES: 43200 (30 days in minutes)

## Step 4: Start the Space
1. After uploading files, click "Restart Space"
2. Wait for the build to complete (may take a few minutes)
3. Your backend will be available at: https://your-username-space-name.hf.space

## Step 5: Update Frontend
Once your backend is running:
1. Update your Vercel frontend environment variable:
   - Key: `NEXT_PUBLIC_API_URL`
   - Value: Your new Hugging Face URL (e.g., https://your-username-space-name.hf.space)
2. Redeploy your Vercel frontend

## Expected Endpoints:
- POST /api/auth/login
- POST /api/auth/register
- GET /api/auth/verify
- GET /api/{user_id}/tasks
- POST /api/{user_id}/tasks
- PUT /api/{user_id}/tasks/{task_id}
- PATCH /api/{user_id}/tasks/{task_id}
- DELETE /api/{user_id}/tasks/{task_id}

## Troubleshooting:
- If you see "Your space is in error", check the logs in your Space settings
- Make sure all folders (api, core, db, models) are uploaded
- Ensure requirements.txt has all necessary packages
- Verify that app.py contains the FastAPI app object named "app"

## Important Notes:
- The application uses SQLite database which is suitable for demo purposes
- For production, consider using PostgreSQL or other persistent databases
- The CORS settings allow all origins - restrict these in production