from blacksheep import  Request, ok
from blacksheep.server.controllers import APIController, get

from resources.bloxlink import instance as bloxlink
from ..decorators import authenticate



class Health(APIController):
    """Results in a path of <URL>/api/health/..."""

    @get("/")
    async def check_health(self, request: Request):
        """Endpoint to check if the service is alive and healthy."""

        # These will raise exceptions if they fail.
        await bloxlink.rest.fetch_application()
        await bloxlink.redis.ping()

        return ok("OK. Service is healthy.")