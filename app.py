"""
A sample Hello World server using Sanic.
"""
import os

from sanic import Sanic
from sanic_ext import render

# pylint: disable=C0103
app = Sanic("hello-world-sanic")


@app.get("/")
async def hello(_request):
    """Renders the main page."""
    message = "It's running!"

    # Get Cloud Run environment variables.
    service = os.environ.get("K_SERVICE", "Unknown service")
    revision = os.environ.get("K_REVISION", "Unknown revision")

    return await render(
        "index.html",
        context={
            "message": message,
            "service": service,
            "revision": revision,
        },
    )


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(host="0.0.0.0", port=int(server_port), debug=False, workers=1)
