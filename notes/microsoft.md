# Study Sheet

## Subjects

### 1. Azure Cloud Services
- **Azure Kubernetes Service (AKS)**
  - *Overview:*
    - Managed Kubernetes service by Microsoft Azure.
    - Simplifies deployment, management, and scaling of containerized applications.

  - *Key Concepts:*
    - Pods, Nodes, and Clusters in AKS.
    - Deployments and Replication Controllers.

### Pods
- **Definition:**
  - Smallest deployable units in Kubernetes.
  - Containers within a pod share the same network namespace.

- **Key Concepts:**
  - Pods encapsulate one or more containers.
  - Containers within a pod communicate using localhost.

### Nodes
- **Definition:**
  - Physical or virtual machines that run pods.
  - Form the underlying infrastructure of a Kubernetes cluster.

- **Key Concepts:**
  - Nodes host multiple pods.
  - Kubernetes components (e.g., kubelet) run on each node.

### Clusters in AKS
- **Definition:**
  - A set of nodes grouped together to form a single, logical unit.
  - Managed by Azure Kubernetes Service (AKS) in the case of Microsoft Azure.

- **Key Concepts:**
  - AKS abstracts cluster management complexities.
  - Multiple clusters can exist within an AKS subscription.

## Deployments and Replication Controllers

### Deployments
- **Definition:**
  - A higher-level abstraction for managing pods.
  - Allows declarative updates to applications.

- **Key Concepts:**
  - Desired state specified in a deployment is maintained.
  - Facilitates rolling updates and rollbacks.

### Replication Controllers
- **Definition:**
  - Ensures a specified number of pod replicas are running.
  - Part of the historical Kubernetes deployment model.

- **Key Concepts:**
  - Monitors and maintains the desired number of pod replicas.
  - Supports scaling horizontally by adjusting the replica count.

## Helm
- **Helm Deployments**
  - *Overview:*
    - Package manager for Kubernetes applications.
    - Simplifies deployment, scaling, and management using charts.

  - *Key Concepts:*
    - Charts, Templates, and Values in Helm.
    - Helm Repositories.

#### Helm Charts
- **Definition:**
  - A package of pre-configured Kubernetes resources.
  - Simplifies the deployment and management of Kubernetes applications.

- **Key Concepts:**
  - Charts contain templates, default values, and metadata.
  - Encapsulates Kubernetes manifest files for applications.

#### Templates in Helm
- **Definition:**
  - Dynamically generate Kubernetes manifest files.
  - Allow parameterization for flexibility.

- **Key Concepts:**
  - Helm uses Go templates for manifest file generation.
  - Templates support conditionals, loops, and functions.

- **Hands-On Practice:**
  - Explore and modify template files within a Helm chart.
  - Use template functions and variables for customization.

#### Values in Helm
- **Definition:**
  - Configuration settings for Helm charts.
  - Allow customization without modifying chart templates.

- **Key Concepts:**
  - Values are defined in a values.yaml file.
  - Can be overridden during chart installation or upgrade.

- **Hands-On Practice:**
  - Define and organize values in a values.yaml file.
  - Override values during Helm chart installation.

#### Helm Repository Basics
- **Definition:**
  - A centralized location for storing and sharing Helm charts.
  - Repositories simplify the distribution of Helm charts.

- **Key Concepts:**
  - Repositories host chart packages and their metadata.
  - Charts can be versioned within a repository.

- **Hands-On Practice:**
  - Create a local Helm chart repository.
  - Publish and share a Helm chart to the repository.

#### Using Public Helm Repositories
- **Official Helm Hub:**
  - Central repository for Helm charts.
  - Provides a wide range of charts for common applications.

- **Key Concepts:**
  - Helm CLI commands for searching and installing charts.
  - Managing dependencies from public repositories.

- **Hands-On Practice:**
  - Search for and install a chart from the Helm Hub.
  - Manage dependencies and versions effectively.

#### Private Helm Repositories
- **Definition:**
  - Custom repositories for hosting private or organization-specific charts.
  - Enhances control and security over Helm chart distribution.

- **Key Concepts:**
  - Configuring Helm to use private repositories.
  - Authentication and access control for private repositories.

- **Hands-On Practice:**
  - Set up a private Helm repository.
  - Authenticate and publish a private Helm chart.

- **Azure Container Service**
  - *Overview:*
    - Older Azure service; consider focusing on AKS for newer projects.
    - Offers multiple orchestration options, including Kubernetes.

  - *Key Concepts:*
    - Container Service Models (ACS-Engine, Kubernetes, Docker Swarm).
    - Deploying containerized applications.

  - *Hands-On Practice:*
    - Deploying containers using ACS-Engine.
    - Comparing ACS-Engine, Kubernetes, and Docker Swarm.

  - *Best Practices:*
    - Choosing the right orchestration service for specific use cases.
    - Migrating from Azure Container Service to AKS.

- **Azure DevOps CI/CD Pipelines**
  - *Overview:*
    - CI/CD (Continuous Integration/Continuous Deployment) platform by Microsoft.
    - Automates software delivery processes.

  - *Key Concepts:*
    - Pipelines, Jobs, and Stages in Azure DevOps.
    - Integration with Git repositories.

  - *Hands-On Practice:*
    - Creating CI/CD pipelines for various application types.
    - Implementing release strategies.

  - *Best Practices:*
    - Implementing secure and efficient CI/CD workflows.
    - Monitoring and optimizing pipeline performance.

### 2. Debugging Tools
- **Kusto**
  - *Overview:*
    - Data exploration and analytics platform by Microsoft.
    - Used for querying large datasets.

  - *Key Concepts:*
    - Kusto Query Language (KQL).
    - Data analysis and visualization in Azure Data Explorer.

  - *Hands-On Practice:*
    - Writing and executing basic KQL queries.
    - Analyzing and visualizing data using Kusto.

  - *Best Practices:*
    - Optimizing queries for performance.
    - Leveraging Kusto for log analysis and troubleshooting.

- **Geneva**
  - *Overview:*
    - Microsoft's internal telemetry and monitoring platform.
    - Used for collecting and analyzing application telemetry data.

  - *Key Concepts:*
    - Instrumentation and telemetry in application code.
    - Data collection and visualization in Geneva.

  - *Hands-On Practice:*
    - Instrumenting code for telemetry using Geneva.
    - Analyzing telemetry data for troubleshooting.

  - *Best Practices:*
    - Implementing effective application instrumentation.
    - Utilizing Geneva for proactive monitoring and issue detection.

- **Prometheus**
  - *Overview:*
    - Open-source monitoring and alerting toolkit.
    - Designed for reliability and scalability.

  - *Key Concepts:*
    - Prometheus Query Language (PromQL).
    - Alerting rules and targets.

  - *Hands-On Practice:*
    - Setting up Prometheus for monitoring.
    - Creating custom alerts and dashboards.

  - *Best Practices:*
    - Configuring Prometheus for optimal performance.
    - Integrating Prometheus with Kubernetes for containerized application monitoring.

### 3. Infrastructure Engineering
- **Designing Secure and Scalable Cloud Infrastructure on Azure**
  - *Overview:*
    - Focus on building robust and secure cloud architecture.
    - Consideration for scalability and performance.

  - *Key Concepts:*
    - Azure Resource Manager (ARM) templates.
    - Networking and security considerations.

  - *Hands-On Practice:*
    - Creating ARM templates for infrastructure provisioning.
    - Implementing network security groups and virtual networks.

  - *Best Practices:*
    - Implementing Identity and Access Management (IAM) for resources.
    - Regularly reviewing and updating infrastructure design for security.

- **Utilizing Azure Functions**
  - *Overview:*
    - Serverless compute service by Microsoft Azure.
    - Allows the execution of code in response to events without the need for infrastructure management.

  - *Key Concepts:*
    - Function triggers and bindings.
    - Serverless architecture advantages and considerations.

  - *Hands-On Practice:*
    - Creating and deploying Azure Functions.
    - Implementing serverless workflows.

  - *Best Practices:*
    - Optimizing Azure Functions for cost and performance.
    - Integrating Azure Functions with other Azure services.

- **PostgreSQL**
  - *Overview:*
    - Open-source relational database management system.
    - Supports a wide range of SQL features.

  - *Key Concepts:*
    - Tables, Indexes, and Constraints in PostgreSQL.
    - Query optimization strategies.

  - *Hands-On Practice:*
    - Setting up and configuring PostgreSQL databases.
    - Writing and optimizing SQL queries.

  - *Best Practices:*
    - Implementing data backup and recovery strategies.
    - Monitoring and optimizing PostgreSQL performance.

### 4. Logging and Monitoring
- **Comprehensive Logging with Kusto**
  - *Overview:*
    - Log analytics platform by Microsoft.
    - Centralized logging and analysis for troubleshooting and monitoring.

  - *Key Concepts:*
    - Log ingestion and querying in Azure Log Analytics.
    - Building custom queries for log analysis.

  - *Hands-On Practice:*
    - Configuring log sources for Azure Log Analytics.
    - Writing and executing custom log queries.

  - *Best Practices:*
    - Implementing effective log ingestion for various sources.
    - Utilizing Kusto for root cause analysis and proactive issue detection.

- **Geneva for Monitoring**
  - *Overview:*
    - Telemetry and monitoring platform by Microsoft.
    - Collects and analyzes application telemetry data for insights.

  - *Key Concepts:*
    - Instrumentation in code for telemetry.
    - Visualizing telemetry data using Geneva.

  - *Hands-On Practice:*
    - Integrating Geneva into application code for telemetry.
    - Analyzing telemetry data for monitoring and troubleshooting.

  - *Best Practices:*
    - Implementing comprehensive application instrumentation for monitoring.
    - Utilizing Geneva for predictive monitoring and trend analysis.

- **Prometheus for Operational Excellence**
  - *Overview:*
    - Open-source monitoring and alerting toolkit.
    - Focus on reliability, scalability, and operational excellence.

  - *Key Concepts:*
    - Metrics collection and storage using Prometheus.
    - Creating and managing alerts.

  - *Hands-On Practice
