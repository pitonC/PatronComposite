from __future__ import annotations

from typing import Callable, Dict, List

from .catalog import BRANCH_LABELS, BUILD_PRIORITY, CATALOG, COMPONENT_LABELS
from .composite import CompositeComponent, LeafProduct

InputFunc = Callable[[str], str]
OutputFunc = Callable[[str], None]


def prompt_branch(input_func: InputFunc, output_func: OutputFunc) -> str:
    output_func("Elige la gama de tu PC:")
    output_func("1) Gama Alta")
    output_func("2) Gama Media")
    output_func("3) Gama Baja")

    options = {"1": "alta", "2": "media", "3": "baja"}
    while True:
        selected = input_func("Selecciona 1, 2 o 3: ").strip()
        if selected in options:
            return options[selected]
        output_func("Opcion invalida. Intenta de nuevo.")


def prompt_component_choice(
    component_key: str,
    options: List[Dict[str, object]],
    input_func: InputFunc,
    output_func: OutputFunc,
) -> Dict[str, object]:
    label = COMPONENT_LABELS[component_key]
    output_func(f"\nSelecciona {label}:")
    for idx, option in enumerate(options, start=1):
        output_func(
            f"{idx}) {option['name']} - ${option['price']} ({option['details']})"
        )

    while True:
        selected = input_func("Elige 1 o 2: ").strip()
        if selected in {"1", "2"}:
            return options[int(selected) - 1]
        output_func("Entrada invalida. Debes elegir 1 o 2.")


def build_pc(branch: str, input_func: InputFunc = input, output_func: OutputFunc = print) -> CompositeComponent:
    if branch not in CATALOG:
        raise ValueError(f"Gama no soportada: {branch}")

    tree = CompositeComponent(name=f"Configuracion {BRANCH_LABELS[branch]}")
    output_func(f"\nArmaras una PC de {BRANCH_LABELS[branch]}.")
    output_func("Prioridad de seleccion: motherboard -> CPU -> RAM -> GPU -> SSD -> PSU -> gabinete -> teclado -> mouse -> monitor")

    branch_catalog = CATALOG[branch]
    for component_key in BUILD_PRIORITY:
        category_node = CompositeComponent(name=COMPONENT_LABELS[component_key])
        chosen = prompt_component_choice(
            component_key=component_key,
            options=branch_catalog[component_key],
            input_func=input_func,
            output_func=output_func,
        )
        category_node.add(
            LeafProduct(
                name=str(chosen["name"]),
                price=int(chosen["price"]),
                details=str(chosen["details"]),
            )
        )
        tree.add(category_node)

    return tree


def format_summary(tree: CompositeComponent) -> str:
    return (
        "\nResumen de tu PC:\n"
        f"{tree.display()}\n"
        f"\nTotal estimado: ${tree.total_price()}"
    )


def run_cli(input_func: InputFunc = input, output_func: OutputFunc = print) -> CompositeComponent:
    output_func("=== Ensamblador de PC (Patron Composite) ===")
    branch = prompt_branch(input_func=input_func, output_func=output_func)
    pc = build_pc(branch=branch, input_func=input_func, output_func=output_func)
    output_func(format_summary(pc))
    return pc

