from gitLoad import downloadRepository
from scaffold import replace_in_files
from azdo import AzureDevOps
from dotenv import load_dotenv
import os

load_dotenv("/workspaces/tfStarter/tfScaffold/.env")

azdo = AzureDevOps(os.getenv("AZURE_DEVOPS_EXT_PAT"),os.getenv("AZURE_DEVOPS_ORGANIZATION"))
azdo.import_repository("test","Demo","https://corneliusschuchardt0951@dev.azure.com/corneliusschuchardt0951/corneliusschuchardt/_git/copyMe")

# # download repository
# downloadRepository("../stagingDir","bla")

# # replace by map
# replacement_map = {
#     "SUBSCRIPTION_ID": "{aaaa-bbbb-cccc-dddd-eeee}"
#     # Add more key-value pairs as needed
# }
# replace_in_files("../stagingDir",replacement_map)
