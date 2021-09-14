# System Design: A framework

### Goal:
Demonstrate knowlege about modern end to end Software Architecture and Design 

### Key Areas:
#### 1. Databases
SQL vs NoSQL
When to use one over the other, why?

##### ACID principals
* Atomicity - either all transaction succeeds or none of it does
* Consistency - all data will be valid all of the time 
* Isolation - all transactions isolated from each other, one cannot be affected by another in progress
* Durability - transactions are permanent once committed
All big relational DBs are ACID
NoSQL prioritize availibility which comprimises consistency or durability
some noSQL DBs are ACID compliant

##### SQL
What relationships are important which aren't, why?
Create a simple ER Diagram to show table layouts
Good for structured unchanging data
Good if you need ACID compliance
1. Atomic Values - cannot be divided
2. All vals in column have same data type
3. each row uinique
4. column/row sequence is insignificant
5. columns have unique names
6. [Integrity constraints](https://www.javatpoint.com/dbms-integrity-constraints) maintain consitancy
* Domain Constraint - str, int, time etc - data has types
* Entity Integrity - primary keys cant be null
* Referential Intgrity - foreign keys cant be null
* key constraint - keys must be unique
##### NoSQL
no schema
store process analize large amounts unstructured data
normalization not needed
better for distributed comnputing, scalability, cost, 
good for unstructured and semi structured data
good if you need scalability

#### 2. Architecture
Microservices vs Monolith
Most often microservices

#### 3. Cacheing
server accessing database to pull results
use cases:
1. Save network calls
    * 1 user accessing another profile multiple times
    * save in server memory recently accessed profiles
    * check server cache before calling DB

2. Avoinding computations
    * if need to take avg of many vals in DB
    * Do 1 time store in server cache, reuse value
##### Cache policy - when to load and remove data from cahce
1. LRU - least recently used
* a stack, push onto the top pop off the bottom
2. LFU - least frequently used
##### Consitantcy
if server A caches profile
then server B updates profile
server A's cache becomes out of date
Solution: Global redis cache not in memory of a single server
more accurate but a little slower
independently scalable
##### Write Through vs Write Back
Write Through
* write a change to the cache
* then write change to DB
* worse for consistancy
Write Back - only option for critical data
* Write to DB
* delete entry in cache if exists
* worse for performance - increaces DB calls
Hybrid
Non critical data
Use write through 
every min or so batch all changes to DB into 1 network call


## 1. Define requirements + features
Write requirements + features when hearing question for first time 
Ask questions to further define requirements

### 1.1 State Assumptions
Make clear to your interviewer thigns that you assume
ex I'm assuming that there is a seperate payment service that exists 

## 2. Identify key components
usually [Front End] -> [Web Server] -> [DataBase] 
Go into details of each component throughout interview

## 3 Key Components - DB
List the big entities, relationships between if applicable
With big entities, key attributes of components 
Talk about SQL vs noSQL

## 4 API - How will data be served
3 main parts 
Domain, Resource, Params
1. State a use case
2. State Domain
    * HTTP POST, GET, PUSH, DELETE, etc
    * Try to cover all if warranted to demonstrate knowlege
3. Resource
    * list url xyz.com/action
4. Params - JSON object - if needed
    * POST - Describe the obj you are adding to the database

## 6 Front end
Describe landing page and functionality offered 
Discuss how the functionality on landing page is connected with back end and db
trace some calls through system and back to get on new page and diagram that page too ie serach results page
Search box + button
buton calls search svc
search svc looks in search DB
search svc calls books svc to get books
search svc returns list of books as search results
diagram search results screen




