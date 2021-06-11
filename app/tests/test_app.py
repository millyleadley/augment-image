from app import app as flask_app


def test_index():
    """
    Checks that we are able to make GET calls,
    and that the response contains the correct description
    of whats in the image.
    """

    with flask_app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"milhouse" in response.data

        response = client.get("/?url=https://imgs.xkcd.com/comics/bad_code.png")
        assert response.status_code == 200
        assert b"milhouse" not in response.data
