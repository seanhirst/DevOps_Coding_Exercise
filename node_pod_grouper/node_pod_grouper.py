from kubernetes import client, config
from kubernetes.client.rest import ApiException
from typing import Dict, List
import os 

class NodePodGrouperService:
    def __init__(self):
        """Initializes the connection to the Kubernetes API."""

        # Get the kubeconfig file path from the environment variable.
        kube_config_path = os.environ.get('KUBECONFIG', '~/.kube/config')

        try:
            config.load_kube_config(config_file=kube_config_path)
        except config.config_exception.ConfigException:
            raise Exception("Could not load Kubernetes configuration from {}".format(kube_config_path))
        self.core_api = client.CoreV1Api()

    def get_node(self, node_name: str) -> List[Dict]:
        """Returns a list of pod details (name, namespace) running on the specified node."""
        try:
            field_selector = f"spec.nodeName={node_name}"
            pods = self.core_api.list_pod_for_all_namespaces(field_selector=field_selector).items
            return [{"name": pod.metadata.name, "namespace": pod.metadata.namespace} for pod in pods]
        except ApiException as e:
            raise Exception(f"Error retrieving pods for node '{node_name}': {e.status} {e.reason}")  # More informative error message

    def get_nodes(self) -> Dict[str, List[Dict]]:
        """Returns a dictionary mapping node names to lists of pod details on those nodes."""
        try:
            nodes = self.core_api.list_node().items
            node_pods = {}
            for node in nodes:
                pods = self.get_node(node.metadata.name)
                node_pods[node.metadata.name] = pods
            return node_pods
        except ApiException as e:
            raise Exception("Error retrieving nodes or pods: ", e)
