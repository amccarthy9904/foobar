


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
Convert the sensitive parameters from Standard tier into Advanced tier. Set a NoChangeNotification policy with a value of 90 days. Use Amazon EventBridge (Amazon CloudWatch Events) to send a notification via Amazon SNS.
#### dont
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
Go to the AWS Console and create a new IAM user with programmatic access. In the application server, create the credentials file at ~/.aws/credentials with the access keys of the IAM user.
#### dont

Go to the AWS Console and create a new IAM User with the appropriate permissions. In the application server, create the credentials file at ~/.aws/credentials with the username and the hashed password of the IAM User.
Create an IAM role with the appropriate permissions to access the required AWS services and assign the role to the on-premises Linux server. Whenever the application needs to access any AWS services, request for temporary security credentials from STS using the AssumeRole API.
Create an IAM role with the appropriate permissions to access the required AWS services. Assign the role to the on-premises Linux server.
#### info
 - programmatic access : applications and scripts that make programmatic calls to AWS services

### 
A developer runs a shell script that uses the aws s3 cp CLI to upload a large file to an S3 bucket. The S3 bucket is configured with Server-side encryption with AWS Key Management Service (SSE-KMS). An Access Denied error always shows up whenever the developer uploads a file with a size of 100 GB or more. However, whenever he uploads a smaller file, the request succeeds.

Which of the following are possible reasons why this issue is happening? (Select TWO.)
#### do
The AWS CLI S3 commands perform a multipart upload when the file is large.
The developer does not have the kms:Decrypt permission.
#### dont
The developer's IAM permission has an attached inline policy that restricts him from uploading a file to S3 with a size of 100 GB or more.
The maximum size that can be encrypted in KMS is only 100 GB.
The developer does not have the kms:Encrypt permission.
#### info
 - aws s3 cp : When you use the aws s3 cp command to upload a file larger than 100GB to Amazon S3, the AWS CLI automatically switches to using multipart upload, chunks
 - you need kms:Decrypt and kms:GenerateDataKey* permissions because Amazon S3 must decrypt and read data from the encrypted file parts before it completes the multipart upload

### 
An application hosted in an Auto Scaling group of On-Demand EC2 instances is used to process data polled from an SQS queue and the generated output is stored in an S3 bucket. To improve security, you were tasked to ensure that all objects in the S3 bucket are encrypted at rest using server-side encryption with AWS KMS–Managed Keys (SSE-KMS).

Which of the following is required to properly implement this requirement?
#### do
Add a bucket policy which denies any s3:PutObject action unless the request includes the x-amz-server-side-encryption header.
#### dont
Add a bucket policy which denies any s3:PutObject action unless the request includes the x-amz-server-side-encryption-aws-kms-key-id header.

Add a bucket policy which denies any s3:PostObject action unless the request includes the x-amz-server-side-encryption header.

Add a bucket policy which denies any s3:PostObject action unless the request includes the x-amz-server-side-encryption-aws-kms-key-id header.
#### info
 - SQS queue : fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications
 - x-amz-server-side-encryption : specify the server-side encryption algorithm that should be applied to the object
 - x-amz-server-side-encryption-aws-kms-key-id : specifies a specific key to use during encryption

### 
A developer is using API Gateway Lambda Authorizer to securely authenticate the API requests to their web application. The authentication process should be implemented using a custom authorization scheme which accepts header and query string parameters from the API caller.

Which of the following methods should the developer use to properly implement the above requirement?
#### do
#### dont
#### info

### 
A developer is using API Gateway Lambda Authorizer to securely authenticate the API requests to their web application. The authentication process should be implemented using a custom authorization scheme which accepts header and query string parameters from the API caller.

Which of the following methods should the developer use to properly implement the above requirement?
#### do
Request Parameter-based Authorization
#### dont
Token-based Authorization
Cross-Account Lambda Authorizer
Amazon Cognito User Pools Authorizer
#### info


### 
A developer needs to encrypt all objects being uploaded by their application to the S3 bucket to comply with the company’s security policy. The bucket will use server-side encryption with Amazon S3-Managed encryption keys (SSE-S3) to encrypt the data using 256-bit Advanced Encryption Standard (AES-256) block cipher.

Which of the following request headers should the developer use?
#### do
x-amz-server-side-encryption
#### dont
x-amz-server-side-encryption-customer-key-MD5
x-amz-server-side-encryption-customer-algorithm
x-amz-server-side-encryption-customer-key
#### info
 - x-amz-server-side-encryption-customer-algorithm : specify the encryption algorithm for server-side encryption with customer-provided keys (SSE-C)

### 
A developer is using API Gateway Lambda Authorizer to provide authentication for every API request and control access to your API. The requirement is to implement an authentication strategy which is similar to OAuth or SAML.

Which of the following is the MOST suitable method that the developer should use in this scenario?
#### do
Token-based Authorization
#### dont
Cross-Account Lambda Authorizer
Request Parameter-based Authorization
AWS STS-based Authentication
#### info
 - Requesting Parameter-based Lambda Authorization is incorrect because this does not use tokens to identify a caller

 - AWS STS-based authentication is incorrect because this is not a valid type of API Gateway Lambda Authorizer.

 - Cross-Account Lambda Authorizer is incorrect because this just enables you to use an AWS Lambda function from a different AWS account as your API authorizer function. not a valid Lambda authorizer type.

### 
Your development team is currently developing a financial application in AWS. One of the requirements is to create and control the encryption keys used to encrypt your data using the envelope encryption strategy to comply with the strict IT security policy of the company.

Which of the following correctly describes the process of envelope encryption?
#### do
Encrypt plaintext data with a data key and then encrypt the data key with a top-level plaintext master key.
#### dont
Encrypt plaintext data with a data key and then encrypt the data key with a top-level encrypted master key.
Encrypt plaintext data with a master key and then encrypt the master key with a top-level encrypted data key.
Encrypt plaintext data with a master key and then encrypt the master key with a top-level plaintext data key.
#### info
 - envelope encryption strategy : encrypting data with a data encryption key (DEK) and then encrypting the DEK with another key(root key or a customer master key (CMK))

###
A serverless application is composed of several Lambda functions which reads data from RDS. These functions must share the same connection string that should be encrypted to improve data security.

Which of the following is the MOST secure way to meet the above requirement?
#### do
Create a Secure String Parameter using the AWS Systems Manager Parameter Store.
#### dont
Create an IAM Execution Role that has access to RDS and attach it to the Lambda functions.
Use AWS Lambda environment variables encrypted with CloudHSM.
Use AWS Lambda environment variables encrypted with KMS which will be shared by the Lambda functions.
#### info
 - Lambda environment variables : not sharable across Lambda envs
 - CloudHSM : not used with Lambda, KMS is preferred
 - AWS SSPS Systems Manager Parameter Store : secure, hierarchical storage for configuration data and secrets management. store data, passwords, db strings, license codes as parameter values. store plain text or encrypted data.


### 
A company has a suite of web applications that is heavily using RDS database in Multi-AZ Deployments configuration with several Read Replicas. For improved security, you were instructed to ensure that all of their database credentials, API keys, and other secrets are encrypted and rotated on a regular basis. You should also configure your applications to use the latest version of the encrypted credentials when connecting to the RDS database.

Which of the following is the MOST appropriate solution to secure the credentials?
#### do
Use AWS Secrets Manager to store and encrypt the credentials and enable automatic rotation.
#### dont
Store the credentials in AWS KMS.
Store the credentials to Systems Manager Parameter Store with a SecureString data type.
Store the credentials to AWS ACM.
#### info
 - SSPS : does not provide automatic rotation

### 
A software engineer is building a serverless application in AWS consisting of Lambda, API Gateway, and DynamoDB. She needs to implement a custom authorization scheme that uses a bearer token authentication strategy such as OAuth or SAML to determine the caller’s identity.

Which of the features of API Gateway is the MOST suitable one that she should use to build this feature?
#### do
#### dont
#### info
 - Cross-Account Lambda Authorizer : use an AWS Lambda function from a different AWS account as your API authorizer function

### 
You are developing a new batch job for the enterprise application suite in your company, which is hosted in an Auto Scaling group of EC2 instances behind an ELB. The application is using an S3 bucket configured with Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS). The batch job must upload files to the bucket using the default AWS KMS key to protect the data at rest.

What should you do to satisfy this requirement with the LEAST amount of configuration?
#### do
Include the x-amz-server-side-encryption header with a value of aws:kms in your upload request.
#### dont
Include the x-amz-server-side-encryption header with a value of AES256 in your upload request.

Include the x-amz-server-side-encryption header with a value of aws:kms as well as the x-amz-server-side-encryption-aws-kms-key-id header containing the ID of the default AWS KMS key in your upload request.

Include the x-amz-server-side​-encryption​-customer-algorithm, x-amz-server-side-encryption-customer-key, and x-amz-server-side-encryption-customer-key-MD5 headers with appropriate values in the upload request.
#### info
 - aws:kms :  AWS Key Management Service (AWS KMS) keys (SSE-KMS) managed keys
 - AES256 :  Amazon S3-managed keys (SSE-S3) or customer SSE-C

### 
A developer is building the cloud architecture of an application which will be hosted in a large EC2 instance. The application will process the data and it will upload results to an S3 bucket.

Which of the following is the SAFEST way to implement this architecture?

#### do
#### dont
Use an IAM Inline Policy to grant the application the necessary permissions to upload data to S3.
Store the access keys in the instance then use the AWS SDK to upload the results to S3.
Install the AWS CLI then use it to upload the results to S3.
Use an IAM Role to grant the application the necessary permissions to upload data to S3.
#### info
 - IAM Inline Policy : policies that are directly attached to a single IAM identity (user, group, or role),  embedded within the identity to which they apply, maintaining a strict one-to-one relationship
 - IAM Role :  IAM identity for authorized entities (users, applications, or services) to perform actions on AWS resources


### 
Your team is developing a serverless application, which is composed of multiple Lambda functions which process data from an SQS queue and stores the results to an RDS database. To comply with the strict IT policy of the company, you were instructed to configure these functions to share the same connection string that should be properly secured and encrypted.

What should you do to protect, encrypt, and share your database credentials in AWS?

#### do
Use AWS Systems Manager Parameter Store as a Secure String Parameter.
#### dont
Use IAM DB Authentication in RDS to allow encrypted connections from each Lambda function.
Store the database credentials as environment variables with KMS encryption which will be shared by the Lambda functions.
Encrypt the database credentials and store them in an S3 bucket which the Lambda functions can fetch.
#### info


## Development


### 
A web application is uploading large files, which are over 4 GB in size, in an S3 bucket called data.tutorialsdojo.com every 30 minutes. You want to minimize the time required to upload each file. Which of the following should you do to minimize upload time?
#### do
Use the Multipart upload API.
#### dont
Use the BatchWriteItem API.
Enable Transfer Acceleration in the bucket.
Use the Putltem API.
#### info
 - BatchWriteItem API : DynamoDB puts or deletes multiple items in one or more tables
 - Multipart upload API : uploading of large objects to S3 in smaller parts, or "chunks," and then assemble them on the server-side to create the complete object
 - Transfer Acceleration :  speed up the transfer of files over long distances between your client and an Amazon S3 bucket
 - Putltem API : DynamoDB Creates a new item, or replaces an old item with a new item.

### 
A developer is building a new Docker application using ECS. She needs to allow containers to access ports on the host container instance to send or receive traffic using port mapping.

Which component of ECS should the developer configure to properly implement this task?
#### do
Task definition
#### dont
Container Agent
Container instance
Service scheduler
#### info
 - Container Agent : runs on each container instance within an ECS cluster
 - Container instance : an EC2 instance that has been configured to run Docker containers and the ECS Container Agent
 - Task definition : blueprint for application describes one or more containers specifies, image to use, resource requirements, network config
 - Service scheduler : ensures that the specified number of tasks are always running and automatically handles scaling and maintaining availability

### 
You are using an AWS Lambda function to process records in an Amazon Kinesis Data Streams stream which has 100 active shards. The Lambda function takes an average of 10 seconds to process the data and the stream is receiving 50 new items per second.

Which of the following statements are TRUE regarding this scenario
#### do
There will be at most 100 Lambda function invocations running concurrently.
#### dont
The Lambda function has 500 concurrent executions.
The Kinesis shards must be merged to increase the data capacity of the stream as well as the concurrency execution of the Lambda function.
The Lambda function will throttle the incoming requests due to the excessive number of Kinesis shards.
#### info
 - shard : base throughput unit of an Amazon Kinesis data stream
   - A single shard can ingest up to 1,000 data records per second or 1 MB/sec. For reads, it supports up to 2 MB/sec
 - Lambda :  each Lambda invocation is associated with a specific shard, and the processing of records is scoped to that shard

### 
A startup has recently launched their new mobile game and is gaining a lot of new users everyday. The founders plan to add a new feature which will enable cross-device syncing of user profile data across mobile devices to improve the user experience.

Which of the following services should they use to meet this requirement?
#### do
Cognito Sync
#### dont
AWS Amplify
Cognito User Pools
Cognito Identity Pools
#### info
 - Cognito Sync : synchronize application-related user data across devices
 - Cognito User Pools : user directory for web and mobile app authentication and authorization
 - Cognito Identity Pools : provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have been authenticated and received a token

### 
A global financial company has hundreds of users from all over the world that regularly upload terabytes of transactional data to a centralized S3 bucket. You noticed that there are some users from different parts of the globe that take a lot of time to upload their data, which causes delays in the processing. You need to improve data throughput and ensure consistently fast data transfer to the S3 bucket regardless of the user’s location.

Which of the following features should you use to satisfy the above requirement?

#### do
Amazon S3 Transfer Acceleration
#### dont
AWS Direct Connect
CloudFront
AWS Transfer for SFTP
#### info
 - AWS Transfer for SFTP : use sftp for transfer into s3 
 - AWS Direct Connect : establishes a dedicated network connection from your premises to AWS
 - CloudFront : CDN. It securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds

### 
A developer is designing the cloud architecture of an internal application which will be used by about a hundred employees. She needs to ensure that the architecture is elastic enough to adequately match the supply of resources to the demand while maintaining its cost-effectiveness.

Which of the following services can provide the MOST elasticity to the architecture? (Select TWO.)
#### do
DynamoDB
EC2 Spot Fleet
#### dont
RDS
WAF
CloudFront
#### info
 - RDS : set up, operate, and scale a relational database in the cloud, doesn’t have the auto-scaling capabilities to dynamically adjust its capacity based on the demand, unlike DynamoDB
 - WAF (Web Application Firewall) : protect your web applications or APIs against common web exploits that could affect application availability, compromise security, or consume excessive resources
 - DynamoDB : key-value and document database
 - EC2 Spot Fleet : request a fleet of Spot Instances, spare Amazon EC2 computing capacity available at up to a 90% discount compared to On-Demand prices


### 
A developer has recently completed a new version of a serverless application that is ready to be deployed using AWS SAM. There is a requirement that the traffic should shift from the previous Lambda function to the new version in the shortest time possible, but you still don’t want to shift traffic all-at-once immediately.

Which deployment configuration is the MOST suitable one to use in this scenario?
#### do
CodeDeployDefault.LambdaCanary10Percent5Minutes
#### dont
CodeDeployDefault.HalfAtATime
CodeDeployDefault.LambdaLinear10PercentEvery1Minute
CodeDeployDefault.LambdaLinear10PercentEvery2Minutes
#### info
deployment preferences are part of the DeploymentPreference property under the AWS::Serverless::Function resource type
CodeDeployDefault.HalfAtATimeis incorrect because this is only applicable for EC2/On-premises compute platform and not for Lambda

### 
You recently deployed an application to a newly created AWS account, which uses two identical Lambda functions to process ad-hoc requests. The first function processes incoming requests efficiently but the second one has a longer processing time even though both of the functions have exactly the same code. Based on your monitoring, the Throttles metric of the second function is greater than the first one in Amazon CloudWatch.

Which of the following are possible solutions that you can implement to fix this issue? (Select TWO.)
#### do
Set the concurrency execution limit of both functions to 500.
Set the concurrency execution limit of the second function to 0.
Configure the second function to use an unreserved account concurrency.
#### dont
Set the concurrency execution limit of both functions to 450.
Decrease the concurrency execution limit of the first function.
#### info
 - Throttles metric : how many requests the Lambda funct is throttleing itself from proccessing
 - concurrency execution limit : the number of instances of the function that can run simultaneously, default 1000 across all Lambda functions, need to keep 100 unreserved to spread across non configured lambda functions

### 
A company decided to re-use the same Lambda function for multiple stages of their API, but the function should read data from a different Amazon DynamoDB table depending on which stage is being called. In order to accomplish this, they instructed the developer to pass configuration parameters to a Lambda function through mapping templates in API Gateway.

Which of the following is the MOST suitable solution that the developer should use to meet this requirement?
#### do
Use Stage Variables.
#### dont
Set up traffic shifting with Lambda Aliases.
Create environment variables in the Lambda function.
Set up an API Gateway Private Integration to the Lambda function.
#### info
 - Stage Variables : name-value pairs that you can define as configuration attributes associated with a deployment stage of a REST API
 - API Gateway Private Integration : expose HTTP/HTTPS resources within an Amazon Virtual Private Cloud (VPC) to clients outside of the VPC
 - traffic shifting with Lambda Aliases : gradually shift incoming traffic between two versions of an AWS Lambda function based on pre-assigned weights

### 
A company has assigned a developer to automate the patch management, data synchronization, and other recurring tasks in their department. The developer needs to have a service which can coordinate multiple AWS services into serverless workflows.

Which of the following is the MOST cost-effective service that the developer should implement in this scenario?
#### do
AWS Step Functions - coordinate multiple AWS services into serverless workflows
#### dont
AWS Batch
AWS Lambda
SWF
#### info
 - AWS Lambda pricing : is based on the number of requests and the duration of function execution time
 - Batch pricing : type and number of instances used to run batch jobs, the amount of storage used, and the data transfer costs

### 
A serverless application is using API Gateway with a non-proxy Lambda Integration. A developer was tasked to expose a GET method on a new /getcourses resource to invoke the Lambda function, which will allow the consumers to fetch a list of online courses in JSON format. The consumers must include a query string parameter named courseType in their request to get the data.

What is the MOST efficient solution that the developer should do to accomplish this requirement?
#### do
Configure the method request of the resource.
#### dont
Configure the integration request of the resource.
Configure the integration response of the resource.
Configure the method response of the resource.
#### info

### 
A company is developing a serverless website that consists of images, videos, HTML pages and JavaScript files. There is also a requirement to serve the files with lowest possible latency to its global users.

Which combination of services should be used in this scenario? (Select TWO.)
#### do
Amazon S3
Amazon CloudFront
#### dont
Amazon Elastic File System
Amazon EC2
Amazon Glacier
#### info
 - cloudfront : cdn
 - Amazon Elastic File System : not good for static files, doesnt integrate with cloud front
 - ec2 : region spcific, not distributed

### 
A developer is working on an application which stores data to an Amazon DynamoDB table with the DynamoDB Streams feature enabled. He set up an event source mapping with DynamoDB Streams and AWS Lambda function to monitor any table changes then store the original data of the overwritten item in S3. When an item is updated, it should only send a copy of the item’s previous value to an S3 bucket and maintain the new value in the DynamoDB table.

Which StreamViewType is the MOST suitable one to use in the DynamoDB configuration to fulfill this scenario?
#### do
OLD_IMAGE
#### dont
KEYS_ONLY
NEW_AND_OLD_IMAGES
NEW_IMAGE
#### info
 - DynamoDB Streams : a time-ordered sequence of item level changes in any DynamoDB table
 - NEW_IMAGE : captures the entire item as it appears after it was modified. all attribute names, values
 - KEYS_ONLY : captures only the key attributes of modified item. does not include any of item's attribute values
 - NEW_AND_OLD_IMAGES :  both the new and the old images of the item.
 - OLD_IMAGE : entire item as it appeared before it was modified.


### 
A media company seeks to protect its copyrighted images from unauthorized distribution. They want images uploaded to their Amazon S3 bucket to be automatically watermarked. A developer has already prepared the Lambda function for this image-processing job.

Which option must the developer configure to automatically invoke the function at each upload?
#### do
#### dont
Set up an Amazon S3 Event Notification to trigger the Lambda function when an ObjectCreated:Put event is detected in the bucket.
Enable S3 Storage Lens to monitor the bucket and configure the Lambda function to be invoked whenever the metrics indicate a new object creation.

Configure an S3 Lifecycle policy to transition images to the INTELLIGENT_TIERING storage class. Use S3 Inventory to generate a report of images that weren’t watermarked and set up the Lambda function to process the report.
Use S3 Select to identify unwatermarked images based on metadata and create an EventBridge rule that triggers the Lambda function upon such findings.
#### info
 - S3 Lifecycle policies : manage storage transitions and object expirations, not event-driven actions like invoking Lambda functions upon upload
 - S3 Select : retrieve specific subsets of data from objects in S3 without retrieving the entire object
 - S3 Storage Lens : provide visibility into storage usage and activity trends
 - ObjectCreated:Put : event to immediately trigger a Lambda function when an object is uploaded to the S3 bucket
 
### 
A company has a website hosted in a multicontainer Docker environment in Elastic Beanstalk. There is a requirement to integrate the website with API Gateway, where it simply passes client-submitted method requests to the backend. It is important that the client and backend interact directly with no intervention from API Gateway after the API method is set up, except for known issues such as unsupported characters.

Which of the following integration types is the MOST suitable one to use to meet this requirement?
#### do
AWS_PROXY
#### dont
AWS
HTTP
HTTP_PROXY
#### info
 - AWS : expose AWS service actions
 - AWS_PROXY : Lambda proxy integration, integrating an API method with a Lambda function invocation action
 - HTTP : expose HTTP endpoints in the backend
 - HTTP_PROXY : client to access backend HTTP endpoints with a streamlined integration setup on a single API method

### 
A programmer is developing a shell script that uses AWS CLI to list all objects of a given bucket. However, the script is timing out if the bucket has tens of thousands of objects.

Which solution would most likely rectify the issue?
#### do
Add pagination parameters in the AWS CLI command
#### dont
Use S3 Select
Enable Amazon S3 Transfer Acceleration
Enable CORS
#### info


### 
A company is re-architecting its legacy application to use AWS Lambda and DynamoDB. The table is provisioned to have 10 read capacity units, and each item has a size of 4 KB.

How many eventual and strong consistent read requests can the table handle per second?
#### do
10 strongly consistent reads and 20 eventually consistent reads per second
#### dont
20 strongly consistent reads and 10 eventually consistent reads per second
5 strongly consistent reads and 20 eventually consistent reads per second
10 strongly consistent reads and 10 eventually consistent reads per second
#### info
 - read request unit : represents one strongly consistent read request, or two eventually consistent read requests per 4KB


### 
You are developing an online game where the app preferences and game state of the player must be synchronized across devices. It should also allow multiple users to synchronize and collaborate shared data in real time.

Which of the following is the MOST appropriate solution that you should implement in this scenario?

Integrate AWS AppSync to your mobile app.
Integrate AWS Amplify to your mobile app.
Integrate Amazon Cognito Sync to your mobile app.
Integrate Amazon Pinpoint to your mobile app.
#### do
#### dont
#### info
 - AppSync : simplifies the development of GraphQL APIs by handling the heavy lifting of connecting to data sources, managing authentication, and providing real-time data updates
 - Cognito Sync : does not allow multiple users to synchronize and collaborate in real-time on shared data
 - Pinpoint : engage with your customers send push notifications, emails, SMS text messages, and voice messages

### 

Category: CDA – Development with AWS Services
A mobile game is using a DynamoDB table named GameScore that keeps track of users and scores. Each item in the table is identified by a partition key (UserId) and a sort key (GameTitle). The diagram below shows how the items in the table are organized:

A developer wants to write a leaderboard application to display the top scores for each game.

How can the developer meet the requirement in the MOST efficient manner?

#### do
Create a global secondary index. Assign the GameTitle attribute as the partition key and the TopScore attribute as the sort key.
#### dont
Use the Scan operation and filter the results based on a GameTitle value.
Create a local secondary index. Assign the TopScore attribute as the partition key and the GameTitle attribute as the sort key.
Create a local secondary index. Assign the GameTitle attribute as the partition key and the TopScore attribute as the sort key.
#### info
 - global secondary index : have a partition key and an optional sort key that can be different from those on the base table
   - own provisioned throughput settings for read and write activity, separate from those of the table
   - index items across all partitions of the base table without any size constraints
   - can be added to an existing table at any time
   - dont support strongly consistent reads, all reads are eventually consistent
 - local secondary index : same partition key as the base table but a different sort key
   - share provisioned throughput settings for read and write activity with the table they are indexing
   - 10GB item collection size limit for any one partition key value
   - must be created when the table is created.
   - support strongly consistent reads
 - Scan operation : reads every item in a table
### 
A developer is planning to add a global secondary index in a DynamoDB table. This will allow the application to query a specific index that can span all of the data in the base table, across all partitions.

Which of the following should the developer consider when using this type of index? (Select TWO.)

#### do
Queries on this index support eventual consistency only.
#### dont
For each partition key value, the total size of all indexed items must be 10 GB or less.
Queries or scans on this index consume read capacity units from the base table.
When you query this index, you can choose either eventual consistency or strong consistency.
Queries or scans on this index consume capacity units from the index, not from the base table.
#### info


### 
Both the read and write operations to your DynamoDB table are throttled, which are causing errors in your application. You checked the CloudWatch metrics but they indicate that the consumed capacity units haven’t exceeded the provisioned capacity units. Upon further investigation, you found that the issue is caused by a “hot partition” in your table in which a certain partition is accessed by your downstream applications much more frequently than other partitions.

What should you do to resolve this issue in your application with MINIMAL cost? (Select TWO.)

#### do
Implement error retries and exponential backoff.
Refactor your application to distribute your read and write operations as evenly as possible across your table.
#### dont
Increase the amount of read or write capacity for your table.
Implement read sharding to distribute workloads evenly.
Use DynamoDB Accelerator (DAX).
#### info
 -  DynamoDB Accelerator (DAX) : is incorrect because although this will solve the problem, it still entails additional cost to maintain a DAX cluster
 - read or write capacity for your table : is incorrect because although it will also alleviate the throttling issues of your application, it is an expensive solution to implement
 - read sharding to distribute workloads evenly : is incorrect because you should implement a write sharding in your application instead

### 
A company is using OpenAPI, which is also known as Swagger, for the API specifications of their REST web services that are hosted on their on-premises data center. They want to migrate their system to AWS using Lambda and API Gateway. In line with this, you are instructed to create a new API and populate it with the resources and methods from their Swagger definition.

Which of the following is the EASIEST way to accomplish this task?

#### do
Import their Swagger or OpenAPI definitions to API Gateway using the AWS Console.
#### dont
Use CodeDeploy to migrate and deploy the company's web services to API Gateway.
Create models and templates for request and response mappings based on the company's API definitions.
Use AWS SAM to migrate and deploy the company's web services to API Gateway.
#### info


### 
In order to quickly troubleshoot their systems, your manager instructed you to record the calls that your application makes to all AWS services and resources. You developed a custom code that will send the segment documents directly to X-Ray by using the PutTraceSegments API.

What should you include in your segment document to meet the above requirement?

#### do
#### dont
metadata
tracing header
annotations
subsegments
#### info
 - AWS X-Ray : provides developers with tools to analyze and debug their applications
 - subsegments :  record calls to AWS services and resources that your application makes, such as calls to internal or external HTTP web APIs or SQL database queries
 - annotations : key-value pairs that are indexed for use with filter expressions
 - metadata : one or more fields with values of any type, including objects and arrays. Metadata is not indexed by X-Ray, meaning it cannot be used with filter expressions
 - tracing header : for linking together the trace data from different services and resources involved in a request. It contains a unique trace ID assigned to every client request, and each service in the request chain sends traces to X-Ray with this trace ID. 
 
### 
A company has an application that is using CloudFront to serve their static contents to their users around the globe. They are receiving a number of bad reviews from their customers lately because it takes a lot of time to log into their website. Sometimes, their users are also getting HTTP 504 errors which is why the developer was instructed to fix this problem immediately.

Which of the following combination of options should the developer use together to set up a cost-effective solution for this scenario? (Select TWO.)

#### do
Customize the content that the CloudFront web distribution delivers to your users using Lambda@Edge, which allows your Lambda functions to execute the authentication process in AWS locations closer to the users.
Configure an origin failover by creating an origin group with two origins. Specify one as the primary origin and the other as the second origin which CloudFront automatically switches to when the primary origin returns 
#### dont
Launch your application to multiple AWS regions to serve your global users. Use a Route 53 record with latency routing policy to route incoming traffic to the region with the best latency to the user.specific HTTP status code failure responses.
Launch your application to multiple and geographically disperse VPCs on various AWS regions then create a transit VPC to easily connect all your resources. Use several Lambda functions in each region using the AWS Serverless Application Model (SAM) service to improve the overall application performance.

Add a Cache-Control max-age directive to your objects in CloudFront and specify the longest practical value for max-age to increase the cache hit ratio of your CloudFront distribution.
#### info
 - HTTP 504  Gateway Timeout error : server, acting as a gateway or proxy, does not receive a timely response from an upstream server it accessed in attempting to complete the request
 - Lambda@Edge : run code across Amazon CloudFront edge locations globally without provisioning or managing servers, for latency-sensitive use cases where your end viewers are distributed globally, authentication and authorization, dynamic content generation, URL redirection
 - origin failover in CloudFront :  enhance the high availability and reliability of web applications by automatically switching to a secondary origin when the primary origin fails or returns specific HTTP status codes indicating a failure

### 
A tech company has a real-time traffic monitoring system which uses Amazon Kinesis Data Stream to collect data and a group of EC2 instances that consume and process the data stream. Your development team is responsible for adjusting the number of shards in the data stream to adapt to changes in the rate of data flow.

Which of the following are correct regarding Kinesis resharding which your team should consider in managing the application? (Select TWO.)

#### do
You can increase the stream's capacity by splitting shards.
You can decrease the stream's capacity by merging shards.
#### dont
You have to merge the hot shards to increase the capacity of the stream.
You have to split the cold shards to decrease the capacity of the stream.
The data records that are flowing to the parent shards will be lost when you reshard.
#### info
 - Kinesis resharding : adjust the number of shards in your stream to adapt to changes in the rate of data flow through the stream
 - Shard Split:  divides a shard into two, increases data capacity of stream, pay per shard costs money
 - Shard Merge: combines two shards into one, decreases data capacity and cost
 - hot shard : getting more data than expected, split
 - cold shard : getting less data than expected, merge

### 
A company is transitioning their systems to AWS due to the limitations of their on-premises data center. As part of this project, a developer was assigned to build a brand new serverless architecture in AWS, which will be composed of AWS Lambda, API Gateway, and DynamoDB in a single stack. She needs a simple and reliable framework that will allow her to share configuration such as memory and timeouts between resources and deploy all related resources together as a single, versioned entity.

Which of the following is the MOST appropriate service that the developer should use in this scenario?

#### do
AWS SAM
#### dont
AWS Systems Manager
AWS CloudFormation
Serverless Application Framework
#### info


### 
You are developing a high-traffic online stocks trading application, which will be hosted in an ECS Cluster and will be accessed by thousands of investors for intraday stocks trading. Each task of the cluster should be evenly placed across multiple Availability Zones to avoid any service disruptions.

Which of the following is the MOST suitable placementStrategy configuration that you should use in your task definition?
#### do

"placementStrategy": [
{
"field": "attribute:ecs.availability-zone",
"type": "spread"
}
]

#### dont
"placementStrategy": [
{
"field": "instanceId",
"type": "spread"
}
]



"placementStrategy": [
{
"field": "memory",
"type": "binpack"
}
]



"placementStrategy": [
{
"type": "random"
}
]


#### info


### 
You are working as an IT Consultant for a top investment bank in Europe which uses several serverless applications in their AWS account. They just launched a new API Gateway service with a Lambda proxy integration and you were instructed to test out the new API. However, you are getting a Connection refused error whenever you use this Invoke URL http://779protaw8.execute-api.us-east-1.amazonaws.com/tutorialsdojo/ of the API Gateway.

Which of the following is the MOST likely cause of this issue?
#### do
You are not using HTTPS in invoking the API.
#### dont
You are not using WebSocket in invoking the API.
You are not using FTP in invoking the API.
You are not using HTTP/2 in invoking the API.
#### info
API Gateway only supports HTTPS.


### 
A company operates an e-commerce website on Amazon Elastic Container Service (ECS) behind an Application Load Balancer (ALB). They’ve set their ALB as an origin for an Amazon CloudFront distribution. Users interact with the website via a custom domain linked to the CloudFront distribution, all maintained within a public hosted zone in Amazon Route 53.

The company wants to display region-specific pricing tables to its users. For example, when a user from the UK visits the site, they should be redirected to https://tutorialsdojo.com/uk/, while users from the Philippines should view prices on https://tutorialsdojo.com/ph/
#### do
Implement a CloudFront function that returns the appropriate URL based on the CloudFront-Viewer-Country. Configure the distribution to trigger the function on Viewer request events.
#### dont
Configure the Route 53 record to use the geolocation routing policy.
Forward the CloudFront-Viewer-Address header to the web server running on the ECS cluster. Implement a custom logic that matches the header’s value against a GeoIP database to determine user location. Based on the resolved location, redirect users to the appropriate region-specific URL.
Use AWS Web Application Firewall (WAF's) geo-matching rule to identify the user country and attach it to the ALB. Configure ALB listener rules with path conditions to route traffic based on the identified country.
#### info
 - Route 53 geolocation routing policy : for directing traffic to specific resources based on user location for performance or regulatory reasons, not for content personalization based on geolocation.

### 
A company has a development team that’s heavily relying on AWS CodeCommit, CodeBuild, and CodeDeploy. The management would like to further automate its CI/CD process. They requested a system that monitors the status of each code change, from the moment it’s committed through to its deployment.

Which of the following AWS services will help you achieve this?

#### do
AWS CodePipeline
#### dont
Amazon CodeGuru
AWS Elastic Beanstalk
AWS Fault Injection Simulator
#### info
 - Amazon CodeGuru :  detect potential defects in Java and Python code that are difficult for developers to find, analyzes the application runtime profile to identify the most expensive lines of code
 - AWS CodePipeline : continuous delivery service that automates the steps required to release software changes continuously


## Troubleshooting + Optimization



### 
#### do
#### dont
#### info
