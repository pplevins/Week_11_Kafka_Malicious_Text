import asyncio

from app.services.retriever import RetrieverManager


def main():
    retriever = RetrieverManager()
    asyncio.run(retriever.retrieve())


if __name__ == "__main__":
    main()
