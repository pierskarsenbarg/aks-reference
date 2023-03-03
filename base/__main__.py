import pulumi
from pulumi_azure_native import resources

config = pulumi.Config()
password = config.require("apitoken")

resource_group = resources.ResourceGroup("resourcegroup", None, pulumi.ResouceOptions(
    protect=True
))

pulumi.export("resourceGroupName", resource_group.name)
