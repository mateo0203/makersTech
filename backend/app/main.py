from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chatbot import router as chatbot_router
from app.database import engine, Base
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Makers Tech Chatbot API",
    description="An AI-powered chatbot for a technology e-commerce platform.",
    version="1.0.0",
)

# Enable CORS (For frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables (only necessary if not using Alembic migrations)
Base.metadata.create_all(bind=engine)

# Include chatbot routes
app.include_router(chatbot_router, prefix="/api")

# Root endpoint for testing
@app.get("/")
def home():
    print("jsjs")
    return {"message": "Welcome to Makers Tech Chatbot API 🚀"}

# Run the server (if running directly)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
