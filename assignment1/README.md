
# Assignment 1: Dockerized Python Application

This project demonstrates how to dockerize a Python application using Docker. The application creates or updates a file named `random.txt` with 100 random characters each time the container runs. This file is stored in a Docker volume to persist data across container lifecycles.

## Prerequisites

Ensure Docker is installed on your system. For installation instructions, refer to the official [Docker documentation](https://docs.docker.com/get-docker/).

## Setup Instructions

### 1. Building the Docker Image

To build the Docker image for the application, navigate to the root of the `assignment1` directory and run the following command:

```bash
docker build -t assignment1 .
```

This command builds a Docker image named `assignment1` based on the Dockerfile located in the current directory.

### 2. Creating the Docker Volume

Before running the container, create a Docker volume named `servervol`. This volume is used to persist the `random.txt` file. Execute the following command to create the volume:

```bash
docker volume create servervol
```

### 3. Running the Container

Run the Docker container with the following command:

```bash
docker run -v servervol:/serverdata assignment1
```

This command mounts the `servervol` volume to the `/serverdata` directory inside the container. The Python application will create or update the `random.txt` file in this directory.

### 4. Accessing the Container's Shell

To access the shell of the container instead of running the application, use the following command:

```bash
docker run -it -v servervol:/serverdata assignment1 /bin/bash
```

This command opens an interactive bash shell inside the container, allowing you to manually execute commands or scripts.

#### Running the Python Application Manually

While in the container's shell, you can manually run the Python application by navigating to the application directory and executing:

```bash
python text_gen.py
```

## Exiting the Container

To exit the container's shell, type `exit` and press Enter. This will stop the shell session and return you to your host machine's command line.

## Additional Information

This `README.md` file explains how to build and run a Docker container for a Python application, how to create and use a Docker volume for data persistence, and how to access the container's shell for manual operations. The `Dockerfile` and `text_gen.py` script are located in the `assignment1` directory and its subdirectory `app`, respectively.
