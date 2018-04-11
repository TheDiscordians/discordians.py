import asyncio
import urllib.parse
import aiohttp


class ArgumentError(Exception):
    pass


class DifferentResponseCode(Exception):
    pass


class DiscordiansClient:

    """
    The main class to interact with the API.

    Raises:
        ArgumentError: Invalid arguments passed.
        DifferentResponseCode: The API returned a non-200 response code.

    """

    def __init__(self, loop=None, session=None):
        """The __init__ method."""
        self._loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=loop) if session is None else session
        self.baseURL = "https://discordians-api.herokuapp.com/"

    async def _get(self, endpoint, params):
        async with self._session.get("{}{}".format(self.baseURL, endpoint), params=params) as resp:
            if resp.status != 200:
                raise DifferentResponseCode("API returned a non-200 response code, that is {}.".format(resp.status))
            text = await resp.text()
        return text

    async def cursive(self, *, text=None):
        """Return cursive text from normal text.
        This function is a coroutine.

        Args:
        text (str) : The text to convert

        Returns:
            dict: A dictionary that contains the cursive text.
            ::

                {
                    "message": The converted text.
                }

        """
        if text is None:
            raise ArgumentError("No text provided.")
        return await self._get("translate/cursive", {"text": text})
    
    async def fancy(self, *, text=None):
        """Return fancy text from normal text.
        This function is a coroutine.

        Args:
            text (str) : The text to convert

        Returns:
            dict: A dictionary that contains the fancy text.
            ::

                {
                    "message": The converted text.
                }

        """
        if text is None:
            raise ArgumentError("No text provided.")
        return await self._get("translate/fancy", {"text": text})
    
    async def fancy2(self, *, text=None):
        """Return fancy (style 2) text from normal text.
        This function is a coroutine.

        Args:
            text (str) : The text to convert
        Returns:
            dict: A dictionary that contains the fancy (style 2) text.
            ::

                {
                    "message": The converted text.
                }

        """
        if text is None:
            raise ArgumentError("No text provided.")
        return await self._get("translate/fancy2", {"text": text})

    async def leet(self, *, text=None):
        """Return leet text from normal text.
        This function is a coroutine.
        
        Args:
            text (str) : The text to convert
        Returns:
            dict: A dictionary that contains the leet type text.
            ::

                {
                    "message": The converted text.
                }

        """
        if text is None:
            raise ArgumentError("No text provided.")
        return await self._get("translate/leet", {"text": text})

    async def pirate(self, *, text=None):
        """Return pirate talk text from normal text.
        This function is a coroutine.

        Args:
            text (str) : The text to convert
        Returns:
            dict: A dictionary that contains the pirate talk text.
            ::

                {
                    "message": The converted text.
                }

        """
        if text is None:
            raise ArgumentError("No text provided.")
        return await self._get("translate/pirate", {"text": text})

    async def zalgolize(self, *, text=None):
        """Return zalgolized text from normal text.
        This function is a coroutine.

        Args:
            text (str) : The text to convert
        Returns:
            dict: A dictionary that contains the zalgolized text.
            ::

                {
                    "message": The converted text.
                }

        """
        if text is None:
            raise ArgumentError("No text provided.")
        return await self._get("translate/zalgolize", {"text": text})

    async def dilbert(self, *, today=False):
        """Return a random or today's Dilbert comic.
        This function is a coroutine.

        Args:
            today (bool) : The bool specifying to get today's comic or not.
        Returns:
            dict: A dictionary that contains the url to the Dilbert comic image.
            ::

                {
                    "URL": Website link
                    "image": image URL
                }

        """
        boolText = "false" if not today else "true" 
        return await self._get("comic/dilbert", {"today": boolText})

    async def garfield(self, *, today=False):
        """Return a random or today's Garfield comic.
        This function is a coroutine.

        Args:
            today (bool) : The bool specifying to get today's comic or not.
        Returns:
            dict: A dictionary that contains the url to the Garfield comic image.
            ::

                {
                    "image": URL
                }

        """
        boolText = "false" if not today else "true" 
        return await self._get("comic/garfield", {"today": boolText})

    async def pickupline(self):
        """Get a random pickup line.
        This function is a coroutine.
        
        Returns:
            dict: A dictionary containing the pickup line.
            ::

                {
                    "pickupLine": the pickup line.
                }

        """
        return await self._get("fun/pickup-line", None)

    async def close(self):
        await self._session.close()
        