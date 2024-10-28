# API Reference for Communication Protocols

## Overview
The Celestrion Nexus API provides a set of endpoints and methods for facilitating communication between spacecraft and ground control, as well as among different spacecraft. This document outlines the key API components and their usage.

## Base URL

[https://api.celestrionnexus.org/v1](https://api.celestrionnexus.org/v1)


## Endpoints

### 1. Send Message 
- **Endpoint:** `/send_message`
- **Method:** POST
- **Description:** Sends a message to a specified recipient.
- **Request Body:**
```json
1 {
2  "recipient": "string",
3  "message": "string",
4  "timestamp": "ISO 8601 date string"
5 }
```

- **Response**:
  - 200 OK: Message sent successfully.
  - 400 Bad Request: Invalid input data.

### 2. Receive Messages
- **Endpoint**: /receive_messages
- **Method**: GET
- **Description**: Retrieves messages for the authenticated user.
- **Response**:
```json
1 {
2   "messages": [
3     {
4       "sender": "string",
5       "message": "string",
6       "timestamp": "ISO 8601 date string"
7     }
8   ]
9 }
```

### 3. Get Status
- **Endpoint**: /status
- **Method**: GET
- **Description**: Retrieves the current status of the communication system.
- **Response**:
```json
1 {
2   "status": "string",
3   "last_communication": "ISO 8601 date string"
4 }
```

## Error Handling
All API responses include an error code and message in case of failure. Common error codes include:

- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error

# Conclusion
This API reference provides the necessary information to interact with the Celestrion Nexus communication protocols. For further details, please refer to the source code and documentation in the repository.
