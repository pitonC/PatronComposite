from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from pc_builder.composite import CompositeComponent, LeafProduct


class CompositeTests(unittest.TestCase):
    def test_total_price_and_display(self) -> None:
        pc = CompositeComponent(name="PC Test")

        cpu = CompositeComponent(name="CPU")
        cpu.add(LeafProduct(name="Ryzen 7", price=200, details="8 nucleos"))

        ram = CompositeComponent(name="RAM")
        ram.add(LeafProduct(name="16GB DDR5", price=80, details="5600MHz"))

        pc.add(cpu)
        pc.add(ram)

        self.assertEqual(pc.total_price(), 280)

        view = pc.display()
        self.assertIn("PC Test", view)
        self.assertIn("CPU", view)
        self.assertIn("RAM", view)


if __name__ == "__main__":
    unittest.main()

