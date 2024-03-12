


#### practice test review

### Lambda funcrtion throttleing - what to do?
problem : current concurrency execution count > concurrency limit
#### do
- exponential backoff : error handling strategy for each repeated request from Client, increace delay between responses - can be used for 429 responses
- throttled invocation requests in Lambda : happens When the number of concurrent executions exceeds the set limits Lambda starts throttling new invocation requests. Throttled invocations receive a 429 error response (Too Many Requests)
- Configuring  Concurrencty: the number of in-flight requests that your function is currently handling
    - Reserved concurrency – the maximum number of concurrent instances allocated to your function. When a function has reserved concurrency, no other function can use that concurrency. incurs no additional charges.
    - Provisioned concurrency – pre-initialized execution environments allocated. These execution environments are ready to respond immediately to incoming function requests. incurs additional charges to your AWS account

#### dont do
Use a compiled language like GoLang to improve the function’s performance is incorrect because no matter what language you use, the Lambda function will still throw a throttling error if the current concurrency execution count is greater than your concurrency limit.

### Many Lambda functions calling each other
problem : hard to manage - what to do
difficult to manage the coordination and dependencies between them, leading to errors, duplication of code, and difficulty debugging and troubleshooting issues.

#### do
Create an AWS Step Functions state machine and convert each Lambda function into individual Task states.
#### dont
Use AWS CodePipeline to define the source, build, and deployment stages for each Lambda function.
Create an AWS AppSync GraphQL API endpoint and configure each Lambda function as a resolver.
Use AWS AppConfig’s feature flag to gradually release new code changes to each Lambda function.
#### info
- AWS Step Functions state machine : JSON describing a state machine
- AWS CodePipeline: CI/CD
- AWS AppSync: Connect apps to data and events with secure, serverless, and performant GraphQL and Pub/Sub APIs, Access data from multiple sources with a single request.
- AWS AppConfig: decouples your feature releases from code deployments. create new features and push the code to production with new feature hidden behind a feature flag. toggle feature flag to turn it on, limited to internal testers, beta users, and then all users.

### storing classified files with AWS KMS
Which of the following is the MOST suitable procedure for encrypting data
#### do
- Generate a data key using a symmetric key. Then, encrypt data with the data key.
#### dont
- Use a symmetric key for encryption and decryption.
- Generate a data key using a KMS key. Then, encrypt data with the ciphertext version of the data key.
- Use a combination of symmetric and asymmetric encryption. Encrypt the data with a symmetric key and use the asymmetric private key to decrypt the data.
#### info
- KMS : stores and protects your encryption keys to make them highly available
    - KMS keys can only encrypt data up to 4kb in size
- Hybrid encryption : sym + asym enc - Anyone can encrypt data using the public key, but only users with the private key can decrypt the data
    - the keys on each encryption algorithm are not related. You cannot encrypt data with a symmetric key and expect it to be decrypted by an asymmetric private key
- Ciphertext : A cipher is an algorithm that transforms an input (plaintext) into an output (ciphertext) with a secret key.
    - ciphertext version of a key cannot be used for encryption
- **[Envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)** : the practice of encrypting plaintext data with a data key and then encrypting the data key under another key. Master key generates, encrypts, decrypts the data key that encrypts the sensitive info
    - safe to store encrypted data key next to the encrypted data
    - instead of re encrypting data you can just reencrypt key, much faster

### transcoding media servicein AWS
Photos uploaded to S3 trigger [Step Functions](https://aws.amazon.com/step-functions/), a series of processes that will perform image analysis. The final output should contain the input plus the result of the final state to conform to the application’s logic flow.
What should the developer do?

#### do
Declare a ResultPath field filter on the Amazon States Language specification.

#### dont
Declare an InputPath field filter on the Amazon States Language specification.

Declare an OutputPath field filter on the Amazon States Language specification.

Declare a Parameters field filter on the Amazon States Language specification.

#### info
- [I/O in Step Funcs](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html) : 
    - input starts as JSON , JSON passed between steps
- [Amazon States Language specification](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) : JSON-based, structured language used to define your state machine, a collection of states, that can do work (Task states), determine which states to transition to next (Choice states), stop an execution with an error (Fail states), and so on.
- [Common State Fields](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-common-fields.html):
    - Type (Required): The state's type.
    - Next : The name of the next state that is run when the current state finishes. Some state types, such as Choice, allow multiple transition states. Not needed when last state in your workflow, or a terminal state, such as Succeed or Fail.
    - End : terminal state (ends the execution) if set to true. can be many terminal states per state machine. mutually exclusive with Next in a state. Some state types don't support or use the End field.
    - InputPath (Optional) : selects a portion of state's input to be passed to the state's task. If omitted, has the value $ = entire input.
    - OutputPath (Optional) : selects a portion of state's output to be passed to next state. If omitted, has the value $ = entire input.
    - Paramaters : enables you to pass a collection of key-value pairs, static values predefined or selected from the input
    - ResultSelector : manipulates the state’s result before ResultPath is applied
    - ResultPath : controls if output of state is a copy of its input, the result it produces or a combination of its input and result. 

### multiple Lambda Functions and a DynamoDB table
The application must be deployed by calling the CloudFormation APIs using AWS CLI. The CloudFormation template and the files containing the code for all the Lambda functions are located on a local computer.
What should the Developer do to deploy the application?
#### do
Use the aws cloudformation package command and deploy using aws cloudformation deploy.
#### dont
Use the aws cloudformation validate-template command and deploy using aws cloudformation deploy.
Use the aws cloudformation deploy command.
Use the aws cloudformation update-stack command and deploy using aws cloudformation deploy.

### info
 - CloudFormation : model and manage infrastructure resources in JSON or yaml
 - [CloudFormation CLI](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/) : prepend commands with 'aws cloudformation'
    - validate-template : checks if the template is valid JSON or YAML. if not return template validation error.
    - deploy : Deploys specified AWS CloudFormation template by creating and executing a change set. terminates after executeing the change set
    - update-stack : Updates stack as specified in the template. After the call completes successfully, the stack update starts.
    - package : Packages local artifacts (paths) referenced in template. uploads local artifacts(Lambda source code, Swagger file for AWS API Gateway REST API) to an S3 bucket. returns a copy of your template, replacing references to local artifacts with S3 location where the command uploaded them.
        - quickly upload local artifacts required by your template. After you package, run the deploy command to deploy the returned template.

### Lambda function GetItem ProvisionedThroughputExceededException  
A code that runs on a Lambda function performs a GetItem call from a DynamoDB table. The function runs three times every week. You noticed that the application kept receiving a ProvisionedThroughputExceededException error for 10 seconds most of the time.

How should you handle this error?
#### do
Reduce the frequency of requests using error retries and exponential backoff.
#### dont
Create a Local Secondary Index (LSI) to the existing DynamoDB table to increase the provisioned throughput.
Refactor the code in the Lambda function to optimize its performance.
Enable DynamoDB Accelerator (DAX) to reduce response times from milliseconds to microseconds.

#### info
 - [Local Secondary Index (LSI)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html) : a second type of primary key that can be used to avoid scanning or sorting large amounts of data. second key is a sortable singular scalar attribute in a seperate table as the table it shares a primary key with
 - ProvisionedThroughputExceededException 4xx
 : AWS SDKs for DynamoDB automatically retry requests that receive this exception. request is eventually successful, unless retry queue is too large to finish. Reduce request frequency via Error retries and exponential backoff.
 - DynamoDB Accelerator (DAX) : caching service built for Amazon DynamoDB

### IAM get EC2 
An IAM user wants to get information about specific EC2 instances on the us-east-1 region. the user was compelled to use the describe-instances operation using AWS CLI. He wants to check whether he has the required permission to initiate the command without actually making the request.

Which of the following actions should be done to solve the problem?
#### do
Add the --dry-run parameter to the describe-instances command.
#### dont
Add the --max-items parameter to the describe-instances command.
Add the --filters parameter to the describe-instances command.
Add the --dry-run parameter to the describe-instances command.
Add the --generate-cli-skeleton parameter to the describe-instances command.
#### info
CLI commands prepend with aws:
 - [describe-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html) : Describes the specified instances or all instances use pagination to ensure that the operation returns qucikly
 - --max-items : The total number of items to return in the command’s output
 - --filters : filters based on hudge list of attributes
 - --generate-cli-skeleton :  Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value input, prints a sample input JSON that can be used as an argument for --cli-input-json
 - --dry-run : Checks whether you have the required permissions without actually making the request, returns error response. If you have req permission, error response is DryRunOperation . Otherwise, UnauthorizedOperation

### decrease latency retrieving data from RDS MySQL DB
A developer is looking for a way to decrease the latency in retrieving data from an Amazon RDS MySQL database. He wants to implement a caching solution that supports Multi-AZ replication with sub-millisecond response times.

What must the developer do that requires the LEAST amount of effort?

#### do
Set up an Elasticache for Redis cluster between the application and database. Configure it to run with replication to achieve high availability.
#### dont

Set up an Elasticache for Memcached cluster between the application and database. Configure it to run with replication to achieve high availability.
Convert the database schema using the AWS Schema Conversion Tool and move the data to DynamoDB. Enable Amazon DynamoDB Accelerator (DAX).
Set up AWS Global Accelerator and integrate it with your application to improve overall performance.

#### info
 - Elasticahce : in-memory data store and cache service by Amazon Web Services. wraps either memcached or redis
 - Memcached : multi threaded, no replication, snapshots, transactions, or disk persistance
 - [Redis](https://aws.amazon.com/elasticache/redis-vs-memcached/) : single threadeded, replication, snapshots, transactions, disk persistance
 - replication : allows replica Redis instances to be exact copies of master instances. needed for Multi-AZ redundancy
 - Multi-AZ redundancy : consists of a DB instance plus a single standby DB instance in a separate Availability Zone
 - AWS Global Accelerator : route traffic to your applications using the AWS global network instead of the internet. helps you improve availability, performance



### Node.js mobile game tournament  AWS Elastic Beanstalk
A full-stack developer has developed an application written in Node.js. The developer deploys the application using AWS Elastic Beanstalk.

Which of the following services can the developer configure with Elastic Beanstalk? (Select THREE.)
#### do
Amazon CloudWatch
Application Load Balancer
Amazon EC2 Instance
#### dont
Amazon Athena 
Amazon CloudFront
AWS Lambda
#### info
 - Amazon Athena : query S3 using SQL queries, analyze JSON, CSV, Parquet, others 
 - Amazon CloudFront : CDN that accelerates delivery web content (images, videos APIs) to end-users by caching content at edge locations closest to them, reducing latency and improving overall website performance.
 <!-- wrong i guess - Amazon EC2 : will not need configuration when using Elastic Beanstalk, some ec2 configs can be changed thru EB, not common -->
 - Application Load Balancer ALB : distributes incoming application traffic across multiple targets, EC2 instances, in a single or multiple availability zones. operates atapplication layer of the OSI model, enabling features like content-based routing, SSL termination, and support for WebSocket and HTTP/2 protocols, scalable and efficient solution for deploying and managing applications with high availability.

With ElasticBeanstalk, you can:
– Select the operating system that matches your application requirements (e.g., Amazon Linux or Windows Server 2016)
– Choose from several Amazon EC2 instances, including On-Demand, Reserved Instances, and Spot Instances.
– Choose from several available database and storage options.
– Enable login access to Amazon EC2 instances for immediate and direct troubleshooting
– Quickly improve application reliability by running in more than one Availability Zone.
– Enhance application security by enabling HTTPS protocol on the load balancer
– Access built-in Amazon CloudWatch monitoring and getting notifications on application health and other important events
– Adjust application server settings (e.g., JVM settings) and pass environment variables
– Run other application components, such as a memory caching service, side-by-side in Amazon EC2.
– Access log files without logging in to the application servers
Hence, the correct answers are: Amazon EC2 Instance, Amazon CloudWatch, and Application Load Balancer.
You cannot configure Amazon Athena, AWS Lambda, and Amazon CloudFront on ElasticBeanstalk.



### URI ne
A developer is writing software that will run in EC2. The script needs to access the local IP address from the instance to manage a connection to an application outside the AWS Cloud. The developer found out that the details about an instance can be viewed by visiting a certain Uniform Resource Identifier (URI).

Which of the following is the correct URI?
#### do
http://169.254.169.254/latest/meta-data/
#### dont
http://254.169.254.169/latest/meta-data/
http://254.169.254.169/latest/user-data/
http://169.254.169.254/latest/user-data/
#### info
to do:
from ec2 instance
'curl http://169.254.169.254/latest/meta-data/'
254 is the correct local IP
[get ec2 metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#instancedata-meta-data-retrieval-examples)


### fuck your password
A company wants to centrally organize login credentials for its application. The application prompts users to change passwords every 35 days. Expired login credentials must be removed automatically, and an email notification should be sent to the users when their passwords are about to expire. A developer must create a solution with the least amount of development effort.

Which solution meets the requirements?

#### do
Store the credentials as Advanced Parameters in AWS Systems Manager (SSM) Parameter Store and configure Expiration and ExpirationNotification policies. Create an Amazon EventBridge rule that sends Amazon SNS email notifications. advnaced parammeters are not neccessary only lets you store greater numbers of parameters

#### dont
Use AWS Secrets Manager to store user credentials. Create a Lambda function that runs periodically to send Amazon SNS email notifications for passwords nearing expiration
Use AWS Secret Managers to store user credentials and turn on automatic rotation.
Store the credentials as Standard Parameters in AWS Systems Manager (SSM) Parameter Store and configure Expiration and ExpirationNotification policies. Create an Amazon EventBridge rule that sends Amazon SNS email notifications. - do not support Expiration and ExpirationNotification policies.
#### info
 - AWS Systems Manager (SSM) : automate and manage operational tasks across AWS 
 - SSM Parameter Store : securely stores, manages configuration data, secrets, parameters for applications
 - Standard Parameters : a versioned key value pair
    - db connection strings, API keys, or any other application-specific configuration values
 - Advanced Parameters : supports Expiration and ExpirationNotification policies.
 - Amazon EventBridge : serverless event bus service, simplifies development of event-driven applications by allowing different AWS services, integrated SaaS applications, and custom sources to communicate with each other through events. 
 - [Parameter Policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html)



# Section Based Qiestions
## Deployment

### Node.js Lambda function
Your manager instructed you to share your technical expertise to the whole software development department of your company. You are planning to deploy a simple Node.js ‘Hello World’ Lambda function to AWS using CloudFormation.

Which of the following is the EASIEST way of deploying the function to AWS?

#### do
Include your function source inline in the ZipFile parameter of the AWS::Lambda::Function resource in the CloudFormation template.
#### dont
Include your function source inline in the Code parameter of the AWS::Lambda::Function resource in the CloudFormation template. - needs to be in ZipFile parameter under the Code parameter
Upload the code in S3 as a ZIP file then specify the S3 path in the ZipFile parameter of the AWS::Lambda::Function resource in the CloudFormation template. - should be AWS::Lambda::Function::"Code": {"S3Bucket": "lambda-functions", "S3Key": "amilookup.zip"},

Upload the code in S3 then specify the S3Key and S3Bucket parameters under the AWS::Lambda::Function resource in the CloudFormation template.

#### info
 - CloudFormation : model and manage infrastructure resources in JSON or yaml
 - [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html): creates a Lambda function, needs  deployment package and an execution role
    - deployment package : .zip file archive or container image that contains your function code
    - execution role : grants the function permission to use AWS services
    - Code : holds a child element [ImageUri, S3Bucket, S3Key, ZipFile] which points to the code
    - ZipFile : (Node.js and Python) The source code of your Lambda function. If you include your function source inline with this parameter, AWS CloudFormation places it in a file named index and zips it to create a deployment package. This zip file cannot exceed 4MB. 

### 

A developer is building an online game in AWS which will be using a NoSQL database with DynamoDB. Each player data has an average size of 3.5 KB and it is expected that the game will send 150 eventually consistent read requests per second.

How may Read Capacity Units (RCU) should the developer provision to the table?

#### do
75
[to calc](https://tutorialsdojo.com/calculating-the-required-read-and-write-capacity-unit-for-your-dynamodb-table/)
Step #1 Get the Average Item Size by rounding up to 4 KB
= 3.5 KB = 4 KB (rounded up)

Step #2 Get the RCU per Item by dividing the Average Item Size by 8 KB
= 4 KB / 8 KB
= 0.5 

Step #3 Multiply the RCU per item to the number of items to be written per second
= 150 x 0.5 
= 75 eventually consistent read requests

#### dont
300
150
600
#### info
 - [DynamoDB read/write capacity units](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html) : read requests can be either strongly consistent, eventually consistent, or transactional.
    - strongly consistent : item up to 4 KB requires one read request unit
    - eventually consistent : item up to 4 KB requires one-half read request unit
    - transactional : item up to 4 KB requires two read request units.
    - 6KB : read units x2 15KB x4 etc
 - Read/Write Capacity Units RCU/WCU : the way amazon adds up how much money you owe them per transaction
    - provisioning 100 RCU gives you 100 RCUs per second

### Elastic Beanstalk microservice container definitions
A developer plans to use AWS Elastic Beanstalk to deploy a microservice application. The application will be implemented in a multi-container Docker environment.

How should the developer configure the container definitions in the environment?

#### do
Configure the container definitions in the Dockerrun.aws.json file.
#### dont
Use the eb config command to configure the container definitions.
Configure the container definitions in the Dockerrun.aws.json.config and put it inside the .ebextensions folder.
Configure the container definitions in the Amazon ECS Console when building the Docker environment. - must be deployed using elastic beanstalk
#### info
 - Dockerrun.aws.json file : describes how Elastic Beanstalk should run Docker containers for your application. info about the Docker images, container definitions, other settings needed for Elastic Beanstalk to deploy/manage app
 - CLI eb config command  : interact with and modify the configuration settings for your Elastic Beanstalk application or environment
    - aws eb config get <environment-name> : Updates the saved configuration for an environment.
    - aws eb config put <environment-name> : Saves the current configuration of an environment to a file.
    - aws eb config save <environment-name> : Lists the saved configurations for an environment.
    - aws eb config list <environment-name> : Lists saved configurations foe an environment.
    - aws eb config delete <configuration-name> : Deletes a saved configuration from an environment.
 - .ebextensions folder : forlder in root holding extra config files for advanced configuration

### Lambda function deploy
A Lambda function has been integrated with DynamoDB Streams as its event source. There has been a new version of the function that needs to be deployed using CodeDeploy where the traffic must be shifted in two increments. It should shift 10 percent of the incoming traffic to the new version in the first increment and then the remaining 90 percent should be deployed five minutes later.

Which of the following deployment configurations is the MOST suitable to satisfy this requirement?
#### do
Canary
#### dont
All-at-once
Linear
Rolling with additional batch
#### info
 - CodeDeploy: deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services
    - In-place : instance in the deployment group is stopped, update installed, and the new version of the application is started and validated.
    - All-at-once : replace all EC2s with new version at same time, down time, risky
    - Canary : move small percentages of users to new version, make sure its good, move rest
    - Linear : move a constant number of userrs per hour to new verrsion
    - Rolling with additional batch : spin up new EC2 before tking down any old ones, roll through all EC2s never reducing capacity
        - only for Elastic Beanstalk not for Lambda


### Lambda, API Gateway, CloudFront, and DynamoDB using CloudFormation
You are deploying a serverless application composed of Lambda, API Gateway, CloudFront, and DynamoDB using CloudFormation. The AWS SAM syntax should be used to declare resources in your template which requires you to specify the version of the AWS Serverless Application Model (AWS SAM).

Which of the following sections is required, aside from the Resources section, that should be in your CloudFormation template?

Format Version
Parameters
Transform
Mappings

### locally build, test, and debug serverless applications
A developer is instructed to set up a new serverless architecture composed of AWS Lambda, API Gateway, and DynamoDB in a single stack. The new architecture should allow the developer to locally build, test, and debug serverless applications.

Which of the following should the developer use to satisfy the above requirement?
#### do
AWS Serverless Application Model (AWS SAM)
#### dont
AWS Elastic Beanstalk
AWS CloudFormation
AWS Systems Manager
#### info
 - AWS Serverless Application Model (AWS SAM) : Infrastructure as code IaC JSON 
    - simplify the development and deployment of serverless applications on AWS
    - shorthand syntax to define functions, APIs, databases, and event source mappings
    - forcused on severless application dev, local running, debugging, testing
 - AWS CloudFormation : similar to SAM, IaC JSON
    - more general purpose can use with more services, more verbose
    - no local running, debugging, testing
 - AWS Systems Manager : automate and manage operational tasks across AWS resources

### ECS Cluster task placement strategy 
A developer is building an application which will be hosted in an ECS Cluster. To minimize the number of instances in use, she must select a strategy which will place tasks based on the least available amount of CPU or memory.

Which of the following task placement strategy should the developer implement?
#### do
binpack
#### dont
random
distinctInstance
spread
#### info
 - ECS task placement strategies: rules that determine how tasks are placed on the instances within a cluster
 - random : chooses randomly from instances w/ enough resources, no logic required
 - distinctInstance : not a strategy rather a task placement constraint
    - Place each task on a different container instance
    - ensures isolation of tasks
 - binpack : use as few EC2 instances as possible
    - give task to instance w/ least CPU or RAM, saves money
 - spread : distriubte as widely and evenly as possible opposite of binpack
    - ensures availability, mitigates risk




### Deployment with quick rollback
An application is hosted in Elastic Beanstalk, which is currently running in Java 7 runtime environment. A new version of the application is ready to be deployed, and the developer was tasked to upgrade the platform to Java 8 to accommodate the changes. All user traffic must be immediately directed to the new version. If problems arise, the developer should be able to quickly revert to the previous version.

Which of the following is the MOST appropriate action that the developer should do to upgrade the platform?
#### do
Perform a Blue/Green Deployment.
#### dont
Perform a Traffic splitting deployment.
Manually upgrade the Java runtime environment of the EC2 instances in the Elastic Beanstalk environment.
Update the environment's platform version to Java 8.
#### info
 - Traffic splitting deployment : canary deployment in Elastic Beanstalk 
    - minimize risk of application failure
    - launches a full set of new instances and forwards a specified percentage of traffic to the new version. 
    - If new instances remain healthy, all traffic is gradually shifted, old instances terminated. 
    - If the new instances do not pass health checks or if the deployment is aborted, traffic is redirected back to old instances, new ones are terminated, ensuring no service interruption
 - Blue/Green Deployment : pretty similar
    - requires full maintainence of 2 environments
    - blue with old version
    - green with new
    - change from one to the onther via load balancer or DNS



### package is too large
A company is deploying the package of its Lambda function, which is compressed as a ZIP file, to AWS. However, they are getting an error in the deployment process because the package is too large. The manager instructed the developer to keep the deployment package small to make the development process much easier and more modularized. This should also help prevent errors that may occur when dependencies are installed and packaged with the function code.

Which of the following options is the MOST suitable solution that the developer should implement?
#### do
Upload the other dependencies of your function as a separate Lambda Layer instead.
#### dont
Upload the deployment package to S3.
Compress the deployment package as TAR file instead.
Zip the deployment package again to further compress the zip file.
#### info
 - S3 : doesnt change the size of the deployment package
 - separate Lambda Layer : reduces size of deployment package
 - TAR + double zip : wont reduce the package size considerably

### Elastic Beanstalk update without re-uploading the entire project
Several development teams worldwide will be collaboratively working on a project hosted on an AWS Elastic Beanstalk environment. The developers need to be able to deploy incremental code updates without re-uploading the entire project.

Which of the following actions will reduce the upload and deployment time with the LEAST amount of effort?
#### do
Create an AWS CodeCommit repository and allow access to all developers. Deploy the code to Elastic Beanstalk.
#### dont
Host the code repository on an EC2 instance and allow access to all the developers. Write a script that will automate the deployment process to Elastic Beanstalk.
Configure event notifications on a central S3 bucket and allow access to all developers. Invoke a Lambda Function that will deploy the code to Elastic Beanstalk when a PUT event occurs.
Upload the code to an Amazon EFS mounted on an EC2 instance. Write a script that will automate the deployment process to Elastic Beanstalk.
#### info
 - CodeCommit : hosts secure, private Git repositories
   - pull requests, reviews, comments, and merges
   - close to prod resources, quicker deployments
 - S3 : does not have the functionality to modify stored objects
 - EFS : file storage service for use with Amazon EC2
   - less performant to workloads that require random access over large files
   - better for distributeing highly parallelized workloads ie analytical / media processing across several machines

### CodePipeline CodeDeploy (CI/CD) pipelines in AWS
A company is heavily using a range of AWS services to host their enterprise applications. Currently, their deployment process still has a lot of manual steps which is why they plan to automate their software delivery process using continuous integration and delivery (CI/CD) pipelines in AWS. They will use CodePipeline to orchestrate each step of their release process and CodeDeploy for deploying applications to various compute platforms in AWS.
In this architecture, which of the following are valid considerations when using CodeDeploy? (Select TWO.)
#### do
AWS Lambda compute platform deployments cannot use an in-place deployment type.
CodeDeploy can deploy applications to both your EC2 instances as well as your on-premises servers.
#### dont
You have to install and use the CodeDeploy agent installed on your EC2 instances and ECS cluster.
The CodeDeploy agent communicates using HTTP over port 80.
CodeDeploy can deploy applications to EC2, AWS Lambda, and Amazon ECS only.
#### info
- in-place deployment type : not applicable to Lambda only EC2 instances
   - lambda uses canary all-at-once or linear
- CodeDeploy : can deploy EC2, Lambda, ECS and on-prem
   - agent communicates via https port 443
   - requires install and use of CodeDeploy agent on EC2 
   - not required for ECS cluster

### CloudFormation and SAM
An aerospace engineering company has recently migrated to AWS for their cloud architecture. They are using CloudFormation and AWS SAM as deployment services for both of their monolithic and serverless applications. There is a new requirement where you have to dynamically install packages, create files, and start services on your EC2 instances upon the deployment of the application stack using CloudFormation.

Which of the following [helper scripts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html) should you use in this scenario?

#### do
cfn-init
#### dont
cfn-hup
cfn-signal
cfn-get-metadata 
#### info
 - cfn-hup : check for updates to metadata and execute custom hooks when changes are detected
 - cfn-init : retrieve and interpret resource metadata, install packages, create files, start services
 - cfn-signal : signal a CreationPolicy or WaitCondition, allows synchronize other resources in the stack when the prerequisite resource or application is ready
 - cfn-get-metadata : retrieve metadata for a resource or path to a specific key.


### CloudFormation template that includes your SAM script
You are using AWS Serverless Application Model (AWS SAM) to build and deploy applications in your serverless infrastructure. Your manager instructed you to create a CloudFormation template that includes your SAM script and other service configurations. This template will be used to launch a similar infrastructure in another region.

What should you do in order to accomplish this task?
#### do
#### dont
Add a Transform section in the template to specify the version of the AWS Serverless Application Model (AWS SAM) to use.
Add a Resources section in the template to specify the version of the AWS Serverless Application Model (AWS SAM) to use.
Add a Parameters section in the template to specify the version of the AWS Serverless Application Model (AWS SAM) to use.
Add a Mappings section in the template to specify the version of the AWS Serverless Application Model (AWS SAM) to use.
#### info
 - CloudFormation :  JSON- or YAML-formatted text file that describes your AWS infrastructure
   - model and provision AWS resources in your cloud environment
 - CloudFormation sections : 
   - Description : text string that describes the template must always follow the template format version section
   - Metadata : Optional provides additional information about the template
   - Parameters : Defines values to pass to your template at runtime (when you create or update a stack). You can refer to parameters from the Resources and Outputs sections of the template.
   - Mappings: A mapping of keys and associated values that you can use to specify conditional parameter values. You can match a key to a corresponding value by using the Fn::FindInMap intrinsic function in the Resources and Outputs sections 
   - Conditions : Defines conditions that control whether certain resources are created or whether certain resource properties are assigned a value during stack creation or update
   - Transform : Optional specifies the version of AWS SAM to use
   - Resources : stack resources and their properties, such as an EC2 instance or an S3 bucket
   - Outputs : values that are returned whenever you view your stack's properties (aws cloudformation describe-stacks)
   - AWS::Serverless transform : a macro hosted by AWS CloudFormation, takes an entire template written in AWS SAM syntax and transforms and expands it into a compliant AWS CloudFormation template

### AppSpec file in CodeDeploy
A developer is preparing the application specification (AppSpec) file in CodeDeploy, which will be used to deploy her Lambda functions to AWS. In the deployment, she needs to configure CodeDeploy to run a task before the traffic is shifted to the deployed Lambda function version.

Which deployment lifecycle event should she configure in this scenario?

#### do
BeforeAllowTraffic
#### dont
BeforeInstall
Install
Start
#### info
 - AppSpec file in CodeDeploy : JSON-formatted file used to manage a deployment
   - defines lifecycle events, scripts that CodeDeploy should execute during deployment 
   - for EC2 + On-Prem AppSpec file must be named appspec.yml,in the root of the directory structure
   - sections : including version, os, files, permissions, hooks, and other
   - hooks : Lambda validation functions to run during a deployment lifecycle event
   - BeforeAllowTraffic : run tasks before traffic is shifted to the deployed Lambda function version.
   - AfterAllowTraffic : run tasks after all traffic is shifted to the deployed Lambda function version.
   - BeforeInstall : this event is only applicable for ECS, EC2 or On-Premises compute platforms and not for Lambda deployments.
   - Install : CodeDeploy agent copy the revision files from temp location to final destination folder of EC2 or On-Premises server. This deployment lifecycle event is not available for Lambda or ECS deployments.

 
### Elastic Beanstalk full capacity deploy
A single docker container environment is hosted in Elastic Beanstalk. Your manager instructed you to ensure that the compute resources maintain full capacity during deployments to avoid any degradation of the service or possible down time.

Which of the following deployment methods should you use to satisfy the given requirement? (Select TWO.)
#### do
Rolling with additional batch
Immutable
#### dont
All at once
Rolling
Canary
#### info
 - All at once : all instances simultaneously, downtime
 - Rolling with additional batch : 
 - Immutable : Deploy update to a fresh group of instances by performing an immutable update.
 - Rolling : deploy in batches. Each batch is taken down during deployment phase, reducing your environment’s capacity by the number of instances per batch
 - Canary : not readily available in Elastic Beanstalk, but primarily to Lambda.
 - Blue/Green : Deploy update to a separate environment, and then swap CNAMEs of the two environments to redirect traffic to the new version instantly.

### what types does CodeDeploy support?
The current application deployment process of a company is tedious and is prone to errors. They asked a developer to set up CodeDeploy as their deployment service, which can automate their application deployments on their hybrid cloud architecture.

Which of the following deployment types does CodeDeploy support? (Select TWO.)
#### do
In-place deployments to on-premises servers
Blue/green deployments to ECS.
#### dont
Blue/green deployments to on-premises servers.
Rolling deployments to ECS.
In-place deployments to AWS Lambda.
#### info
 - ECS : Blue/green
 - Lambda : Canary, Linear, All at once
 - EC2/On-Premises : Blue/green || In place for [All at once, Half at a time, One at a Time] 
   - only one that can do blue green and inplace on CodeDeploy


### update SAM
A development team is working on an AWS Serverless Application Model (SAM) application with its source code hosted on GitHub. A newly recruited developer clones the repository and observes that the SAM template contains references to AWS Lambda functions with CodeUri pointing to local file paths. The developer has added a new Lambda function and must redeploy the updated version to Production.

Which combination of steps must be taken to satisfy the requirement? (Select Two
#### do
Execute sam build to resolve dependencies and construct deployment artifacts for all functions and layers in the SAM template.
Use the sam deploy command to deploy the application with a specified CloudFormation stack.
#### dont
Execute sam publish to make the application available in the AWS Serverless Application Repository.

Run sam init to initialize a new SAM project.

Use the sam sync command to synchronize the local changes to the application in AWS.
#### info
 - sam publish : gives link to the AWS Serverless Application Repository directly to your application
 - sam deploy : packages your application, uploads it to an S3 bucket, and deploys it using CloudFormation
 - sam init : create a new SAM application with a sample AWS Lambda function
 - sam build : compile your application's source code and prepare it for deploymen
 - sam sync : watches your local application for changes and automatically syncs them to the AWS Cloud
 - sam local : local invocation and testing of your Lambda functions and SAM-based serverless applications by executing your code locally

### Lambda features
A Lambda function is over 80 MB in size, which exceeds the deployment package size limit for direct uploads. You want to refactor the function to pull in additional code and other dependencies from another source, which will reduce the size of the deployment.

Which feature of Lambda should you use in order to implement the above task? 

#### do
Layers
#### dont
Execution Context
Environment Variable
Alias
#### info

 - Layers :  distribution mechanism for libraries, custom runtimes, and other function dependencies
   - code sharing and separation of responsibilities so that you can manage your function's code and dependencies independently
 - Execution Context : runtime environment, the function's code, and any dependencies
 - Environment Variable : key-value pairs to customize the behavior of your function w/o changeing code
 - Alias : pointer to a specific Lambda function version
   - manage different stages of your application, such as development, testing, and production

### AWS::Lambda::Function resource
A developer is writing a CloudFormation template which will be used to deploy a simple Lambda function to AWS. The function to be deployed is made in Python with just 3 lines of codes which can be written inline in the template.

Which parameter of the AWS::Lambda::Function resource should the developer use to place the Python code in the template?

#### do
ZipFile
#### dont
Code
CodeUri
Handler

#### info

### zip upload and make template file for deployment
A development team has recently completed building their serverless application, and they are now ready to deploy it to AWS. They need to zip their code artifacts, upload them to Amazon S3, and produce the package template file for deployment.

Which command is the MOST suitable to use for automating the deployment steps?
#### do
sam deploy
#### dont
sam package
aws cloudformation deploy
sam publish
#### info
 - aws cloudformation : expects artifacts already packaged and uploaded to S3. It doesn’t handle the packaging process implicitly.
 - sam package : prepares the app for deployment by zipps artifacts, upload to S3, generates CloudFormation template w/ references to the uploaded artifacts in S3. It doesn’t deploy the application.
 - sam publish: publishes an AWS SAM application to the AWS Serverless Application Repository, does not generate the template file. It takes a packaged AWS SAM template and publishes the application to the specified region.
 - sam deploy : zips your code artifacts, uploads them to Amazon S3, and produces a packaged AWS SAM template file that it uses to deploy your application.


### AWS CLI new Lambda InvalidParameterValueException
You developed a shell script which uses AWS CLI to create a new Lambda function. However, you received an InvalidParameterValueException after running the script.

What is the MOST likely cause of this issue? 
#### do
You provided an IAM role in the CreateFunction API which AWS Lambda is unable to assume.
#### dont
The AWS Lambda service encountered an internal error.
You have exceeded your maximum total code size per account.
The resource already exists.
You provided an IAM role in the CreateFunction API which AWS Lambda is unable to assume.
#### info
 - resource already exists : the ResourceConflictException will be returned
 - AWS Lambda internal error : ServiceException
 - exceeded maximum code size : CodeStorageExceededException



### detach the root volume from the compromised EC2 instance
An EBS-backed EC2 instance has been recently reported to contain a malware that could spread to your other instances. To fix this security vulnerability, you will need to attach its root EBS volume to a new EC2 instance which hosts a security program that can scan viruses, worms, Trojan horses, or spyware.

What steps would you take to detach the root volume from the compromised EC2 instance?

#### do
Stop the instance then detach the volume.
#### dont
Detach the volume from the AWS Console. AWS takes care of unmounting the volume for you.
Unmount the volume, stop the instance, and then detach.
Unmount the volume from the OS and then detach.
#### info
 - root volume : must be stopped before it can be detached or unmounted


### managing CloudFormation template updates 
An application architect manages several AWS accounts for staging, testing, and production environments, which are used by several development teams. For application deployments, the developers use the similar base CloudFormation template for their applications.

Which of the following can allow the developer to effectively manage the updates on this template across all AWS accounts with minimal effort?
#### do
Update the stacks on multiple AWS accounts using CloudFormation StackSets.
#### dont
Create and manage stacks on multiple AWS accounts using CloudFormation Change Sets.
Upload the CloudFormation templates to CodeCommit and use a combination of CodeDeploy and CodePipeline to manage the deployment to multiple accounts.
Define and manage stack instances on multiple AWS Accounts using CloudFormation Stack Instances.
#### info
 - CloudFormation Change Sets : allow you to preview and manage changes to a stack before applying them
 - CloudFormation StackSets : create, update, or delete stacks across multiple accounts and regions with a single operation
 - CloudFormation Stack Instances : a single stack within a StackSet
 - CodeCommit : too much work use the thing they built for this use case 


## Security


### 
A company has different AWS accounts, namely Account A, Account B, and Account C, which are used for their Development, Test, and Production environments respectively. A developer needs access to perform an audit whenever a new version of the application has been deployed to the Test (Account B) and production (Account C) environments.

What is the MOST efficient way to provide the developer access to execute the specified task?
#### do
Grant the developer cross-account access to the resources of Accounts B and C.
#### dont
Set up AWS Organizations and attach a Service Control Policy to the developer to access the other accounts.
Create separate identities and passwords for the developer on both the Test and Production accounts.
Enable AWS multi-factor authentication (MFA) to the IAM User of the developer.
#### info

### 
To improve their information security management system (ISMS), a company recently released a new policy which requires all database credentials to be encrypted and be automatically rotated to avoid unauthorized access.

Which of the following is the MOST appropriate solution to secure the credentials?
#### do
Create a secret in AWS Secrets Manager and enable automatic rotation of the database credentials.
#### dont

Create an IAM Role which has full access to the database. Attach the role to the services which require access.
Enable IAM DB authentication which rotates the credentials by default.

Create a parameter to the Systems Manager Parameter Store using the PutParameter API with a type of SecureString.
#### info


### 
A cryptocurrency exchange portal has a key management service hosted in their on-premises data center, which stores encryption keys and uses an RSA asymmetric encryption algorithm. The company has recently implemented a hybrid cloud architecture in AWS and you were assigned to migrate the exchange portal to their cloud infrastructure. For security compliance, the keys should be stored in dedicated, third-party validated hardware security modules under your exclusive control.

Which of the following is the BEST solution that you should implement to meet the above requirement?
#### do
Import the encryption keys from your on-premises key management service to AWS CloudHSM.
#### dont
Use AWS KMS to store and manage the encryption keys.
Develop a custom key management service using the AWS Encryption SDK.
Import the encryption keys from your on-premises key management service to AWS Secrets Manager as Customer Master Keys (CMKs).
#### info
AWS CloudHSM provides hardware security modules in AWS Cloud. A hardware security module (HSM) is a computing device that processes cryptographic operations and provides secure storage for cryptographic keys.
– Generate, store, import, export, and manage cryptographic keys, including symmetric keys and asymmetric key pairs.
– Use symmetric and asymmetric algorithms to encrypt and decrypt data.
– Use cryptographic hash functions to compute message digests and hash-based message authentication codes (HMACs).
– Cryptographically sign data (including code signing) and verify signatures.
– Generate cryptographically secure random data.
You should consider using AWS CloudHSM instead of AWS KMS if you require:
– Keys stored in dedicated, third-party validated hardware security modules under your exclusive control.
– FIPS 140-2 compliance.
– Integration with applications using PKCS#11, Java JCE, or Microsoft CNG interfaces.
– High-performance in-VPC cryptographic acceleration (bulk crypto).
Customer Master Keys (CMKs) is incorrect because you can’t store CMKs to AWS Secrets Manager.

### 
A company uses AWS Systems Manager (SSM) Parameter Store to manage configuration details for multiple applications. The parameters are currently stored in the Standard tier. The company wants its operations team to be notified if there are sensitive parameters that haven’t been rotated within 90 days.

Which must be done to meet the requirement?
#### do
#### dont
Convert the sensitive parameters from Standard tier into Advanced tier. Set a NoChangeNotification policy with a value of 90 days. Use Amazon EventBridge (Amazon CloudWatch Events) to send a notification via Amazon SNS.

Configure a NoChangeNotification policy with a value of 90 days. Use Amazon EventBridge (Amazon CloudWatch Events) to send a notification via Amazon SNS.

Convert the sensitive parameters from Standard tier into Advanced tier. Set a ExpirationNotification policy with a value of 90 days. Use Amazon EventBridge (Amazon CloudWatch Events) to send a notification via Amazon SNS.
Set up an Amazon EventBridge (Amazon CloudWatch Events) event pattern that captures SSM Parameter-related events. Use Amazon SNS to send notifications.
#### info
 - NoChangeNotification - sends notification by reading the LastModifiedTime attribute of the parameter
 - ExpirationNotification - deletes parameter after given amount of time regardless if changed or not
 - Standard tier - does not support notification policies

### 
A product design firm has adopted a remote work policy and wants to provide employees with access to a suite of CAD software through EC2 Spot instances. These instances will be deployed using a CloudFormation template. The development team must be able to securely obtain software license keys in the template each time it is needed.

Which solution meets this requirement while offering the most secure and cost-effective approach?
#### do
Store the license key as a SecureString in AWS Systems Manager (SSM) Parameter Store. Use the ssm-secure dynamic reference to retrieve the secret in the CloudFormation template.
#### dont
Embed the license keys in the Mapping section of the CloudFormation template. Let users choose the correct license key using the Parameter section. Enable the NoEcho attribute on the parameter.
Pass the license key in the Parameter section of the CloudFormation template during stack creation. Enable the NoEcho attribute on the parameter.
Store the license key as a secret in AWS Secrets Manager. Use the secretsmanager dynamic reference to retrieve the secret in the CloudFormation template.
#### info
Secrets manager SSPS costs money
Systems Manager SSM is free

### I dont understand this
A company is currently in the process of integrating their on-premises data center to their cloud infrastructure in AWS. One of the requirements is to integrate the on-premises Lightweight Directory Access Protocol (LDAP) directory service to their AWS VPC using IAM.

Which of the following provides the MOST suitable solution to implement if the identity store that they are using is not compatible with SAML?
#### do
Create a custom identity broker application in your on-premises data center and use STS to issue short-lived AWS credentials.
#### dont
Implement the AWS IAM Identity Center service to manage access between AWS and your LDAP.
Create IAM roles to rotate the IAM credentials whenever LDAP credentials are updated.
Set up an IAM policy that references the LDAP identifiers and AWS credentials.
#### info
 - LDAP : helps users find data about organizations, persons, and more
 - SAML : Security Assertion Markup Language a standardized way to tell external applications and services that a user is who they say they are uses SSO

### 
You are a software developer for a multinational investment bank which has a hybrid cloud architecture with AWS. To improve the security of their applications, they decided to use AWS Key Management Service (KMS) to create and manage their encryption keys across a wide range of AWS services. You were given the responsibility to integrate AWS KMS with the financial applications of the company.

Which of the following are the recommended steps to locally encrypt data using AWS KMS that you should follow? (Select TWO.)
#### do
Erase the encrypted data key from memory and store the plaintext data key alongside the locally encrypted data.
Use the GenerateDataKey operation to get a data encryption key then use the plaintext data key in the response to encrypt data locally.
#### dont
Encrypt data locally using the Encrypt operation.
Use the GenerateDataKeyWithoutPlaintext operation to get a data encryption key then use the plaintext data key in the response to encrypt data locally.
Erase the plaintext data key from memory and store the encrypted data key alongside the locally encrypted data.

#### info

### 
A company has created a private S3 bucket named tdojo. The Developer IAM role must be granted read access to all objects within this bucket. However, objects stored under the qa folder should be restricted to the QA IAM role only.

Which S3 bucket policy will effectively implement the principle of least privilege access while satisfying the given requirements?
#### do
#### dont
#### info
just look at the permissions given to the different roles
also the question is written wrong
it sounds like the devs shouldnt have access to the qa folder but they do




### 
A company is using AWS Organizations to manage its multiple AWS accounts which is being used by its various departments. To avoid security issues, it is of utmost importance to test the impact of service control policies (SCPs) on your IAM policies and resource policies before applying them.

Which of the following services can you use to test and troubleshoot IAM and resource-based policies?
#### do
#### dont
AWS Config
IAM Policy Simulator
Systems Manager
Amazon Inspector
#### info
 - IAM policy simulator : evaluates the policies that you choose and determines the effective permissions for each of the actions that you specify
   - does not make an actual AWS service request
 - AWS Config : service that enables you to assess, audit, and evaluate the configurations of your AWS resources
 - Systems Manager : unified user interface to view operational data from multiple AWS services, automate operational tasks across AWS resources
 - Amazon Inspector : automated security assessment service, improves the security and compliance of applications deployed on AWS.


### 
Your manager assigned you a task of implementing server-side encryption with customer-provided encryption keys (SSE-C) to your S3 bucket, which will allow you to set your own encryption keys. Amazon S3 will manage both the encryption and decryption process using your key when you access your objects, which will remove the burden of maintaining any code to perform data encryption and decryption.

To properly upload data to this bucket, which of the following headers must be included in your request?
#### do
x-amz-server-side​-encryption​-customer-algorithm, x-amz-server-side-encryption-customer-key and x-amz-server-side-encryption-customer-key-MD5 headers
#### dont
x-amz-server-side-encryption-customer-key header only

x-amz-server-side-encryption and x-amz-server-side-encryption-aws-kms-key-id headers

x-amz-server-side-encryption, x-amz-server-side-encryption-customer-key and x-amz-server-side-encryption-customer-key-MD5 headers
#### info
 - x-amz-server-side-encryption-customer-algorithm : required header specifies the encryption algorithm. The header value must be “AES256”.

 - x-amz-server-side-encryption-customer-key : This header provides the 256-bit, base64-encoded encryption key for Amazon S3 to use to encrypt or decrypt your data.

 - x-amz-server-side-encryption-customer-key-MD5 : This header provides the base64-encoded 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

### 
A startup has recently launched a high-quality photo sharing portal using Amazon Lightsail and S3. They noticed that there are other external websites which are linking and using their photos without permission. This has caused an increase on their data transfer cost and potential revenue loss.

Which of the following is the MOST effective method to solve this issue?
#### do
Configure the S3 bucket to remove public read access and use pre-signed URLs with expiry dates.
#### dont
Block the IP addresses of the offending websites using Network Access Control List.
Enable cross-origin resource sharing (CORS) which allows cross-origin GET requests from all origins.
Use a CloudFront web distribution to serve the photos.
#### info

### 
A web application is currently using an on-premises Microsoft SQL Server 2019 Enterprise Edition database. Your manager instructed you to migrate the application to Elastic Beanstalk and the database to RDS. For additional security, you must configure your database to automatically encrypt data before it is written to storage, and automatically decrypt data when the data is read from storage.

Which of the following services will you use to achieve this?
#### do
Enable Transparent Data Encryption (TDE).
#### dont
Use IAM DB Authentication.
Use Microsoft SQL Server Windows Authentication.
Enable RDS Encryption.
#### info
- Transparent Data Encryption (TDE) : encrypt stored data on your DB instances running Microsoft SQL Server. encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.
- Enable RDS Encryption : encrypts your Amazon RDS DB instances and snapshots at rest. 

### 
To improve their information security management system (ISMS), a company recently released a new policy which requires all database credentials to be encrypted and be automatically rotated to avoid unauthorized access.

Which of the following is the MOST appropriate solution to secure the credentials?
#### do
Create a secret in AWS Secrets Manager and enable automatic rotation of the database credentials.
#### dont
Create a parameter to the Systems Manager Parameter Store using the PutParameter API with a type of SecureString.
Enable IAM DB authentication which rotates the credentials by default.
Create an IAM Role which has full access to the database. Attach the role to the services which require access.
#### info

### 
A developer is working on an application that will process files encrypted with a data key generated from a KMS key. The application needs to decrypt the files locally before it can proceed with the processing of the files.

Which of the following are valid and secure steps in decrypting data? (Select TWO.)
#### do
Use the Decrypt operation to decrypt the encrypted data key.
Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory.
#### dont
Use the Decrypt operation to decrypt the plaintext data key.
Use the plaintext data key to decrypt data locally, then erase the encrypted data key from memory.
Use the encrypted data key to decrypt data locally, then erase the encrypted data key from memory.

#### info


### 
A developer is building an application that will be hosted in ECS and must be configured to run tasks and services using the Fargate launch type. The application will have four different tasks, each of which will access different AWS resources than the others.

Which of the following is the MOST efficient solution that can provide your application in ECS access to the required AWS resources?
#### do
Create 4 different IAM Roles with the required permissions and attach them to each of the 4 ECS tasks.
#### dont
Create 4 different Service-Linked Roles with the required permissions and attach them to each of the 4 ECS tasks.
Create 4 different Container Instance IAM Roles with the required permissions and attach them to each of the 4 ECS tasks.
Create an IAM Group with all the required permissions and attach them to each of the 4 ECS tasks.
#### info
 - Fargate : serverless compute engine for containers that works with ECS and Elastic Kubernetes Service (EKS). 
   - runs containers without having to manage the underlying server infrastructure. 
   - abstracts away the need to manage servers or clusters of Amazon EC2 instances
   - enhances security through workload isolation by design
 - you cannot directly attach an IAM Group to an ECS Task
 - Container Instance IAM Role : only applies if you are using the EC2 launch type
 - service-linked role : a unique type of IAM role that is linked directly to Amazon ECS itself, not on the ECS task

###
A company has a static website running in an Auto Scaling group of EC2 instances which they want to convert as a dynamic e-commerce web portal. One of the requirements is to use HTTPS to improve the security of their portal and also improve their search ranking as a reputable and secure site. A developer recently requested an SSL/TLS certificate from a third-party certificate authority (CA) which is ready to be imported to AWS.

Which of the following services can the developer use to safely import the SSL/TLS certificate? (Select TWO.) 
#### do
AWS Certificate Manager : use this one
IAM certificate store : use this ones in regions that dont support AWS cert manager
#### dont
Amazon Cognito
CloudFront
A private S3 bucket with versioning enabled
#### info
 - IAM certificate store : part of IAM, manage SSL/TLS server certificates for use with AWS services. 
   - upload cert aws iam upload-server-certificate --server-certificate-name elastic-beanstalk-x509 --certificate-body file://https-cert.crt --private-key file://private-key.pem


### 
A financial mobile application has a serverless backend API which consists of DynamoDB, Lambda, and Cognito. Due to the confidential financial transactions handled by the mobile application, there is a new requirement provided by the company to add a second authentication method that doesn’t rely solely on user name and password.

Which of the following is the MOST suitable solution that the developer should implement?

#### do
Integrate multi-factor authentication (MFA) to a user pool in Cognito to protect the identity of your users.
#### dont
Create a custom application that integrates with Amazon Cognito which implements the second layer of authentication.
Use a new IAM policy to a user pool in Cognito.
Use Cognito with SNS to allow additional authentication via SMS.
#### info

### 
A programmer is developing a Node.js application that will be run on a Linux server in their on-premises data center. The application will access various AWS services such as S3, DynamoDB, and ElastiCache using the AWS SDK.

Which of the following is the MOST suitable way to provide access for the developer to accomplish the specified task?
#### do
#### dont
Go to the AWS Console and create a new IAM user with programmatic access. In the application server, create the credentials file at ~/.aws/credentials with the access keys of the IAM user.

Go to the AWS Console and create a new IAM User with the appropriate permissions. In the application server, create the credentials file at ~/.aws/credentials with the username and the hashed password of the IAM User.

Create an IAM role with the appropriate permissions to access the required AWS services and assign the role to the on-premises Linux server. Whenever the application needs to access any AWS services, request for temporary security credentials from STS using the AssumeRole API.
Create an IAM role with the appropriate permissions to access the required AWS services. Assign the role to the on-premises Linux server.
#### info


### 
#### do
#### dont
#### info

### 
#### do
#### dont
#### info


### 
#### do
#### dont
#### info

### 
#### do
#### dont
#### info


### 
#### do
#### dont
#### info

### 
#### do
#### dont
#### info


### 
#### do
#### dont
#### info

### 
#### do
#### dont
#### info


### 
#### do
#### dont
#### info

### 
#### do
#### dont
#### info


### 
#### do
#### dont
#### info

### 
#### do
#### dont
#### info





## Development


### 
#### do
#### dont
#### info



## Troubleshooting + Optimization



### 
#### do
#### dont
#### info
