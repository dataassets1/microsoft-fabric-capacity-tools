import sempy.fabric as fabric
from datetime import datetime, timedelta
import time

# 1. Open your Fabric Workspace and check the browser's URL
# 2. https://app.fabric.microsoft.com/groups/WORKSPACE_ID_IS_HERE when you selects WorkSpace for the Capacity Metrics App
target_workspace = "PASTE HERE"

# 1. Open a Semantic Model from the Capacity Metrics App
# 2. Copy to below https://app.fabric.microsoft.com/onelake/details/11234-1234-2134-1234/dataset/SEMANTIC_MODEL_ID_IS_HERE/overview
target_semantic_model = "PASTE HERE"

q = """
EVALUATE 'Items'
"""

dax_query_user = mssparkutils.env.getUserName()
print(dax_query_user)
 
target_dax_query = q
 
dax_result = fabric.evaluate_dax(workspace = target_workspace, dataset = target_semantic_model,dax_string = target_dax_query)
 
display(dax_result)
