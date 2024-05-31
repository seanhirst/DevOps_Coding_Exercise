from typing import Protocol

Node = str
Pod = str


class NodePodGrouperProtocol(Protocol):
    def get_nodes(self) -> dict[Node, list[Pod]]:
        ...

    def get_node(self, Node) -> list[Pod]:
        ...
