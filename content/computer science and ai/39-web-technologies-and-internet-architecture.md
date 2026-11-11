---
title: Web Technologies and Internet Architecture
level: intermediate
---

Web technologies are the tools, protocols, programming languages, and software systems used to create and operate websites and web applications. Understanding web architecture explains how browsers, servers, databases, and network protocols work together.

## 1. Understanding the World Wide Web

The World Wide Web is a system of interconnected resources accessed through the internet.

It allows users to access:

- Websites.
- Web applications.
- Documents.
- Images.
- Videos.
- Online services.

The internet is the underlying global network infrastructure, while the World Wide Web is one of the services that operates over it.

## 2. Client and Server Architecture

Web applications commonly use a client-server model.

### Client

The client is the application that requests services.

A web browser is a common client.

Examples:
- Google Chrome.
- Mozilla Firefox.
- Microsoft Edge.
- Safari.

### Server

A server receives requests and provides responses.

It may:
- Deliver web pages.
- Process application logic.
- Authenticate users.
- Access databases.
- Provide APIs.
- Store uploaded information.

## 3. How a Web Request Works

A simplified web communication process is:

1. A user enters a website address.
2. The browser identifies the required server.
3. DNS resolution obtains the relevant network address.
4. The browser establishes the required network connection.
5. An HTTP or HTTPS request is sent.
6. The server processes the request.
7. The server returns a response.
8. The browser interprets the response and displays the page.

Real web communication may involve additional steps such as proxies, caching, redirects, and content delivery networks.

## 4. HTML

HTML stands for HyperText Markup Language.

It defines the structure and content of web pages.

Common HTML elements include:

- Headings.
- Paragraphs.
- Links.
- Images.
- Tables.
- Forms.
- Lists.

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>This is a web page.</p>
</body>
</html>
```

HTML describes page structure rather than application styling or general-purpose program logic.

## 5. CSS

CSS stands for Cascading Style Sheets.

It controls the visual presentation of web pages.

CSS properties can control:

- Colours.
- Fonts.
- Spacing.
- Borders.
- Layout.
- Animations.
- Responsive behaviour.

Example:

```css
body {
    font-family: Arial, sans-serif;
    background-color: lightgray;
}

h1 {
    color: navy;
}
```

CSS separates presentation from the underlying document structure.

## 6. JavaScript

JavaScript is a programming language widely used to add behaviour and interactivity to websites.

It can:

- Respond to user actions.
- Validate forms.
- Update page content.
- Communicate with APIs.
- Manage application state.
- Create interactive interfaces.

Example:

```javascript
const button = document.querySelector("button");

button.addEventListener("click", function () {
    alert("Welcome!");
});
```

JavaScript can execute in browsers and in server-side environments such as Node.js.

## 7. Frontend and Backend

### Frontend

The frontend is the part of an application through which users interact.

It commonly includes:
- HTML.
- CSS.
- JavaScript.
- Frontend frameworks.

### Backend

The backend handles server-side processing.

It may include:
- Authentication.
- Business logic.
- Database operations.
- API endpoints.
- Security checks.
- Application configuration.

Common backend technologies include Python, Java, JavaScript, PHP, and C#.

## 8. HTTP and HTTPS

HTTP stands for HyperText Transfer Protocol.

It defines how clients and servers exchange web requests and responses.

HTTPS is HTTP protected using TLS.

TLS provides cryptographic protection for communication, including encryption and server authentication.

HTTPS is important for protecting sensitive information transmitted over networks.

## 9. HTTP Request Methods

Common HTTP methods include:

| Method | Purpose |
| --- | --- |
| GET | Retrieves a resource |
| POST | Submits information or requests processing |
| PUT | Replaces a resource representation |
| PATCH | Partially modifies a resource |
| DELETE | Requests deletion of a resource |

The exact behaviour depends on the server implementation and API design.

## 10. HTTP Status Codes

Status codes indicate the outcome of an HTTP request.

| Code Range | Meaning |
| --- | --- |
| 1xx | Informational |
| 2xx | Successful |
| 3xx | Redirection |
| 4xx | Client error |
| 5xx | Server error |

Examples:

- 200: OK.
- 201: Created.
- 301: Moved Permanently.
- 400: Bad Request.
- 401: Unauthorized.
- 403: Forbidden.
- 404: Not Found.
- 500: Internal Server Error.

## 11. APIs

API stands for Application Programming Interface.

An API defines how software components communicate with one another.

A web API allows an application to request information or services from another application through a network.

Examples include:
- Weather data services.
- Payment services.
- Authentication services.
- Mapping services.
- Database-backed application services.

## 12. REST Architecture

REST stands for Representational State Transfer.

It is an architectural style for designing networked applications.

Common REST principles include:

- Client-server separation.
- Stateless communication.
- Cacheable responses where appropriate.
- Uniform interfaces.
- Layered architecture.

RESTful APIs commonly represent resources through URLs and use HTTP methods to interact with them.

## 13. JSON in Web Applications

JSON is a common format for exchanging structured information.

Example:

```json
{
    "student_id": 101,
    "name": "Asha",
    "completed": true
}
```

A client may send JSON to a server, and the server may return JSON as a response.

## 14. Cookies and Sessions

### Cookies

Cookies are small pieces of information stored by a browser and associated with a website.

They may be used for:

- Session identifiers.
- Preferences.
- Certain authentication-related functions.
- Analytics.

### Sessions

A session represents a period of interaction between a user and an application.

Server-side session systems commonly associate stored session information with a session identifier held by the client.

Secure cookie settings are important when sessions contain authentication-related identifiers.

## 15. Web Hosting and Deployment

Web hosting makes an application accessible through a network.

Common deployment components include:

- Application server.
- Web server or reverse proxy.
- Database.
- Domain name.
- DNS configuration.
- TLS certificate.
- Environment variables.
- Static file storage.

Cloud platforms can simplify hosting and deployment by providing managed infrastructure.

## 16. Web Security Fundamentals

Important web security practices include:

- Validate input on the server.
- Use parameterized database queries.
- Protect authentication credentials.
- Use HTTPS.
- Apply authorization checks.
- Secure session cookies.
- Prevent cross-site scripting.
- Protect against cross-site request forgery.
- Avoid exposing secret keys.
- Keep dependencies updated.

## Common Exam Traps

- The internet and the World Wide Web are not identical.
- HTML defines structure.
- CSS controls presentation.
- JavaScript adds programmable behaviour.
- Frontend code runs in the user's interface environment, while backend code handles server-side processing.
- HTTPS protects HTTP communication using TLS.
- GET is commonly used to retrieve resources.
- POST commonly submits information or requests processing.
- REST is an architectural style, not a programming language.
- JSON is a data-interchange format.

## Quiz

1. Which technology primarily defines the structure of a web page?
   - [ ] CSS
   - [ ] SQL
   - [x] HTML
   - [ ] DNS

   > HTML defines the structure and content of web documents.

2. Which protocol protects HTTP communication using TLS?
   - [ ] FTP
   - [ ] SMTP
   - [ ] UDP
   - [x] HTTPS

   > HTTPS uses TLS to protect web communication.

3. Which HTTP method is commonly used to retrieve a resource?
   - [ ] DELETE
   - [ ] PATCH
   - [x] GET
   - [ ] POST

   > GET is designed to retrieve a representation of a resource.