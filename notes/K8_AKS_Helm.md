# Kubernetes Study Sheet

## 1. Kubernetes

### Definition
Kubernetes (K8s) is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.

### General Use Case
- **Container Orchestration:** Kubernetes simplifies the deployment and management of containerized applications, providing tools for scaling, updating, and monitoring.

### First Steps
1. **Installation:**
   - Use `kubeadm` or a managed Kubernetes service.
   - Example: `kubeadm init` for a basic cluster.

2. **Pods:**
   - Pods are the smallest deployable units and can contain one or more containers.
   - Create a pod YAML file and deploy it using `kubectl apply -f <pod.yaml>`.

3. **ReplicaSets:**
   - Ensure high availability and scalability.
   - Define and manage multiple replicas of a pod.

4. **Services:**
   - Expose pods to the network within or outside the cluster.
   - Use `kubectl expose` or create a Service YAML file.

5. **Deployments:**
   - Higher-level abstraction for managing ReplicaSets and Pods.
   - Allows rolling updates and rollbacks.

## 2. Azure Kubernetes Service (AKS)

### Definition
Azure Kubernetes Service (AKS) is a managed Kubernetes service provided by Microsoft Azure.

### Changes in Interactions with Kubernetes
- **Simplified Deployment:**
  - AKS abstracts away much of the complexity of setting up and managing a Kubernetes cluster.
  - Use the Azure Portal or Azure CLI to create and manage AKS clusters.

- **Integrated Azure Services:**
  - AKS integrates with other Azure services, such as Azure Active Directory, Azure Monitor, and Azure Policy.

- **Automated Upgrades:**
  - AKS provides automated Kubernetes version upgrades, reducing maintenance overhead.

## 3. Helm

### Definition
Helm is a package manager for Kubernetes applications. It simplifies the deployment and management of Kubernetes applications by defining, installing, and upgrading even the most complex Kubernetes applications.

### Managing a Kubernetes Cluster with Helm
1. **Installation:**
   - Install Helm on your local machine and initialize the Helm client and server components in the Kubernetes cluster.

2. **Charts:**
   - Charts are Helm packages. Create a Helm chart for your application using `helm create <chart-name>`.

3. **Values and Templates:**
   - Customize Helm charts using values files and templates.
   - Values files contain configurable parameters, and templates define Kubernetes manifests.

4. **Installing and Upgrading:**
   - Use `helm install` to deploy a chart and `helm upgrade` to update a release with a new version.

5. **Repositories:**
   - Publish and share Helm charts via repositories.
   - Add repositories using `helm repo add` and search for charts with `helm search`.

6. **Rollback:**
   - Rollback to a previous release version in case of issues using `helm rollback`.

7. **Hooks:**
   - Execute pre and post actions during install, upgrade, or deletion using Helm hooks.

## Additional Resources
- [Official Kubernetes Documentation](https://kubernetes.io/docs/)
- [Azure Kubernetes Service Documentation](https://docs.microsoft.com/en-us/azure/aks/)
- [Helm Documentation](https://helm.sh/docs/)