from kubernetes import client, config
from kubernetes.client.rest import ApiException
from typing import Dict, List


class NodePodGrouperService:
    def __init__(self):
        """Initializes the connection to the Kubernetes API."""
        try:
            config.load_incluster_config()  # Prefer in-cluster config if available
        except config.config_exception.ConfigException:
            config.load_kube_config()  # Fallback to kubeconfig file
        self.core_api = client.CoreV1Api()

    def get_node(self, node_name: str) -> List[str]:
        """Returns a list of pods running on the specified node."""
        try:
            field_selector = f"spec.nodeName={node_name}"
            pods = self.core_api.list_pod_for_all_namespaces(field_selector=field_selector).items
            return [pod.metadata.name for pod in pods]
        except ApiException as e:
            raise Exception(f"Error retrieving pods for node '{node_name}': {e}")

    def get_nodes(self) -> Dict[str, List[str]]:
        """Returns a dictionary mapping node names to lists of pods on those nodes."""
        try:
            nodes = self.core_api.list_node().items
            node_pods = {}
            for node in nodes:
                pods = self.get_node(node.metadata.name)
                node_pods[node.metadata.name] = pods
            return node_pods
        except ApiException as e:
            raise Exception("Error retrieving nodes or pods: ", e)
