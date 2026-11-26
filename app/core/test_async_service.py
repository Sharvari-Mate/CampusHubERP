
import asyncio

from app.services.async_service import (
    load_all_data,
    generate_all_reports
)


async def test_async_functions():
    await load_all_data()
    print("All data loaded successfully.")

    await generate_all_reports()


if __name__ == "__main__":
    asyncio.run(test_async_functions())
