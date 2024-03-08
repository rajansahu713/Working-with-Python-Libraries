"""
Initializes and configures an AsyncIOScheduler instance to enable background job 
scheduling in a FastAPI application.

The scheduler is configured to use a SQLAlchemyJobStore backed by a SQLite database
to persist jobs across restarts. Some sample scheduled jobs are defined to illustrate
usage.

Application startup and shutdown events are registered to properly initialize and 
shutdown the scheduler.
"""
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os

# Create a FastAPI app instance
app = FastAPI()

# Define the SQLite database file path
database_path = 'jobs.sqlite'

# Initialize a SQLAlchemyJobStore with SQLite database
jobstores = {
    'default': SQLAlchemyJobStore(url=f'sqlite:///{database_path}')
}


# Initialize an AsyncIOScheduler with the jobstore
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='Asia/Kolkata') 
"""
Initializes an AsyncIOScheduler instance with a SQLAlchemyJobStore backed by an SQLite database.

This allows scheduling background jobs that will persist across application restarts. The jobs 
are stored in the SQLite database file provided by the database_path variable.

The scheduler instance is configured with a timezone of Asia/Kolkata.
"""


# Define a scheduled job function
@scheduler.scheduled_job('interval', seconds=1)
def scheduled_job_1():
    print("scheduled_job_1")


@scheduler.scheduled_job('date', run_date='2024-07-21 11:00:00')
def scheduled_job_2():
    print("scheduled_job_2")

@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=22, minute=30, second=0)
def scheduled_job_3():
    print("scheduled_job_3")



# Register an event for application startup
@app.on_event("startup")
async def startup_event():
    """
    Registers an event handler to start the scheduler when the app starts up.

    Checks if the database file already exists, and deletes it if so, to ensure
    a clean state for the scheduler. Then starts the scheduler.
    """
    if os.path.exists(database_path):
        os.remove(database_path)

    scheduler.start()

# Register an event for application shutdown
@app.on_event("shutdown")
async def shutdown_event():
    """
    Shuts down the AsyncIOScheduler instance on application shutdown.

    This is registered as an event handler for the FastAPI "shutdown" event. It calls 
    scheduler.shutdown() to gracefully shut down the scheduler.
    """
    scheduler.shutdown()

# Define a root route
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}



