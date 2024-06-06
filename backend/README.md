# backend

## Architecture
### REST API technology
We use 

### Running users' Python code
We run user code in a sandboxed environment using Docker containers.

This is to ensure that the environment is consistent and isolated for each user submission.

We'll have a background timer running to time out the execution of the code if it runs for too long (10 seconds). Otherwise, if the code successfully runs, then it is saved into a database and can be reused later.
