from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import auth, chat, actions,workspace

app = FastAPI(title="Research Co-Pilot")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev (later restrict)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(actions.router, prefix="/actions")
app.include_router(workspace.router, prefix="/workspace")

@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}