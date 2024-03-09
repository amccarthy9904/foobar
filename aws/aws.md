### Links
[practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-developer-associate-practice-exams/)
[video](https://www.youtube.com/watch?v=RrKRN9zRBWs)
[shorter video](https://www.youtube.com/watch?v=bhomsGI56Ok)
[AWS Lambda cheat sheet](https://tutorialsdojo.com/aws-lambda/)
[AWS Lambda best practives](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
[AWS KMS cheat sheet](https://tutorialsdojo.com/aws-key-management-service-aws-kms/)
[AWS Coloudformation cheat sheet](https://tutorialsdojo.com/aws-cloudformation/)
[AWS Coloudformation CLI reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html)
[AWS Serverless Application Model Cheat Sheet](https://tutorialsdojo.com/aws-serverless-application-model-sam/)
[AWS DynamoDB cheet sheet](https://tutorialsdojo.com/amazon-dynamodb/)
[AWS elasticache cheat sheet](https://tutorialsdojo.com/amazon-elasticache/)
[AWS Elastic Beanstalk Cheat Sheet](https://tutorialsdojo.com/aws-elastic-beanstalk/)
[AWS EC2 Elastic Compute Cloud Cheat Sheet](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)
[Amazon ECS Elastic Container Service Cheat Sheet](https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/)
[ebextensions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)
[AWS CodeDeploy Cheat Sheet](https://tutorialsdojo.com/aws-codedeploy/)
[AWS CodeCommit Cheat Sheet](https://tutorialsdojo.com/aws-codecommit/)
### Exam guide

passing grade: 72%

65 questions
130mins - 2 mins per qu

mult choice - 1 of 4
mulit reposnse 2 or more of 5

#### Domains

1. Deployment - 22%
2. Security - 25%
3. Development with AWS services 30%
4. Refactoring 10%
5. Monitoring Troubleshooting 12%

#### Whitepapers

exam questions are based off whitepapers
to read:
[AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf#welcome)
[Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/pdfs/whitepapers/latest/practicing-continuous-integration-continuous-delivery/practicing-continuous-integration-continuous-delivery.pdf?did=wp_card&trk=wp_card)

#### Elastic Beanstalk EB

deploy and manage apps w/o worrying about underlying infrastructure
Paas - platform as a service
Not recommended for production enterprise apps
does alot of stuff for you
Rotates passwords
blue-green deployments
auto sclaing groups
rds database
runs dockerized containers

supports go, node, java, python, ruby etc

##### EB web vs worker env

web apps go on web
usually need both
web talks to workers to do tasks in background

###### EB web env
EC2 instances running aauto scaling group
load balanced envs 
or 
single instance env
no load balance
still has auto scaling group - ASG


###### EB worker env
EC2 instances in auto scaling group
SQS queue 
installs sqs daemon on EC2 so they can talk to the SQS queue

#### EB Deployment Policies

1. All at once
    - load balacned env + Single Instance
    - deploy new app version to all instances at same time
    - all instnaces out of service during deployment
    - downtime - interrupts trasactions
    - very risky, fastest
    - may need to roll everything back if something goes wrong

2. Rolling
    - load balacned env only
    - load balancer is needed to bring up new instances and bring them down
    - deploy new version to batch of instances at one time
    - for each patch
    - take them out of service
    - update
    - reattach updated batch
    - safer and slower than all at once
    - painful rollback

3. Rolling with additional batch
    - load balacned env only
    - launch new instance to replace a batch
    - deploy update app version to new batch
    - attach new batch and terminate the old
    - never reduces capacity
    - costs more than regular rolling
    - roll back painful

4. Immutable
    - load balacned env + Single Instance
    - reliant on ASG
    - make new ASG with all replacement EC2 instances
    - deploy updated app on new EC2s
    - point ELB to new ASG
    - delete old ASG
    - safest way to deploy for crit apps
    - if fail you can use old EC2s

5. Canary
    - load balacned env + Single Instance
    - Load balancer sends small percentage of traffic to new version
    - Use metrics to measure the success of the deployment; this indicates whether the deployment should continue or roll back
    - Increase the load on the new version until either all users are on the new version or you have fully rolled back.

6. blue/green
    - only one w/ DNS change
    - similar to immutable
    - replicate environment w/ updated version
    - swap URL from old Load Balacner to new LB
    - DNS changes have to propgate through DNS servers you dont control
    - if old goes down users could get 404s

#### EB in place vs blue green

in place could mean a few different things

1. within the scope of Elastic Beanstock env
    - all but blue green are in place
2. within the scope of the same server EC2 instance
    - all at once, rolling
    - servers before and after are the same
3. within the scope of uninterrupted server
    - blue green is occuriing on the server itself
    - not possible on EB
    - fast zero downtime deployment
    - Ruby on Rails + unicorn does this

B/G within context of EB:
    - you can bring up 2nd env within current ASG
    - then swap from old to the new
    - deactivate the old
    - no interruption in service from DNS servers
    - DBs must be outside EB envs

#### EB Configuration Files
.ebextensions is a folder at root of proj
inside you put <name>.config files
can control
option settings - linux windows server config - custom resources

#### EB Env Manifest

environment manifest is in file env.yml
stored at root fo proj
configures elastic beanstalk
[image here](https://youtu.be/RrKRN9zRBWs?t=2774)
EnvironmentName: prod1
SolutionStack: Node
EnvironmentLinks:
    "WORKERQUEUE" : "workerprod"
OptionsSettings:
    aws:elb:loadbalancer:
        CrossZone: true
many more options














## AWS

Content outline
This exam guide includes weightings, content domains, and task statements for the
exam. This guide does not provide a comprehensive list of the content on the exam.
However, additional context for each task statement is available to help you prepare
for the exam.
The exam has the following content domains and weightings:
• Domain 1: Development with AWS Services (32% of scored content)
• Domain 2: Security (26% of scored content)
• Domain 3: Deployment (24% of scored content)
• Domain 4: Troubleshooting and Optimization (18% of scored content)

### Domain 1: Development with AWS Services
#### Task Statement 1: Develop code for applications hosted on AWS.
Knowledge of:
• Architectural patterns (for example, event-driven, microservices, monolithic,
choreography, orchestration, fanout)
• Idempotency
• Differences between stateful and stateless concepts
• Differences between tightly coupled and loosely coupled components
• Fault-tolerant design patterns (for example, retries with exponential
backoff and jitter, dead-letter queues)
• Differences between synchronous and asynchronous patterns
Skills in:
• Creating fault-tolerant and resilient applications in a programming
language (for example, Java, C#, Python, JavaScript, TypeScript, Go)
• Creating, extending, and maintaining APIs (for example, response/request
transformations, enforcing validation rules, overriding status codes)
• Writing and running unit tests in development environments (for example,
using AWS Serverless Application Model [AWS SAM])
• Writing code to use messaging services
• Writing code that interacts with AWS services by using APIs and AWS SDKs
• Handling data streaming by using AWS services
#### Task Statement 2: Develop code for AWS Lambda.
Knowledge of:
• Event source mapping
• Stateless applications
• Unit testing
• Event-driven architecture
• Scalability
• The access of private resources in VPCs from Lambda code
Skills in:
• Configuring Lambda functions by defining environment variables and
parameters (for example, memory, concurrency, timeout, runtime, handler,
layers, extensions, triggers, destinations)
• Handling the event lifecycle and errors by using code (for example, Lambda
Destinations, dead-letter queues)
• Writing and running test code by using AWS services and tools
• Integrating Lambda functions with AWS services
• Tuning Lambda functions for optimal performance
#### Task Statement 3: Use data stores in application development.
Knowledge of:
• Relational and non-relational databases
• Create, read, update, and delete (CRUD) operations
• High-cardinality partition keys for balanced partition access
• Cloud storage options (for example, file, object, databases)
• Database consistency models (for example, strongly consistent, eventually
consistent)
• Differences between query and scan operations
• Amazon DynamoDB keys and indexing
• Caching strategies (for example, write-through, read-through, lazy loading,
TTL)
• Amazon S3 tiers and lifecycle management
• Differences between ephemeral and persistent data storage patterns
Skills in:
• Serializing and deserializing data to provide persistence to a data store
• Using, managing, and maintaining data stores
• Managing data lifecycles
• Using data caching services
### Domain 2: Security
#### Task Statement 1: Implement authentication and/or authorization for applications and AWS services.
Knowledge of:
• Identity federation (for example, Security Assertion Markup Language
[SAML], OpenID Connect [OIDC], Amazon Cognito)
• Bearer tokens (for example, JSON Web Token [JWT], OAuth, AWS Security
Token Service [AWS STS])
• The comparison of user pools and identity pools in Amazon Cognito
• Resource-based policies, service policies, and principal policies
• Role-based access control (RBAC)
• Application authorization that uses ACLs
• The principle of least privilege
• Differences between AWS managed policies and customer-managed
policies
• Identity and access management
Skills in:
• Using an identity provider to implement federated access (for example,
Amazon Cognito, AWS Identity and Access Management [IAM])
• Securing applications by using bearer tokens
• Configuring programmatic access to AWS
• Making authenticated calls to AWS services
• Assuming an IAM role
• Defining permissions for principals
#### Task Statement 2: Implement encryption by using AWS services.
Knowledge of:
• Encryption at rest and in transit
• Certificate management (for example, AWS Private Certificate Authority)
• Key protection (for example, key rotation)
• Differences between client-side encryption and server-side encryption
• Differences between AWS managed and customer managed AWS Key
Management Service (AWS KMS) keys

Skills in:
• Using encryption keys to encrypt or decrypt data
• Generating certificates and SSH keys for development purposes
• Using encryption across account boundaries
• Enabling and disabling key rotation
#### Task Statement 3: Manage sensitive data in application code.
Knowledge of:
• Data classification (for example, personally identifiable information [PII],
protected health information [PHI])
• Environment variables
• Secrets management (for example, AWS Secrets Manager, AWS Systems
Manager Parameter Store)
• Secure credential handling
Skills in:
• Encrypting environment variables that contain sensitive data
• Using secret management services to secure sensitive data
• Sanitizing sensitive data
### Domain 3: Deployment
#### Task Statement 1: Prepare application artifacts to be deployed to AWS.
Knowledge of:
• Ways to access application configuration data (for example, AWS
AppConfig, Secrets Manager, Parameter Store)
• Lambda deployment packaging, layers, and configuration options
• Git-based version control tools (for example, Git, AWS CodeCommit)
• Container images
Skills in:
• Managing the dependencies of the code module (for example, environment
variables, configuration files, container images) within the package
• Organizing files and a directory structure for application deployment
• Using code repositories in deployment environments
• Applying application requirements for resources (for example, memory,
cores)

#### Task Statement 2: Test applications in development environments.
Knowledge of:
• Features in AWS services that perform application deployment
• Integration testing that uses mock endpoints
• Lambda versions and aliases
Skills in:
• Testing deployed code by using AWS services and tools
• Performing mock integration for APIs and resolving integration
dependencies
• Testing applications by using development endpoints (for example,
configuring stages in Amazon API Gateway)
• Deploying application stack updates to existing environments (for example,
deploying an AWS SAM template to a different staging environment)
#### Task Statement 3: Automate deployment testing.
Knowledge of:
• API Gateway stages
• Branches and actions in the continuous integration and continuous delivery
(CI/CD) workflow
• Automated software testing (for example, unit testing, mock testing)
Skills in:
• Creating application test events (for example, JSON payloads for testing
Lambda, API Gateway, AWS SAM resources)
• Deploying API resources to various environments
• Creating application environments that use approved versions for
integration testing (for example, Lambda aliases, container image tags,
AWS Amplify branches, AWS Copilot environments)
• Implementing and deploying infrastructure as code (IaC) templates (for
example, AWS SAM templates, AWS CloudFormation templates)
• Managing environments in individual AWS services (for example,
differentiating between development, test, and production in API Gateway)

#### Task Statement 4: Deploy code by using AWS CI/CD services.
Knowledge of:
• Git-based version control tools (for example, Git, AWS CodeCommit)
• Manual and automated approvals in AWS CodePipeline
• Access application configurations from AWS AppConfig and Secrets
Manager
• CI/CD workflows that use AWS services
• Application deployment that uses AWS services and tools (for example,
CloudFormation, AWS Cloud Development Kit [AWS CDK], AWS SAM, AWS
CodeArtifact, AWS Copilot, Amplify, Lambda)
• Lambda deployment packaging options
• API Gateway stages and custom domains
• Deployment strategies (for example, canary, blue/green, rolling)
Skills in:
• Updating existing IaC templates (for example, AWS SAM templates,
CloudFormation templates)
• Managing application environments by using AWS services
• Deploying an application version by using deployment strategies
• Committing code to a repository to invoke build, test, and deployment
actions
• Using orchestrated workflows to deploy code to different environments
• Performing application rollbacks by using existing deployment strategies
• Using labels and branches for version and release management
• Using existing runtime configurations to create dynamic deployments (for
example, using staging variables from API Gateway in Lambda functions)

### Domain 4: Troubleshooting and Optimization
#### Task Statement 1: Assist in a root cause analysis.
Knowledge of:
• Logging and monitoring systems
• Languages for log queries (for example, Amazon CloudWatch Logs Insights)
• Data visualizations
• Code analysis tools
• Common HTTP error codes
• Common exceptions generated by SDKs
• Service maps in AWS X-Ray
Skills in:
• Debugging code to identify defects
• Interpreting application metrics, logs, and traces
• Querying logs to find relevant data
• Implementing custom metrics (for example, CloudWatch embedded metric
format [EMF])
• Reviewing application health by using dashboards and insights
• Troubleshooting deployment failures by using service output logs
#### Task Statement 2: Instrument code for observability.
Knowledge of:
• Distributed tracing
• Differences between logging, monitoring, and observability
• Structured logging
• Application metrics (for example, custom, embedded, built-in)
Skills in:
• Implementing an effective logging strategy to record application behavior
and state
• Implementing code that emits custom metrics
• Adding annotations for tracing services
• Implementing notification alerts for specific actions (for example,
notifications about quota limits or deployment completions)
• Implementing tracing by using AWS services and tools

#### Task Statement 3: Optimize applications by using AWS services and features.
Knowledge of:
• Caching
• Concurrency
• Messaging services (for example, Amazon Simple Queue Service [Amazon
SQS], Amazon Simple Notification Service [Amazon SNS])
Skills in:
• Profiling application performance
• Determining minimum memory and compute power for an application
• Using subscription filter policies to optimize messaging
• Caching content based on request headers

### In-scope AWS services and features
The following list contains AWS services and features that are in scope for the exam.
This list is non-exhaustive and is subject to change. AWS offerings appear in
categories that align with the offerings primary functions:

#### Analytics:
• Amazon Athena
    - query S3 using SQL queries, analyze JSON, CSV, Parquet, others 
• Amazon Kinesis
    - real time data output from infrastucture
    - visualize in other service like ApacheSpark
• Amazon OpenSearch Service

#### Application Integration:
• AWS AppSync
• Amazon EventBridge
• Amazon Simple Notification Service (Amazon SNS)
    - send push notifications to your users
• Amazon Simple Queue Service (Amazon SQS)
• AWS Step Functions

#### Compute:
• Amazon EC2
    - Elastic Compute Cloud
    - virtual cloud computer w/ OS memory etch
    - can use instace as server for webapp
    - might need to distribute load across instances -> (ELB)
• AWS Elastic Beanstalk
    - layer that sits on top of EC2 + other autoscaling features
    - to deploy web app, chose a template and go
    - Platform aaS - scaling is automatic
• AWS Lambda
    - serverless, no presistant state needed
    - Functions aas 
    - upload code, chose event to trigger code
    - traffic scaling networking all in background
    - only pay for exact number of actions that happen

• AWS Serverless Application Model (AWS SAM)
    - simplify the development and deployment of serverless applications on AWS
    - shorthand syntax to define functions, APIs, databases, and event source mappings
    - model applications using YAML or JSON config files, transformed into AWS CloudFormation syntax on deploy
    - built on top of CloudFormation
    - abstract, short-hand syntax, define infrastructure with fewer lines of code, less errors
    - AWS SAM CLI to build, test, and debug their serverless applications locally

#### Containers:
• AWS Copilot
• Amazon Elastic Container Registry (Amazon ECR)
    - upload your apps docker image
• Amazon Elastic Container Service (Amazon ECS)
    - pulls your apps docker image down and runs it
    - starting stopping allocating vMS to run containers
    - connecting vms to other things like loadbalancers
• Amazon Elastic Kubernetes Service (Amazon EKS)
    - more control over scalability
    - 

#### Database:
• Amazon Aurora
    - Propriatary amazon SQL flavor
    - Compatible with portgres and mysql
    - Better perfomace and lower cost than other options
• Amazon DynamoDB
    - Doc based noSQL db
    - scales horizonatlly easy
    - fast and cheap
    - no joins
    - limited queries
• Amazon ElastiCache
    - fully managed version of Redis
    - ultra fast memory

• Amazon MemoryDB for Redis
• Amazon RDS
    - relational DB 
    - supports many SQL DB flavors
    - backups, patching, sacleing


#### Developer Tools:
• AWS Amplify
    - sdks to connect to android from js frameworks
• AWS Cloud9
• AWS CloudShell
• AWS CodeArtifact
• AWS CodeBuild
• AWS CodeCommit
    - hosts secure, private Git repositories
• AWS CodeDeploy
    - deployment service that automates software deployments to Amazon EC2, AWS Fargate, AWS Lambda, and on-premises.
• Amazon CodeGuru
• AWS CodePipeline
• AWS CodeStar
• Amazon CodeWhisperer
• AWS X-Ray

#### Management and Governance:
• AWS AppConfig
• AWS CLI
• AWS Cloud Development Kit (AWS CDK)
• AWS CloudFormation
    - yaml json infrastucture templates 
    - [helper scripts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html)
• AWS CloudTrail
• Amazon CloudWatch
    - collects logs / metrics from ec2 instances
• Amazon CloudWatch Logs
    - a feature of cloudwatch, lets you look at logs 
• AWS Systems Manager
    - unified user interface, allowing you to automate and manage operational tasks across your AWS resources.
    - Parameter Store: Securely store configuration data and secrets, such as db connection strings, in a centralized, scalable storage.
    - Run Command: Remotely and securely execute commands on EC2 instances and other managed resources, making it easier to perform operational tasks at scale
    - Automation: Create and execute workflows that automate manual and repeatable tasks
    - Session Manager: Securely connect to instances without the need for opening inbound ports or managing SSH keys, simplifying access management.

#### Networking and Content Delivery:
• Amazon API Gateway
• Amazon CloudFront
    - CDN that accelerates delivery web content (images, videos APIs) to end-users by caching content at edge locations closest to them, reducing latency and improving overall website performance.
• Elastic Load Balancing (ELB)
    - distributes traffic evenly across EC2 instances automatically
    - pass data to auto scaling
    - define policies that will spin up / down new ec2 instances as needed
    - 2 types of load balancers : Classic and Application Load balancer
    - ALB has 3 sub types Application, network, Gateway
    - classic has less features, operates at layers 4, 7 transport, application
    - ALB operates only layer 7 application
    - ALB content-based routing, WebSocket and HTTP/2 protocols, host-based + path-based routing, integration with ECS (Elastic Container Service) and EKS (Elastic Kubernetes Service).
• Amazon Route 53
• Amazon VPC

#### Security, Identity, and Compliance:
• AWS Certificate Manager (ACM)
• Amazon Cognito
    - manages logins for your webapp
    - manages user sessions
• AWS Identity and Access Management (IAM)
    - create rolse, grant / restrict access to aws account
• AWS Key Management Service (AWS KMS)
• AWS Private Certificate Authority
• AWS Secrets Manager
• AWS Security Token Service (AWS STS)
• AWS WAF

#### Storage:
• Amazon Elastic Block Store (Amazon EBS)
    - very fast file storage
    - high throughput
    - more manual config required
• Amazon Elastic File System (Amazon EFS)
    - higher cost high perfomance file storeage
    - less management and config required than EBS   
    - less performant to workloads that require random access over large files
    - better for distributeing highly parallelized workloads ie analytical / media processing across several machines
### 
• Amazon S3
    - first thing aws offerd
    - stores any file or obj
    - great for general purpose file storage
• Amazon S3 Glacier
    - lower cost higher latency file storage
    - for files less frequently accessed than S3

### AWS setup

install AWS CLI
AWS website -> Security Config -> create access key
aws configure
paste creds in

### [Start the vid](https://www.youtube.com/watch?v=bhomsGI56Ok)

#### EC2 structure

##### Instance

self contained virtual compute unit
each instance needs software to run
avaliable as Amazon Machine Image - AMI
    can be an OS or some other software ie Node.js
    can create your own or use one from AWS marketplace
seperation between exceution env and file system
3 options for file systems
1. Instance Store Volume
    hard drive physically connected to EC2 instance
    non transferable between EC2 instances
2. Elastic block storeage EBS
    connecable to multiple instances
    can live on past life of EC2 instance
    non scalable
3. Elastic File System EFS
    similar to EBS 
    Scaleable in size

##### Launch an AMI

2 options
1. Instance volume backed AMI
    cannot be stopped
    can only be terminated or restarted
    slower to boot
    data transfered from s3 on boot
2. EBS backed AMI
    can be stopped for a arbitrary lenght of time
    instance data persists on EBS
    faster to boot
    data sored in EBS

##### AMI visibility

who has permission to use it
1. public
    anyone can use it
2. explicit
    whitelist
3. implicit
    private

AMIS are region specific
need to grab the AMI id for your specific region

##### EC2 Instance Classes

defines conditions of instance life and how its paid for
1. Spot instances
    bid for computing resources
    uses spare unused EC2 capacity
    biggerst discounts
    poor availiability
2. On-demand Instances
    pay for what you use
    no commitment
    easy to delete anc create
    good scalability
3. Reserved Instances
    commitment for a period of time
    1 - 3 years
    big discounts
    good for enterprise applications

#### AWS REST API

each request must be signed with credentials
AWS SDK is code interface to REST API
in SDK signing the requests is done for you

#### Create EC2 Instance

needed to run application in AWS
can be done in AWS Consle or CLI
we will be using AWS SDK with code
need to also make security group and keypair

##### Set ENV

in .env in root of project
AWS_REGION=us-west-2
creating ec2 instance
hbfl/scripts/03/create-ec2-instance.js

##### AWS SDK

version 2 != version 3

in V2
const AWS = require('aws-sdk')
improt entire sdk every time

in V3
const{
    EC2CLient,
    DescribeImagesCommand
} = require('@aws-sdk/client-ec2')
much more modular
only impor the consturctor functions
1 client and several commands

#### Create EC2 instance w/ AWS SDK

1. import
const {
    EC2CLient,
    DescribeImagesCommand
} = require('@aws-sdk/client-ec2')

2. instantiate client
const client = new EC2Client(options)
3. instantiate command
const command = new DescribeImagesCommand(input)
4. use client to send command to AWS
client.send(command)

code in AWS-tools/create-ec2-instance.js

need to specify which AMI to use for our EC@ intance
There are a milllion
best way to search is through aws amangement console website
aws.com -> EC2 dashboard -> launch instance -> Application and OS Images (Amazon Machine Image) -> Browse More AMIs -> copy the AMazon Linux x86 id
looks like: ami-0c20d88b0021158c6

AWS-tools/create-ec2-instance.js n 0assumes i have a default VPC configured
in EC2 dashboard default VPC id should be displayed
Account attributes
Default VPC 
vpc-031aaff6af02c87eb

also default subnets must auto assign public IPV4 addresses to instances 
hb  
in hblf repo
npm install

node --env-file=.env scripts/03/create-ec2-instance.js

node --env-file=.env scripts/03/manage-ec2-instance.js

#### Launching an EC2 instance from AWS marketplace

EC2 dahsboard -> Launch instance -> Browse AMIs -> AWS marketplace tab -> Bitnami Node AMI -> Subscribe -> get ami_id

ami-09212cdf02ea4b121
paste into create instance file
get user data from marketplace-ec2-startup

AMIs help to easily reproduce EC2s instances with your app on them

