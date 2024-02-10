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


#### AWS DB offerings

- Amazon RDS
    - relational database services
    - MySQL, PostgreSQL, MariaDB, Oracle, and Microsoft SQL Server
- Amazon Dynamo DB
    - A fully managed NoSQL database service.
    - Designed for high-performance, low-latency applications.
    - Supports both document and key-value data models.
- Amazon DocumentDB
    - fully managed document database service compatible with MongoDB.
    - scales and provides high availability for document-oriented applications.
- Amazon ElastiCache
    - in-memory data store service
    - Redis and Memcached, providing a caching layer for improved performance.
- Amazon Timestream
    - A fully managed, serverless time-series database.
    - Optimized for IoT and operational applications that generate high volumes of time-stamped data.