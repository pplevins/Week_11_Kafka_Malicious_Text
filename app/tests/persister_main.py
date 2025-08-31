import asyncio

from persister import PersisterService

if __name__ == '__main__':
    asyncio.run(PersisterService().insert_to_db())
