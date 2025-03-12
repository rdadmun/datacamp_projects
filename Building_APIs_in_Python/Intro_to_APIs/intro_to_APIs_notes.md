# Building Web APIs in Python
# What is an API?
    Stands for Application Programming Interface
        Sets communication rules and capabilities for two systems to communicate with each other. 
        Systems can interact with each other to exchange or manipulate data. 
            Clicking send on an email tells the email server to use an API to send the message to the reciepient. 
        We will focus on Web APIs
            Web APIs are used to enable communication between two software applications over a network or the internet.
            This communication uses the HTTP protocol
                Sends a request message to a server
                ther server returns a response message to the client
        3 most common kind of Web APIs
            SOAP
                Focus on strict and formal API design
                Most commonly used in enterprise applications
            REST
                Focus on simplicity and scalability
                Most common API architecture
            GraphQL
                Takes a more sophisticated approach, focus on flexibility, minimizing data transfer and optomized for performance. 
    Two well known Python libraries for integrating Web APIs - wrllib and requests
        urllib
            Bundled with Python, Powerful but not developer friendly
        requests
            Offers many powerful buiolt in features, and is easier to use. 

# The basic anatomy of an API request
    URL = Uniform Resource Locator
    They are the structured address to an API resource
    Customize the URl to interact with specific API resources
        As an example, we will compare a REST API to an office building, where each office unit is a unique resource. The URL contains all the information to navigate to a specific unit within the building. 
    URls can be broken down into 5 main components:
        http:// -> Protocol - the means of transportation
        350.5th-ave.com -> Domain - the street address of the office building
        :80 -> Port - gateway or door into the building
        /unit/243 -> Path - the specific office unit
        ?floor=77 -> Query - additional instructions
    Although we could pass the entire URL to the requests.get(), there is a better way:
        Each HTTP method from the requests package accepts an additional argument called 'params'
            'params' is a dictionary of key/value paris , one for each query parameter
    Request Actions
        GET -> Read action - Check the mailbox contents
        POST -> Create action - drop a new package in the mailbox
        PUT -> Update action - replace all packages with a new one
        DELETE -> delete action - removes all packages from the mailbox

# Headers and Status Codes
    What if we want to give the server extra instructions?
    Or check that the server properly handeled our request?
        Examining a GET request and the response message, we see both messages are similar, and can be split into 3 distinct parts:
            START LINE -> contains the request type such as GET, POST etc., aloong with the path where the return messages should be delivered. In the return message, this includes a status code (numeric)
                There are over 70 status codes in general, grouped into 5 categories:
                    1XX - Informational responses
                    2XX - Successful responses - 200 OK
                    3XX - Redirection responses
                    4XX - Client Error responses - 404 Not Found
                    5XX - Server Error responses - 500 Internal Server Error
            Next we have the Header bracket. Headers contain information that described the message or data whcih is being sent or recieved, like the type of content we are sending or the date the requested resource was last modified. 
                Always formatted as key-value pairs separated by a colon.
                Each header stats with a case-sensitive key, colon, then value of the header.
                In order to effectively communicate, client and server use message headers to agree on the language they are using to exchange information (dtype).
                    This is content negotiation
                    Using requests, we create a dictionary called 'header', with key/value parirs to add additional instructions. 
            Requests also simplifies how we get the status codes from a response. 
                Requests has a built in search method for status codes. 
                    By chaining the status-message to the requests.codes object, 
# API Authentication
    APIs we interact with frequently contain private, personal or sensitive data. 
    To protect this, APIs require clients to authenticate before granting access. 
        Trying to access APIs which demand authentication results ina 401 error. 
        When we add information to the request to ID ourselves, the server can give us the OK. 
    Common ways to add authentication information:
        Basic Authentication -> The simplest form, using a username and password. Easy to integrate and the least secure, as it sends your password unencrypted over the internet to the server. 
        API key or Token -> attaches a unique authentication key to each request. API keys are simmple to implement but posr a security risk if compromised, as they also transmit unencrypted data. 
            Simialr - JWT or JSON token - JWTs only have a limited lifespan and can contain additional encrypted data such as user information. 
        OAuth 2.0 is a comprehensive authentication framework that allows fine-grain access to resources without credentials. 
    ## Basic Authentication
        To use, we need to add a authorization header to the request within the API. The header must contain a base65-encoded combination of our username and password. Base64 is a two-way algorithm that anyone can decode. 
            Implementation of basic authorization is easy, as you just pass a tuple containing the username and password using the auth_function argument, and requests takes care of the encoding before adding the header. 
    ## API keys / token authentication
        There are two common options to add the authentication token to our request. 
            1. Simply adding the API key to the URL as a query parameter. 
            2. Adding an authorization header (usually preferred). Requests package doesn't offer an out of the box method like Basic, so we need to add the header ourselves.

# Working with Structured Data
    This lesson is focused on how to handle API requests for more complex data structures other than strings
    We have a few handy data formats to make working with structured data easier:
        JSON - Javascript Object Notation
            Most common, and very lightweight format used by WebAPIs
            Natively supported and readable by humans and machines.
                One of many types we call content types, mime-types or media-types
                    Other options include XML, CSV and YAML
            In order to use a Python Object with WebAPIs, we need to convert it to a JSON string to transmit, then decode it on the other end. 
                Python's built in json package can do this -> json.dumps(album) = encode; json.loads(string) = decode

# Error Handeling
    When integrating with a web API, it is important to consider what might go wrong. 
    To determiune if an error has occured or if the request was successful, REST APIs use the status_code object in the response. 
        4XX and 5XX indicate errors. 
            4XX are client errors, indicating the request from the client could not bbe handeled properly. These can be fixed by editing the request.
                401 - Unauthorized
                404 - Not Found
                429 - Too Many Requests - spread out requests
            5XX errors indicate server problems. These are beyonf the client's control, and are typically caused by server overload or configuration errors. 
                500 - Catch all server error
                502 - Bad Gateway
                504 - Gateway Timeout
        We can check API errors through the response.status_code. However, an error can occur even before the request reachers the server, meaning we would not recieve and error code. 
            Requestsd library will raise a ConnectionError in this case, which we can check using a try/except block.
