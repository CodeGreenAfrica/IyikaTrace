from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base

from routes.users import router_users
from routes.batches import router_batches
from routes.trace_logs import router_trace_logs
from routes.locations import router_locations
from routes.documents import router_documents

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
