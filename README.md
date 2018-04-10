# Discordian-API for Python
============================
A simple fully async wrapper for the Discordians API.

## Example
------------
Fetching fancy variant of normal text.
```python
import asyncio
import discordians

client = discordians.DiscordiansClient()

async def main():
    text="This is gonna be fancy!"
    fancyText = await client.fancy(text=text)
    print(fancyText)

asyncio.get_event_loop().run_until_complete(main())
```

## Requirements
----------------
aiohttp>=2.0.0,<2.3.0

## Contributing
----------------
Just open a PR!

## Support
-------------
You will find support for this at our Discord server, https://discord.gg/jr8g83W

## License
-----------
It's released under the MIT license.
