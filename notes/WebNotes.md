
## TCP Transmission Control Protocol

## IP INternet Protocol

## DNS Domain Name Servers

## HTTP HypertextTransferProtocol

## Component Files

### Code Files

### Assets

How Your Browser Finds Websites
# The Process
## 1. Find the IP of the Webserver that is hosting the website we want
### DNS Resolution
Browser uses URL to ask for IP address from DNS server
#### Local Cache
Broswers keep a local cache of {url : IPs}
If it is not found it checks the OS's cache.
If IP is not found locally, Must ask DNS Server
#### Recursive DNS Server
Servers run by the ISP
Big URL caches, capable of asking other Recursive DNS Servers for URLs
#### Root DNS Servers
Request for IP hits Root Name Servers, which re-direct to correct Top Level DNS Servers
#### Top Level DNS Servers 
Top Level DNS Servers associated with a url suffix ie .com, .org, .io
The Top Level Server will know who to ask to get the IP
Sends request to the Authoritative DNS Server that knows
#### Authoritative DNS Servers
This is where you register a domain
They keep the DNS Records / IP address we want
#### DNS Records
##### A Records
Point to IPv4 address
##### AAAAA
Point to IPv6 address
##### CNAME records
Used to make links between a subdomain and a root domain.
One CNAME record could redirect you from blog.example.com to example.com
Not the other way around
##### DNAME Records
Links every subdomain on one to main to the same subdomain of another
```
<sub_domain>.ex.com -redirects to> <sub_domain>.ample.com - for any <sub_domain>
```
##### ALIAS Record
Links 2 A Records
ex.com -redirects to> ample.com
##### CERT Record
Stores Certificates in DNS
There are many others
##### MX Records
Mail eXchange records
Handles emails sent to domain
##### TTL Time To Live
DNS records have expiration dates ranging from hours to minutes
When making a DNS change set all effected recods to a small TTL, 
wait for curernt records to expire
Update the Records and set to regular TTL
ensures DNS records update fast
## 2. Use the IP to send a request to the serer hosting the website

### HTTP Methods
1. 	GET - The GET method is used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.
2. 	HEAD - Same as GET, but it transfers the status line and the header section only.
3. 	POST - A POST request is used to send data to the server, for example, customer information, file upload, etc. using HTML forms.
4. 	PUT - Replaces all the current representations of the target resource with the uploaded content.
5. 	DELETE - Removes all the current representations of the target resource given by URI.
6. 	CONNECT - Establishes a tunnel to the server identified by a given URI.
7. 	OPTIONS - Describe the communication options for the target resource.
8. 	TRACE - Performs a message loop back test along with the path to the target resource.

### HTTP Requests
3 main parts request line, header, and body

#### Request Line
Tells the recipient the HTTP-Method, URI, HTTP-PROTOCOL version
ex. GET /api/authors HTTP/1.1
GET is the Http Method we are requesting a resource
The resource we want is /api/authors
And we are using HTTP/1.1

#### Request Header
Contains metadata about the request
* Accept - What filetypes are acceptable as a response - text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
* Host - The domain of the server - pizza.com
* Connection - if the connection should stay open after current transaction finishes - keep-alive
  
#### Request Body (optional)
Section to put whatever you want in
Not used very much with GET requests
Used more for POST to describe data to give to the web Server
ie 
```
POST /api/authors HTTP/1.1
Host: myWebApi.com
Content-Type: application/json
Cache-Control: no-cache

{
     "Name": "Felipe Gavilán",
     "Age": 999
}
```
### HTTP Response
Same structure as Request - request line, header, and body
#### Status Code
resides in request Line
1 digit in 3 digit code catagorizes response
1. 	1xx: Informational - request was received and the process is continuing.
2. 	2xx: Success - action was successfully received, understood, and accepted.
3. 	3xx: Redirection - further action must be taken in order to complete the request.
4. 	4xx: Client Error - request contains incorrect syntax or cannot be fulfilled.
5. 	5xx: Server Error - server failed to fulfill an apparently valid request.
ex
```
Request Line:
    HTTP/1.1 200 OK
Header:
    Date: Thu, 03 Jan 2019 23:26:07 GMT
    Server: gws
    Accept-Ranges: bytes
    Content-Length: 68894
    Content-Type: text/html; charset=UTF-8
Body:
    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
```







