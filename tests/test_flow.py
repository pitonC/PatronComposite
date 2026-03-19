from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from pc_builder.catalog import BUILD_PRIORITY
from pc_builder.cli import build_pc, format_summary
from pc_builder.composite import CompositeComponent, LeafProduct


class FlowTests(unittest.TestCase):
    def test_build_pc_asks_components_in_priority_order(self) -> None:
        # 10 componentes + 1 seleccion de gama.
        answers = iter(["1"] * len(BUILD_PRIORITY))
        prompts = []

        def fake_input(prompt: str) -> str:
            prompts.append(prompt)
            return next(answers)

        logs = []
        pc = build_pc(branch="media", input_func=fake_input, output_func=logs.append)

        self.assertEqual(len(pc.children), len(BUILD_PRIORITY))
        self.assertTrue(all(isinstance(node, CompositeComponent) for node in pc.children))
        self.assertTrue(all(len(node.children) == 1 for node in pc.children))
        self.assertTrue(all(isinstance(node.children[0], LeafProduct) for node in pc.children))
        self.assertTrue(any("Motherboard" in line for line in logs))
        self.assertTrue(any("Monitor" in line for line in logs))

        summary = format_summary(pc)
        self.assertIn("Total estimado", summary)


if __name__ == "__main__":
    unittest.main()

