

class TestRoute:
    """
    Test class to verify routes
    """

    def test_default(self, client):
        response = client.get("/")
        assert response.status_code == 200
        expected = "Congrats !!"
        print(response.get_data(as_text=True))
        assert expected == response.get_data(as_text=True)
