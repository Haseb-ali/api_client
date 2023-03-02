import unittest

from haso_api_client.rest_client import APIClient




class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient("https://jsonplaceholder.typicode.com")

    def test_get_data(self):
        response, status_code, _ = self.client.get("/posts/1")
        self.assertEqual(status_code, 200)
        self.assertEqual(response["userId"], 1)
        self.assertEqual(response["id"], 1)
        self.assertEqual(
            response["title"],
            "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        )
        self.assertEqual(
            response["body"],
            "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
        )

    def test_post_data(self):
        data = {"userId": 1, "id": 101, "title": "test title", "body": "test body"}
        response, status_code, _ = self.client.post(path="/posts", data=data)
        self.assertEqual(status_code, 201)
        self.assertEqual(response["userId"], 1)
        self.assertEqual(response["id"], 101)
        self.assertEqual(response["title"], "test title")
        self.assertEqual(response["body"], "test body")

    # test delete, put, patch
    def test_delete_data(self):
        response, status_code, _ = self.client.delete("/posts/1")
        self.assertEqual(status_code, 200)
        self.assertEqual(response, {})

    def test_put_data(self):
        data = {"userId": 1, "id": 1, "title": "test title", "body": "test body"}
        response, status_code, _ = self.client.put(path="/posts/1", data=data)
        self.assertEqual(status_code, 200)
        self.assertEqual(response["userId"], 1)
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["title"], "test title")
        self.assertEqual(response["body"], "test body")

    def test_patch_data(self):
        data = {"userId": 1, "id": 1, "title": "test title", "body": "test body"}
        response, status_code, _ = self.client.patch(path="/posts/1", data=data)
        self.assertEqual(status_code, 200)
        self.assertEqual(response["userId"], 1)
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["title"], "test title")
        self.assertEqual(response["body"], "test body")


if __name__ == "__main__":
    unittest.main()
