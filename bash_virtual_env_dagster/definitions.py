from dagster import Definitions, load_assets_from_modules, PipesSubprocessClient

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=[*all_assets],
    resources={"pipes_subprocess_client": PipesSubprocessClient()},
)