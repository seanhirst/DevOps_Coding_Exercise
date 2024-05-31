from typing import Protocol, List, Dict

Node = str
Pod = str


class NodePodGrouperProtocol(Protocol):
    def get_nodes(self) -> Dict[Node, List[Pod]]:
        ...

    def get_node(self, node_name: Node) -> List[Pod]:
        ...
