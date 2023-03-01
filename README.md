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

response, status_code, headers = client.get("/posts/1")


```
API Client also supports POST, PUT, and DELETE requests:
```python
# POST request
data = {"userId": 1, "id": 101, "title": "test title", "body": "test body"}
response, status_code, headers = self.client.post(path="/posts", data=data)


# PUT request
data = {"userId": 1, "id": 1, "title": "test title", "body": "test body"}
response, status_code, headers = self.client.put(path="/posts/1", data=data)
# DELETE request
response, status_code, _ = self.client.delete("/posts/1")
```

#  Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/Haseb-ali/api_client. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the code of conduct.


# License
API Client is released under the [MIT License](URL).
