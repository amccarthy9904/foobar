# Docker and Kubernetes Integration Study Sheet

## 1. Docker

### Definition
Docker is a platform that enables developers to automate the deployment of applications inside lightweight, portable containers. Containers package an application and its dependencies, ensuring consistency across different environments.

### Components

1. **Docker Engine:**
   - The runtime environment for containers.
   - Manages building, running, and distributing containers.

2. **Docker Image:**
   - A lightweight, standalone, executable package that includes application code, runtime, libraries, and system tools.

3. **Dockerfile:**
   - A script that defines the steps to create a Docker image.
   - Specifies the base image, dependencies, and commands to run.

4. **Docker Hub:**
   - A cloud-based registry for sharing and storing Docker images.
   - Use `docker pull` to download images from Docker Hub.

## 2. Kubernetes and Docker Integration

### Overview
Kubernetes complements Docker by providing orchestration and management capabilities for containerized applications.

### Key Points

1. **Container Orchestration:**
   - Kubernetes automates the deployment, scaling, and management of Docker containers.

2. **Pods:**
   - The basic unit in Kubernetes is a pod, which can host one or more Docker containers.
   - Pods enable colocation of tightly coupled application components.

3. **Kubelet:**
   - An agent running on each node in the Kubernetes cluster.
   - Manages the containers and ensures they are running in a Pod.

4. **Kube-Proxy:**
   - Maintains network rules on nodes.
   - Enables communication across Pods and external traffic.

5. **Deployments:**
   - Kubernetes Deployments define desired state for Pods.
   - They ensure the specified number of replicas are running and facilitate rolling updates.

6. **Services:**
   - Kubernetes Services provide a stable endpoint to access a set of Pods.
   - LoadBalancer, NodePort, and ClusterIP are common service types.

7. **Ingress:**
   - Manages external access to services, allowing for routing and SSL termination.
   - Configured with Ingress resources.

8. **ConfigMaps and Secrets:**
   - Kubernetes resources for managing configuration data and sensitive information.

## 3. Docker and Kubernetes Workflow

### Workflow Steps

1. **Docker Image Creation:**
   - Develop and containerize the application using Docker.
   - Create a Dockerfile specifying the image configuration.

2. **Docker Image Registry:**
   - Push the Docker image to a container registry (e.g., Docker Hub, Azure Container Registry).

3. **Kubernetes Deployment:**
   - Create Kubernetes Deployment YAML file describing the application and specifying the Docker image.

4. **kubectl Apply:**
   - Use `kubectl apply -f <deployment.yaml>` to deploy the application to the Kubernetes cluster.

5. **Scaling:**
   - Adjust the number of replicas in the Deployment to scale the application horizontally.

6. **Updates:**
   - Modify the Docker image version in the Deployment YAML for updates.
   - Use `kubectl apply` for rolling updates.

7. **Monitoring and Scaling:**
   - Utilize Kubernetes monitoring tools to observe application performance.
   - Use autoscaling based on resource metrics.

8. **Rollback:**
   - If issues arise, rollback to a previous version using Kubernetes deployment rollback features.

## Additional Resources
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
