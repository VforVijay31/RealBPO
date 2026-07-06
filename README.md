# RealBPO

RealBPO is a Django-based BPO management website that helps business owners keep track of outsourced work in a structured way. The platform acts as a central log for outsourced projects, allowing owners to monitor progress, completion percentage, and key contact details for each outsourced partner or service.

## Features

- Business owner dashboard for managing outsourced projects
- Role-based access control (RBAC)
- Owner can create and manage projects
- Owner can create employee accounts and provide login credentials
- Employees can log in and access project-related information
- Employees can add and edit outsourced services
- Owners can update project details and oversee outsourced work
- Django built-in authentication system
- Track outsourced work progress and completion percentage
- Store contact details related to outsourced work

## Tech Stack

- Python
- Django
- SQLite
- Docker
- Jenkins

## Project Structure

- `realbpo/` - Django project package
- `accounts/` - User and authentication-related logic
- `home/` - Project, service, and dashboard functionality
- `templates/` - HTML templates for the web interface
- `Dockerfile` - Container build configuration
- `compose.yaml` - Docker Compose configuration
- `jenkinsfile` - Jenkins pipeline configuration

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (optional, for containerized deployment)

### Local Development

1. Clone the repository
2. Navigate to the project folder
3. Install dependencies:

```bash
pip install -r realbpo/requirements.txt
```

4. Run database migrations:

```bash
python realbpo/manage.py migrate
```

5. Start the development server:

```bash
python realbpo/manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## Docker Deployment

A prebuilt Docker image is already available in a public Docker repository and can be pulled directly:

```bash
docker pull vijayshriram2005/realbpo:v1
```

To start it with Docker Compose, use:

```bash
docker compose up -d
```

To run it separately with Docker, use:

```bash
docker run -p 8000:8000 vijayshriram2005/realbpo:v1
```

If you want to map it to a different host port, use a command like this:

```bash
docker run -p 8080:8000 vijayshriram2005/realbpo:v1
```

## Jenkins

A Jenkins pipeline configuration is included in `jenkinsfile` for CI/CD automation.

## License

This project is for educational and demo purposes.
