import asyncio
import time

import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.thumbnailUrl = thumbnail_url
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.albumId = album_id

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    if not isinstance(album, int):
        raise RuntimeError('invalid album number')

    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'
    response = await session.get(url)
    photos_json = await response.json()

    await asyncio.sleep(1)
    return [Photo.from_json(photo) for photo in photos_json]


async def download_albums(albums):
    async with aiohttp.ClientSession() as session:
        for album in albums:
            try:
                yield await photos_by_album(f't{album}', album, session)
            except Exception as ex:
                print(repr(ex))


async def main():
    async for photos in download_albums([1, 2, 'a', 4]):
        print_photo_titles(photos)


if __name__ == '__main__':
    asyncio.run(main())

    time.sleep(3)
    print('main ended')
