🌦️ Gothenburg Weather App

A FastAPI-based weather application that provides real-time weather updates for Gothenburg, Sweden — automated end-to-end with a CI/CD pipeline using GitHub Actions, Docker, and Kubernetes (Minikube).

🚀 Project Overview

This project demonstrates a DevOps pipeline integrating modern tools and best practices:

FastAPI for building a lightweight backend API

Docker for containerization

GitHub Actions for Continuous Integration & Deployment

Kubernetes (Minikube) for container orchestration

ConfigMaps for environment variable management

The goal is to simulate a production-grade deployment workflow entirely in a local Kubernetes environment, ideal for DevOps learning and demos.

🏗️ Architecture

            ┌───────────────────────────┐
            │  GitHub Repository         │
            │  (Code + Workflow YAML)    │
            └─────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │  GitHub Actions           │
             │  (CI/CD Pipeline)         │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │  Docker Hub               │
             │  (Image push/pull)        │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │  Kubernetes (Minikube)   │
             │  Deployment + Service     │
             └───────────────────────────┘

⚙️ Tech Stack

Category	Tool
Backend Framework	FastAPI
Language	            Python 3.9
Containerization	Docker
CI/CD	            GitHub Actions
Orchestration	Kubernetes (Minikube)
Cloud Registry	Docker Hub
Configuration	ConfigMap

📁 Repository Structure


├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── requirements.txt     # Python dependencies
│   ├── templates/           # HTML UI templates
│   └── static/              # CSS and JS files
├── deployment.yaml          # Kubernetes Deployment
├── service.yaml             # Kubernetes Service
├── configmap.yaml           # Environment variables
├── Dockerfile               # Container build file
├── .github/workflows/
│   └── ci-cd.yml            # GitHub Actions pipeline
└── README.md                # Project documentation

🧪 CI/CD Workflow Summary

Every push to the main branch triggers GitHub Actions to:
1️⃣ Build and test the FastAPI app
2️⃣ Build a Docker image
3️⃣ Push the image to Docker Hub
4️⃣ Trigger a Kubernetes deployment update using the latest image

🐳 Docker Setup

# Build the Docker image
docker build -t gothenburg-weather:latest .

# Run locally
docker run -p 8080:8080 gothenburg-weather:latest


Then open http://localhost:8080
 in your browser.

☸️ Kubernetes Deployment (Minikube)
# Start Minikube
minikube start

# Apply manifests
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Access the app
minikube service gothenburg-weather-service --url

🔄 CI/CD with GitHub Actions

Your pipeline automatically:

Installs dependencies

Runs basic tests

Builds & pushes image to Docker Hub

Updates Kubernetes deployment

Example workflow file: .github/workflows/ci-cd.yml

🌐 Accessing the Application

When deployed via Minikube:

minikube service gothenburg-weather-service --url


Visit the provided URL (example: http://127.0.0.1:63138) to view the live UI.


🧠 Learnings

Through this project, I practiced:

Automating deployments with GitHub Actions

Managing environment configs using ConfigMaps

Handling image versioning with Docker Hub

Running production-like workloads on Kubernetes

Integrating DevOps tools for continuous delivery

Added Prometheus + Grafana for monitoring


👩‍💻 Author

Deepika Elangovan
🔹 DevOps Engineer | Azure | Kubernetes | CI/CD Automation

