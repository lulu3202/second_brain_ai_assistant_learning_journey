from pathlib import Path

from loguru import logger
from zenml.steps import step

from second_brain_offline.entities.page import Page


@step
def read_pages_from_disk(data_directory: Path) -> list[Page]:
    pages: list[Page] = []

    if not data_directory.exists():
        raise FileNotFoundError(f"Directory not found: {data_directory}")

    for database_dir in data_directory.iterdir():
        if database_dir.is_dir():
            json_files = database_dir.glob("*.json")

            for json_file in json_files:
                page = Page.from_file(json_file)
                pages.append(page)

    logger.info(f"Successfully read {len(pages)} Page objects files")

    return pages
