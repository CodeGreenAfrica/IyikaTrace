from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.backend.db.database import engine, Base
from apps.backend import models
from apps.backend.routes.users import router_users
from apps.backend.routes.batches import router_batches
from apps.backend.routes.trace_logs import router_trace_logs
from apps.backend.routes.locations import router_locations
from apps.backend.routes.documents import router_documents

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="IyikaTrace API")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(router_users)
app.include_router(router_batches)
app.include_router(router_trace_logs)
app.include_router(router_locations)
app.include_router(router_documents)

@app.get("/")
def root():
    return {"message": "Welcome to IyikaTrace API"}
