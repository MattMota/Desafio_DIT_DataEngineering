# Defines version for Python image
FROM python:3.9

# Installs PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Sets working directory inside the container
WORKDIR /app

# Copies project files from the project's
# working directory to the container's WD
COPY . .

# Installs proj dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Makes Prefect visible in the container's local network
EXPOSE 4200

# Starts Prefect server
CMD ["prefect", "agent", "local", "start"]
