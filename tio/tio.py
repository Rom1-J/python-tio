from functools import lru_cache

import aiohttp
import requests
from aiocache import cached, Cache
from aiocache.serializers import PickleSerializer

from tio.contants import JSON_URL, API_URL
from tio.exceptions import LangNotFound, TioError
from tio.utils import shortcut, prepare_payload, clean_result


class Tio:
    @staticmethod
    @lru_cache(maxsize=None)
    def get_languages() -> dict:
        with requests.get(JSON_URL) as res:
            return res.json()

    def language_exists(self, lang: str) -> bool:
        return lang in self.get_languages()

    def run(
        self,
        lang: str,
        code: str,
        inputs: str = "",
        wrapped: bool = False,
        **kwargs
    ) -> str:
        lang = shortcut(lang)

        if not self.language_exists(lang):
            raise LangNotFound

        payload = prepare_payload(lang, code, inputs, wrapped, **kwargs)

        with requests.post(url=API_URL + "/", data=payload) as req:
            if req.status_code != 200:
                raise TioError

            return clean_result(req.text)


class AsyncTio:
    @staticmethod
    @cached(
        ttl=24 * 3600,
        serializer=PickleSerializer(),
        cache=Cache.MEMORY,
        namespace="tio",
    )
    # pylint: disable=invalid-overridden-method
    async def get_languages() -> dict:
        async with aiohttp.ClientSession() as cs, cs.get(JSON_URL) as res:
            return await res.json()

    # pylint: disable=invalid-overridden-method
    async def language_exists(self, lang: str) -> bool:
        return lang in await self.get_languages()

    # pylint: disable=invalid-overridden-method
    async def run(
        self,
        lang: str,
        code: str,
        inputs: str = "",
        wrapped: bool = False,
        **kwargs
    ) -> str:
        lang = shortcut(lang)

        if not await self.language_exists(lang):
            raise LangNotFound

        payload = prepare_payload(lang, code, inputs, wrapped, **kwargs)

        async with aiohttp.ClientSession() as cs, cs.post(
            url=API_URL + "/", data=payload
        ) as req:
            if req.status != 200:
                raise TioError

            return clean_result(await req.text())
