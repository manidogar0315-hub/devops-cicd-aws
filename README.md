.

🚀 DevOps CI/CD Project

Docker · GitHub Actions · Docker Hub








📌 Project Overview

This project demonstrates a basic yet complete DevOps CI/CD workflow.

A Flask application is containerized using Docker, version-controlled with GitHub, and automatically built & pushed to Docker Hub using GitHub Actions CI/CD whenever code is pushed.

This repository currently focuses on CI/CD automation.
Cloud deployment (AWS) is planned as the next phase.

🛠 Tools & Technologies

Python (Flask) – Application

Docker – Containerization

Git & GitHub – Version control

Docker Hub – Image registry

GitHub Actions – CI/CD automation

📁 Project Structure

devops-cicd-aws
├── app.py
├── requirements.txt
├── Dockerfile
├── .github
│   └── workflows
│       └── docker-ci.yml
└── README.md

⚙️ Application Flow (Simple Diagram)
Developer
   |
   | git push
   v
GitHub Repository
   |
   | GitHub Actions (CI/CD)
   v
Docker Image Build
   |
   v
Docker Hub

🔄 CI/CD Pipeline

Trigger:
Push to main branch

Steps:

Checkout source code

Login to Docker Hub (via GitHub Secrets)

Build Docker image

Push Docker image to Docker Hub

📌 This process is fully automated — no manual Docker commands needed.

🚀 Run the Application Locally
docker run -p 5001:5000 manidogar/devops-cicd-aws:latest


Open in browser:

http://localhost:5001

📦 Docker Hub Image

🔗 https://hub.docker.com/r/manidogar/devops-cicd-aws

🔐 Security Practices

Docker credentials stored using GitHub Actions Secrets

No passwords or tokens hard-coded in repository

🔮 Planned Next Steps

Deploy container on AWS EC2

Add basic monitoring & logging

Improve scalability and security

🧠 What This Project Demonstrates

Containerization using Docker

CI/CD automation using GitHub Actions

Secure handling of credentials

Real-world DevOps workflow fundamentals

👤 Author

Abdul Rehman Dogar
Aspiring DevOps Engineer | Learning by building 🚀
