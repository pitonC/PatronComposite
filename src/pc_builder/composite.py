from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


class Component:
    """Interfaz base del patron Composite."""

    def add(self, component: "Component") -> None:
        raise NotImplementedError("Este nodo no admite hijos.")

    def remove(self, component: "Component") -> None:
        raise NotImplementedError("Este nodo no tiene hijos para remover.")

    def display(self, indent: int = 0) -> str:
        raise NotImplementedError

    def total_price(self) -> int:
        raise NotImplementedError


@dataclass
class LeafProduct(Component):
    """Nodo hoja: representa un producto elegible."""

    name: str
    price: int
    details: str = ""

    def display(self, indent: int = 0) -> str:
        space = " " * indent
        details = f" ({self.details})" if self.details else ""
        return f"{space}- {self.name}{details}: ${self.price}"

    def total_price(self) -> int:
        return self.price


@dataclass
class CompositeComponent(Component):
    """Nodo compuesto: agrupa otros componentes o productos."""

    name: str
    children: List[Component] = field(default_factory=list)

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def display(self, indent: int = 0) -> str:
        space = " " * indent
        lines = [f"{space}{self.name}"]
        for child in self.children:
            lines.append(child.display(indent + 2))
        return "\n".join(lines)

    def total_price(self) -> int:
        return sum(child.total_price() for child in self.children)

