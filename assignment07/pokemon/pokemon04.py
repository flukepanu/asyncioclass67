import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Create tasks for each file.
    tasks = [process_file(path) for path in pathlist]

    # Wait for all tasks to complete.
    await asyncio.gather(*tasks)

asyncio.run(main())