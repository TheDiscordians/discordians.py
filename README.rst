============================
Discordian-API for Python
============================
-------------------------------------------------------
A simple fully async wrapper for the Discordians API.
-------------------------------------------------------

Example
=========

Fetching fancy variant of normal text.

.. code:: python

    import asyncio
    import discordians

    async def main():
        client = discordians.DiscordiansClient()
        text="This is gonna be fancy!"
        fancyText = await client.fancy(text=text)
        print(fancyText)
        await client.close()

    asyncio.get_event_loop().run_until_complete(main())

Requirements
================

aiohttp>=3.3.0,<3.4.0

Contributing
=============

Just open a PR!

Support
============

You will find support for this at our Discord server,
https://discord.gg/jr8g83W

License
===========

It's released under the MIT license.
