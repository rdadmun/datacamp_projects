# What is Fast API
    Qpplication Programming Interface - in internet jargon, it refers to web applicaitions using the HTTP protocol to transmit structured data.
    Key Features:
        Very high performance and is one of the fastest available. 
        Low code, and easy to learn. 
        Leverages Python annotations and type hints to make coding APIs almost identical to Python functions. 
        Robust - builds production ready code with automatic interactive features. 
        Standards-based: based on and fully compatible with open standards for APIs: OpenAPI and JSON schema. 
    VS other python frameworks:
        Flask and Django are also web framework,s, but are designed for web-based GUI apps instead of APIs
        Difference between Falsk and Django is that Django has built in Object-Relational Mapping (ORM)
        ORM is a software thay represents database models as Python objects. 
        FastAPI and Flask do not have built-in ORMs
        FastAPIs key difference is that it's designed for APIs without database operations, which can hurt API performance. 
            Great framework for high-throughput data and ML operations. 
    First Web App
        FastAPI is very simple to get up and running.
            Install the fastapi module in terminal with pip
            Create the main.py file (see main.py)
            run the file with "fastapi dev main.py"
    Some notes prior to practicing 
        We can't run the FastAPI server like we run Python scripts with a run button. Instead, we will define our server code in the Python editor as "main.py", and run it in the terminal with the command "fastapi dev main.py"
        Alwasy verify that the logs in the terminal show "Application startup complete" before pushing live. 
        You can close the terminal by pushing Ctrl+C in the same terminal.

# Get Operations
    How to use FastAPI to handle HTTP GET requests that accept data input
    Get is the most common HTTP operation.
        Designed to retrieve information rather than send, update or delete. 
        Going to a website is a GET request

    Handleing a GET request with FastAPI is easy!
        We import the FastAPI module at the top with "from fastapi import FastAPI"
        Then, we instantiate our app on the next line as an instance of the class FastAPI
        The last part tells the app the handle the GET requests to root, which is either the host alone or the host followed by a single /
        Then, we provide a function called "root()" that returns the response. 
        The application responds to requests to root by sending back a static dictionary with the key "message" and the value "Hello World"
            FastAPI encodes this dictionary as JSON
    
# POST Operations
    The difference between GET and POST
        1. Tranditional use of a GET operation is to request information about an object, while a POSR operation is to create a new object. 
        2. GET request parameters should only be sent via the URL query string, while POST request parameters can also be sent via the request bost. 
            The important thing to remember for now is that POST requests can send a great deal more information to the server than GET requests can.
        3. Get requests can be typed into the URL bar of a browser, but POST requests require an application or framework like cURL or Python's requests.

    HTTP request body
        Both HTTP requests and responses can include a message body, which is the data sent after the HTTP header.
            Headers specify the body encoding, which tells the application how to decode the data correctly, meaning the request bodies support nested data strcutures.
                JSON and XML are the most common encodings for APIs.
                We will use JSON since this is Fast APIs default encodings. 

    Using PyDantic's BaseModel
        Since HTTP request bodeis support nested data structures, we need more than just type hints to define a message body for a POST request. 
        Python's pydantic library is designed to generate and manage nested model schemas. Pydantic model schema consist of a named model with named and typed attributes, which inherit from the pydantic BaseModel class. 
        Using pydantic, we can define a model schema for the movie review record. A Review has an int num_stars, free text and a boolean for public status. Since Pydantic models follow standard type hint practices, we specify =False to make the last attribute optional, default False. 
            MovieReview consists  of a movie string and a reference to a Review. Notice we are nesting Review inside MovieReview to get the nested body structure of the movie reviews. This helps us keep our models well-organized, and add attributes to a Review without changing the model and vice-versa. 

# Chapter 2
## PUT and DELETE operations
    PUT and DELETE are used to update or delete existing objects. Like POST operations, they accept parameters from both the the query string and the request body. They also require an application or framework to send or recieve requests. 

    Referencing Existing Objects
        Referencing existing objects is the most important concept to understand when using PUT or DELETE operations. 
        Frameworks with a built in ORM handle this mapping automatically, but FastAPI does not have built-in ORM.
        It is the applications responsibility to map API requests to objects it manages. Typically, this means mapping a parameter to the ID or other unique column of a database table.  It is common practice to include the name of the column in the parameter name. 
            For example, we might name a parameter review_id to indicate tthat it is the ID column of the table called reviews, as we can see in a pydantic model for DbReview that includes review_id as the last attribute. The same convention is used in many frameworks with a built-in ORM, and is very familair to API developers and users alike. 
    Handeling a PUT Operation
        Let's make a PUT endpoint to update an existing movei review. The endpoint is called 'reviews'. We use the @app.put annotation to tell FastAPI that this is a PUT operation. We follow it with a function `update_review` that defines the input and output types. Both are the pydantic model for DbReview objects that we defined previously, which includews the db identifier for the data to be updated.
        the function `update_review` updates the review data in the db and returns the same model. 
    Handeling a DELETE Operation. 
        Let's make a DELETE endpoint to delete an existing movie review. The endpoint is again called `reviews`, and accepts the DbReview model as the request body. Recall that the DbReview model includes the db identifier for the data to be deleted. We use `@app.delete` annotation to tell FastAPI this is a DELETE operation. We follow it with a function delete_review, which deletes the review data from a database. The DELETE endpoint returns no data, since at the end of the operation the object is gone. 

# Handeling Errors
    There are two main reasons for errors. First errors caused by users of the API. This includes using an invalid or outdated URI or missing or incorrect input. 
        For example, an API user could request to delete an object that doesn't exist. In this case, we check if we have the item and respond with an error if we don't/ 
    The other main reason for errors is server error. These happen when something unexpectedly goes wrong.
        For example, the app could get an exception when trying to delete an object. In this case we wrap our code in a try block and respond with an error when there is an Exception. 

# USing async for concurrent work
    Why would we use async?
        We see two people waiting at a restaurant where every cashier prepares every order they take. This would be sequential burgers. We would have to wait at the counter a long time, since each worker completes every step individually.
        With Concurrent burgers, most of the workers are in the kitchen doing different jobs to make the burgers, so we don't wait as long. 
        Async can be used to help our API server requests concurrently and spend less time waiting for work to be done.
    What does async look like in practice?
        At the sequential burger restaurant, workers can't share jobs in the kitchen. 
            In Python, this is equivalent to defining a function with def and calling it in the normal way.
        To serve concurrent burgewrs using Python, we define a function with async def, and we call it using await. This tells Python that the code is safe to run in the background and wait until its finished for a response, freeing up Python to do more work. 
    FastAPI with async
        Async is quite easy with FastAPI.
            If we can call all the external functions in our endpoint definition using await, then we can define our endpoint function with async def. 
            Importantly, we should only ever use await inside of functions created with async def. 
    When to use async
        Short answer: we should use async if our application doesn't have to communicate with anything else and wait for it to respond. This is true in many instances of data processing, and it is especially helpful when it requires lots of computation that can take a long time to finish. 
            Examples: audio or imaging processing, computer vision, machine learning and deep learning. 
        We should not use async when our application must communicate in sync with other systems, like a file system, database, or another server. We should also not use async whenever we are nor sure we can. 
    
# Chapter 3
   # FastAPI automated testing
    Learn how to test your endpoints automatically
    What are animated tests?
        There are two kinds of automated tests we can build with FastAPI
            Unit Tests
                Unit tests focus on isolated code
            System Tests
                System tests focus on an isolated system operations.
        This means that unit tests are designed to validate how specific units of code function, whereas system tests arte designed to validate specific parts of the system functions.
            All unit tests are scoped to a function or method.
            System tests are scoped to an endpoint or other specific parts of the application.
            Technically, there is only one very important difference between the two kinds of test. 
                To run unit tests, you need only an isolated Python environment with necessary dependenccies. 
                To run system tests, you need a Python env with accrss to the running application. 
    Using TestClient
        FastAPI lets us write automated system tests just like unit tests. To enable this, the TestClients class lets pytest call the running API and validate its responses.
        In our system tests, we can import TestClients from fastapi.testclient and import our app from main.py, the local file that defines our server. 
        Then, we can create a client object with the application context by passing in the app. Each of our system tests can use the client to call endpoints in our running application and validate any aspect of the full H TTP response. 
    Testing Error vs Failure Response
        How do we test error or failure responses from our app with system tests?
            Unlike unity tests, where we have to catch an exception, FastAPI system tests let us test error or failure responses just like success responses, by validating the HTTP status code and response body.
                Having a delete item endpoint that we defined to send a 404 status code and an item nor found message when the item does not exist. 
                With system testing, we can test this endpoint just as we would for a successful response. 

# Building a JSON CRUD API
    The four steps in Object Management Lifecycle
        When we manage objects in a DB, there are 4 steps. 
            We create objects, then we can read and update them whenever we want.
            Once we delete an object, it's lifecycle is over.
            Translating this lifecycle into API operations is easy, since the HTTP protocol specifies what operations should be used for each step. 
                We create objects with the POST operation. We read objects with the GET operation, and update objects with PUT operations. 
                With our four lifecycle steps tied to these API commands, we can build a FASTAPI application to manage database objects following the HTTP protocol. 
    JSON CRUD API Motivation
        Why would wwe want to learn a JSON CRUD API. We want to learn important fundamentals. These include managing the entire object lifecycle above, and understnad best practices for HTTP operations. Understanding these makes us ready to design our own APIs right away, allowing us to pursue more advanced opportunities. These include injecting business logic operations and building high throughput data and ML pipelines.
    Building a CRUD module
        To make it easier to manage database operations from API endpoints, it's common practice to build a CRUD module. Let's assume we have 2 defined pydantic models for a movie review. 
            The model DbReview has an additional database identifier for update and delete. 
            We can build a module in a file called crud.py with methods that handle the four types of operations based on input from the models. 
            Creating a review takes a Review without a DbId and creates the review in the database. 
            Read review only needs a review ID to read the record from the Db. 
            Update review needs a DbReview with a database identifier to update the review.
            Delete simply needs the review ID.
                With a CRUD module in place, it will be simple to build our CRUD API. 
    POST Endpoint to Create
        A POST endpoint to create a movie review accepts a Review Object, calls the CRUD module to perform the operatin, and returns a DbReview object with a DbId.
    GET Endpoint to Read
        GET endpoints are not supposed to accept request bodies, so a GET endpoint to read a movie reviw can only accept parameters from the URL string. But we can still accept review ID as a URL parameter as we have learned. Then we can call the CRUD module to read the review from the database and return the DbReview object. 
    PUT Endpoint to Update
        A PUT endpoint to update a movie review accepts a DbReview object, calls the CRUD module to update the review in the db, and returns a DbReview object. 
    DELETE Endpoint to Delete
        Accepts a DbReview object, calls the CRUD module to delete the review from the database, and returns an empty dictionary since the object is gone. 
         