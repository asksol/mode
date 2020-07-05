import asyncio
import pytest


@pytest.yield_fixture()
def loop():
    try:
        prev_loop = asyncio.get_event_loop()
    except Exception:
        prev_loop = None
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        yield loop
    finally:
        if prev_loop is not None:
            asyncio.set_event_loop(prev_loop)
