from config import ClusterConfig
from components.managed_kubernetes_cluster import (
    ManagedKubernetesCluster,
    ManagedKubernetesClusterArgs
)

from pulumi import export

cluster_config = ClusterConfig()

cluster = ManagedKubernetesCluster(
    "cluster",
    ManagedKubernetesClusterArgs(
        kubernetes_version="1.22.4",
        node_count=3,
        resource_group_name=cluster_config.resource_group_name,
        subnet_id=cluster_config.subnet_id,
        vnet_id=cluster_config.vnet_id,
        subscription_id=cluster_config.subscription_id,
    ),
)

export("kube_config", cluster.kube_config)
export("ingress_ip_address", cluster.ingress_ip_address)
