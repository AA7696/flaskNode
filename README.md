# 🚀 Flask + Express CI/CD Deployment using Docker & Jenkins

## 👨‍💻 Author
**AA7696**

---

## 🧾 Project Overview

This project demonstrates how to:

- Dockerize and deploy a **Flask backend** and **Express frontend** on a single **EC2 instance**.
- Use **Docker Compose** for container orchestration.
- Automate deployment with a **Jenkins CI/CD pipeline** triggered by GitHub pushes.

---

## 🧱 Tech Stack

- **Backend:** Python Flask (port `5000`)
- **Frontend:** Node.js Express + EJS (port `3000`)
- **Containerization:** Docker & Docker Compose
- **CI/CD:** Jenkins (port `8080`)
- **Hosting:** AWS EC2 (Ubuntu 20.04)

---

## ⚙️ Directory Structure

flaskNode/
│
├── backend/ # Flask API
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/ # Express App
│ ├── app.js
│ ├── views/
│ ├── package.json
│ └── Dockerfile
│
├── docker-compose.yml
└── Jenkinsfile

## 🌐 Deployment Architecture  


---

## 🧰 Step-by-Step Setup

### 🔹 1. Provision EC2

- Launch Ubuntu 20.04 EC2 Instance
- Open **inbound ports** in EC2 Security Group:
  - `22` (SSH)
  - `3000` (Frontend)
  - `5000` (Backend)
  - `8080` (Jenkins)

---

### 🔹 2. Install Docker & Jenkins

```bash
sudo apt update
sudo apt install -y docker.io git

# Enable Docker service
sudo systemctl enable docker
sudo systemctl start docker

# Add current user to docker group
sudo usermod -aG docker ubuntu
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

sudo apt install -y openjdk-17-jdk
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install -y jenkins

# Start Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins

sudo usermod -aG docker jenkins
sudo systemctl restart jenkins

Set Up Jenkins

Go to http://<EC2_PUBLIC_IP>:8080

Unlock Jenkins with the initial password:

sudo cat /var/lib/jenkins/secrets/initialAdminPassword


Install suggested plugins

Create admin user


Install Jenkins Plugins

Install the following plugins:

Git Plugin

Docker Pipeline

Pipeline

GitHub Integration

NodeJS Plugin (Optional if not using Jenkins to run npm directly)

Configure GitHub Webhook

Go to your GitHub repo → Settings > Webhooks

Add webhook:

Payload URL: http://<EC2_PUBLIC_IP>:8080/github-webhook/

Content type: application/json

Trigger: Just the push event