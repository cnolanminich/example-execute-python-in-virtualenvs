
import shutil

from dagster import AssetExecutionContext, Definitions, PipesSubprocessClient, asset
from pathlib import Path
import os 

PATH_TO_AUTOMATIONS =  Path("/Users/christian/code/dagster-demos/example-execute-python-in-virtualenvs/env1/")

@asset
def cli_command_asset(
    context: AssetExecutionContext, pipes_subprocess_client: PipesSubprocessClient
):
    path_to_python_exe = os.path.join(PATH_TO_AUTOMATIONS, ".venv/bin/python")
    #cmd = [shutil.which("bash"), os.path.join(path_to_script, "my_bash_script.sh")]
    cmd = [path_to_python_exe, os.path.join(PATH_TO_AUTOMATIONS, "my_script.py")]
    return pipes_subprocess_client.run(
        command=cmd,
        context=context,
    ).get_materialize_result()
