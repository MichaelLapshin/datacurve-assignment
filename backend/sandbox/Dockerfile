# We create a sandbox environment for the user to execute Python code
FROM python:3.11.6

WORKDIR /usr/sandbox

# Switch to an unpriviledged user
USER sandbox

# Install environment dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Run the user code
ENV USER_CODE "print('User code is not specified'); exit 1;"
ENTRYPOINT [ "python", "-c", "$USER_CODE" ]