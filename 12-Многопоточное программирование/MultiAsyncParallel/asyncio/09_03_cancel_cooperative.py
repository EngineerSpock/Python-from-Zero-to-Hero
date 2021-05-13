import asyncio
import threading


async def fetch_doc(doc):
    await asyncio.sleep(3)  # emulating doc downloading
    print(f'{doc=}')
    return doc


async def get_docs(docs, token):
    pages = []
    for cur_doc in docs:
        if token.is_set():
            break
        doc = await fetch_doc(cur_doc)
        for page in doc:
            pages.append(page)
    return pages


def get_response(token):
    reply = input('Want to cancel or no? [y/n]')
    if reply == 'y':
        token.set()


async def main():
    token = threading.Event()
    task = asyncio.create_task(get_docs(['doc1', 'doc2', 'doc3'], token))

    t = threading.Thread(target=get_response, args=(token,))
    t.start()

    result = await task
    for doc in result:
        print(f'{doc}', end='')


if __name__ == '__main__':
    asyncio.run(main())
