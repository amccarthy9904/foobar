# Online Book Store
Question:
Design an online book store
## 1. Define requirements + features
ask: What type of books
ans: Ebooks and regular books
write: ebooks, regular books
6 million users
500 trasanctions per second
Assume a payment system already exists

## 2. Identify key components
[Front End] -> [Web Server] -> [DataBase]
Front end for users to interact with
Web server to host the app and process orders
Database to store data on inventory etc

## 3 Key Components - DB
1. Customer
    * Name
    * ID
    * Address
2. Order
    * Transaction ID
    * Date
3. Books
    * ID
    * Author

## 4 API - How will data be served
Domain / Resource / Params
Use Case - Insert Book into table
D - HTTP Post
R - xyz.com/books/
P - {
    id:
    Author:
    Price:
}

## 5 Microservices
Using Microservice Architrecture to accomodate large volume 
horizontal scaleing and reliability is a concern
Micro Services:
* Order svc
* Payment svc
* Search svc
* Books svc

Define the relationships between the services + DB
Do they share a DB or do they each need their own DB?

## 6 Front End
sketch out landing page, with search button
connect search button with service design
Search button invokes the search API, passes user input as param
Search svc invokes Books svc to get books it wants 
Return Search obj back to browser
Diagram the search results page

# Tindr

## 1. Define requirements + features
1. Store Profiles
    * Images - num per user? 5
2. Recommend Matches
    * num active users? 
3. Store Matches
    * assume .1% chance to match per swipe
4. Direct Messaging

## 2. Identify key components
[Front End] -> [Web Server] -> [DataBase]

## 3 Key Components - DB

### 3.1 images
File vs BLOB (Binary Large Object)
BLOBs are inb a database and dont take advantage of DB properties (Mutability, indexes, Access Control)
File systems seems to be better for storing images
* Chaper, Faster
* profile_id : Image_id {path to file}
CDN allows fast access
in DB profile_id | image_id | File URL 

1. Customer
    * Name
    * ID
    * Address

## 4 API - How will data be served
Domain / Resource / Params
Use Case
D - HTTP Post
R - xyz.com/books/
P - {
    id:
    Author:
    Price:
}

## 5 Microservices
1. Profile Svc
* send usr, pass, update DB with user profile
* update profile, send images, w/ username
* Use tokens to ensure secure transactions
* This can get tedius as all services will need to talk to profile to verify authentication, Gateway solves this   

2. Gateway svc
[user] -> [gateway] -> [profile] -> [profileDB] 
* Sits in front of all other services
* asks Profile if requests are auth
* if authorized, directs to correct service, forwards response to user  

3. Image Service
[gateway] -> [image] -> [distributed file system]  
                     -> [imageDB]
* imageDB - 1 table - profile_id | image_id | File URL 
* Gets all images for a user profile

4. Messages + Session Service
* Dont want to poll the server, want messages to be pushed to you
* XMPP - Peer-to-Peer protocol
* Make a TCP (needed for sustained connections) connection with gateway
* need connection_id associated with one user_id
* SessionDB = connection_id | user_id


## 6 Front End