import pathlib

SITE_URL = 'https://nickderobertis.github.io/fin-model-course/'

PACKAGE_ROOT = pathlib.Path(__file__).parent.parent
PROJECT_ROOT = PACKAGE_ROOT.parent
LOCAL_PLBUILDER_ROOT = PACKAGE_ROOT / 'plbuild' / 'sources'
BUILD_TOOLS_ROOT = PACKAGE_ROOT / 'build_tools'

DOCSRC_SOURCE_PATH = PROJECT_ROOT / 'docsrc' / 'source'
DOCSRC_STATIC_PATH = DOCSRC_SOURCE_PATH / '_static'
EXAMPLES_PATH = DOCSRC_STATIC_PATH / 'Examples'
EXTRA_EXAMPLES_PATH = DOCSRC_STATIC_PATH / 'Extra Examples'

LAB_FOLDER_NAME = 'Materials for Lab Exercises'
LAB_EXERCISES_PATH = DOCSRC_STATIC_PATH / LAB_FOLDER_NAME

PRACTICE_PROBLEMS_FOLDER_NAME = 'Practice Problem Solutions'
PRACTICE_PROBLEMS_PATH = DOCSRC_STATIC_PATH / PRACTICE_PROBLEMS_FOLDER_NAME

GENERATED_OUT_PATH = DOCSRC_STATIC_PATH / 'generated'
GENERATED_PDFS_OUT_PATH = GENERATED_OUT_PATH / 'pdfs'
GENERATED_CONTENT_METADATA_PATH = BUILD_TOOLS_ROOT / "generated-content-metadata.json"

EXAMPLE_PATHS = [
    EXAMPLES_PATH,
    EXTRA_EXAMPLES_PATH,
    LAB_EXERCISES_PATH,
    PRACTICE_PROBLEMS_PATH
]
STATIC_CONTENT_METADATA_PATH = BUILD_TOOLS_ROOT / "static-content-metadata.json"

METADATA_PATHS = (
    GENERATED_CONTENT_METADATA_PATH,
    STATIC_CONTENT_METADATA_PATH,
)

ZIP_FILE_NAME = 'Financial Modeling All Downloads'
ZIP_FOLDER = DOCSRC_STATIC_PATH / ZIP_FILE_NAME
ZIP_FILE = DOCSRC_STATIC_PATH / f'{ZIP_FILE_NAME}.zip'
ZIP_COPY_PATHS = EXAMPLE_PATHS + [GENERATED_PDFS_OUT_PATH]


