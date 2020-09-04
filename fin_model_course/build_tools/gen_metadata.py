"""
Takes hashes of all the generated content and determines whether the hash
has changed to update a JSON file with modified times
"""
import pathlib
from typing import Optional, Type

from build_tools.config import (
    GENERATED_PDFS_OUT_PATH,
    GENERATED_CONTENT_METADATA_PATH,
    EXAMPLES_PATH,
    STATIC_CONTENT_METADATA_PATH,
)
from models.content import (
    GeneratedCollectionMetadata,
    CollectionMetadata,
    StaticCollectionMetadata,
)


def generate_content_metadata_json(
    in_folder: pathlib.Path = GENERATED_PDFS_OUT_PATH,
    out_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
    collection_cls: Type[CollectionMetadata] = GeneratedCollectionMetadata,
    hashed_extension: str = "tex",
    output_extension: str = "pdf",
):
    print(f"Analyzing metadata for folder {in_folder}")
    current_metadata: Optional[collection_cls] = None
    if out_path.exists():
        current_metadata = collection_cls.parse_raw(out_path.read_text())
        print(f"Got existing metadata with {len(current_metadata.items)} items")
    print(f"Generating new metadata for folder {in_folder}")
    metadata = collection_cls.generate_from_folder(
        in_folder, hashed_extension=hashed_extension, output_extension=output_extension
    )
    if current_metadata is not None:
        print(f"Merging metadata")
        metadata = current_metadata.merge(metadata)
    print(f"Writing content metadata to {out_path}")
    out_path.write_text(metadata.json(indent=2))


if __name__ == "__main__":
    generate_content_metadata_json()
    generate_content_metadata_json(
        EXAMPLES_PATH,
        STATIC_CONTENT_METADATA_PATH,
        StaticCollectionMetadata,
        hashed_extension="xlsx",
        output_extension="xlsx",
    )
    generate_content_metadata_json(
        EXAMPLES_PATH,
        STATIC_CONTENT_METADATA_PATH,
        StaticCollectionMetadata,
        hashed_extension="ipynb",
        output_extension="ipynb",
    )
