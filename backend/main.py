from fastapi import FastAPI
import logging

from sandbox.sandbox import Sandbox
from database import Database

# Run the FastAPI app
logging.info("Starting server...")
app = FastAPI()

# Logic routes
@app.post("/test-code")
def post_test_code(submission: str):
    sandbox = Sandbox(submission)
    sandbox.run()
    return {sandbox.stdout, sandbox.stderr}

@app.post("/submit")
def post_test_code(submission: str):
    sandbox = Sandbox(submission)
    sandbox.run()

    if sandbox.status_code == 0:
        # Save successful submission to the database
        Database().save_submission(submission)
        Database().save_run(sandbox.stdout, sandbox.stderr, sandbox.status_code)

    return {sandbox.stdout, sandbox.stderr}
