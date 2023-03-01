# API Client

API Client is a Python package for making HTTP requests to web APIs. It provides a simple interface for sending GET, POST, PUT, and DELETE requests, handling query parameters and request bodies, and parsing JSON responses. API Client is designed to be easy to use and to integrate with any Python project.

## Installation

API Client can be installed using pip:
```
pip install api-client
```

## Usage

Here's an example of how to use API Client to make a GET request:

```python
import api_client

base_url = "https://jsonplaceholder.typicode.com"
client = api_client.ApiClient(base_url=base_url)

response, status_code, headers = client.get_data("/posts/1")

print(response)

```
API Client also supports POST, PUT, and DELETE requests:
```python
# POST request
data = {"username": "johndoe", "email": "johndoe@example.com"}
response = client.post("/users", json=data)

# PUT request
data = {"email": "newemail@example.com"}
response = client.put("/users/1", json=data)

# DELETE request
response = client.delete("/users/1")
```

#  Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/yourusername/api-client. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the code of conduct.


# License
API Client is released under the [MIT License](URL).