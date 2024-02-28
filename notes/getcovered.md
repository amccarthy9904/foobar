$110K-$150K

REST vs SOAP APIs

Authentication
OAuth
JWT

testing:
1 off REST test use cURL
make a collection of test in Postman
or in Python
i want to try Rabbittrace


to talk about:

VirusScanner
Designed + devloped by me + conffering with Tien
Java RabbitMQ virus scanning service
Created testing suite in Java

Vino
Problem: Morpheus does not maintain server ID,s
chrl-clust-4-server-5 will be a different server depending on the day of the week
I created python software to pull server info from Morpheus API
push into Vino's data storeage solution via its API
then a client software to pull from up to date info from Vino
didnt except raw JSON, needed to add each field individually
needed to dfs through the json structure of every serve cluster env site
change all lists if lists into lists of dictionaries w/ 1 key : value []
the dfs again on retrival and convert back intp regular JSON
this put a strain on Vino's data storeage solution
started to chug pretty hard
to optimize i fugured out how to convert JSON into a single string 
and those long strings could be storesd as a single object in vino
no longer user readable
but performant
and output of client side was regular readable json

Cake
problem: Hardeen is slow and unreliable
we need to get servers from customer unconfigured and back into general morpheus pool
Spark is here, allows for event driven hardeen
we create a connection to Sparks event queue
when a server pops up as needeing to be reintroduced to the pool we can know immeditaly
made a commissioner that recieves events from docker
makes a decision as to what to do
publish task to queue
worker picks up the task - different docker container
initializes the task
doesnt need to wait around 
once task is finished, commissioner will know, start the next task
highly scalable design 




1. Design and develop scalable, secure, and well-documented APIs using modern programming languages and frameworks.
2. Collaborate closely with product managers, software architects, and other engineering teams to identify API requirements and design appropriate solutions.
3. Conduct thorough testing, debugging, and troubleshooting to ensure the reliability and robustness of APIs.
4. Optimize API performance, throughput, and scalability to meet growing demand.
5. Implement security standards and protocols to protect APIs and sensitive data.
6. Integrate APIs with various platforms, systems, and third-party applications.
7. Continuously monitor, evaluate, and enhance the performance and functionality of existing APIs.
8. Work closely with the Quality Assurance team to develop and execute comprehensive API testing strategies.
9. Stay updated with industry trends, emerging technologies, and advancements in API development to propose innovative solutions.
10. Provide technical guidance and support to junior engineers and team members.
11. Document API specifications, design patterns, and standard methodologies.

Requirements:
4. Solid understanding of RESTful and SOAP-based API concepts, principles, and best practices.
5. Experience with API testing tools and frameworks.
6. Strong knowledge of authentication, authorization, and security protocols (e.g., OAuth, JWT).
7. Familiarity with database technologies and the ability to design data models and integrate APIs with databases.
8. Experience with version control systems (e.g., Git) and continuous integration/continuous deployment (CI/CD) pipelines.
9. Ability to identify and resolve performance bottlenecks and scalability challenges.

12. Experience working in an Agile development environment is a plus.





What upcoming projects or initiatives is the engineering team excited about?

How is feedback typically provided, and is there a formal performance review process?

What are the next steps in the interview process, and what is the expected timeline for a decision?

saas for property management
3 things for them
- tracking insurances of tenents - notifies tenets if they need to do stuff
- provide insturance for tenants
- blanket insurance for property

API work
10ks of tenants buying insurance get data addresses from them
emailing many tenants
100s of properties pre company


AWS databases
Ruby
favio
Angular
REST
