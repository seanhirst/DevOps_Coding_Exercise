from kubernetes import client, config
from kubernetes.client.rest import ApiException
from typing import Dict, List
import os
import yaml

class NodePodGrouperService:
    def __init__(self):
        """Initializes the connection to the Kubernetes API."""
        # Get the kubeconfig content from the environment variable.
        kube_config_content = os.environ.get('KUBECONFIG')

        if kube_config_content:
            try:
                kube_config = yaml.safe_load(kube_config_content)
                config.load_kube_config_from_dict(kube_config)
            except yaml.YAMLError as e:
                raise Exception(f"Error parsing kubeconfig from environment variable: {e}")
        else:
            raise Exception("KUBECONFIG environment variable not set or empty.")

        self.core_api = client.CoreV1Api()

    def get_node(self, node_name: str) -> List[Dict]:
        """Returns a list of pod details (name, namespace) running on the specified node."""
        try:
            field_selector = f"spec.nodeName={node_name}"
            pods = self.core_api.list_pod_for_all_namespaces(field_selector=field_selector).items
            return [{"name": pod.metadata.name, "namespace": pod.metadata.namespace} for pod in pods]
        except ApiException as e:
            raise Exception(f"Error retrieving pods for node '{node_name}': {e.status} {e.reason}")  

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
