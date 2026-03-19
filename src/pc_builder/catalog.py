from __future__ import annotations

from typing import Dict, List


BUILD_PRIORITY = [
    "motherboard",
    "cpu",
    "ram",
    "gpu",
    "ssd",
    "psu",
    "case",
    "keyboard",
    "mouse",
    "monitor",
]

COMPONENT_LABELS = {
    "motherboard": "Motherboard",
    "cpu": "Procesador (CPU)",
    "ram": "Memoria RAM",
    "gpu": "Tarjeta grafica (GPU)",
    "ssd": "Almacenamiento SSD",
    "psu": "Fuente de poder (PSU)",
    "case": "Gabinete",
    "keyboard": "Teclado",
    "mouse": "Mouse",
    "monitor": "Monitor",
}

BRANCH_LABELS = {
    "alta": "Gama Alta",
    "media": "Gama Media",
    "baja": "Gama Baja",
}

CatalogType = Dict[str, Dict[str, List[dict]]]


CATALOG: CatalogType = {
    "alta": {
        "motherboard": [
            {"name": "ASUS ROG Maximus Z790", "price": 520, "details": "DDR5 / WiFi 6E"},
            {"name": "MSI MEG Z790 ACE", "price": 500, "details": "DDR5 / PCIe 5.0"},
        ],
        "cpu": [
            {"name": "Intel Core i9-14900K", "price": 640, "details": "24 nucleos"},
            {"name": "AMD Ryzen 9 7950X", "price": 620, "details": "16 nucleos"},
        ],
        "ram": [
            {"name": "64GB DDR5 6000", "price": 260, "details": "2x32GB"},
            {"name": "32GB DDR5 6400", "price": 220, "details": "2x16GB"},
        ],
        "gpu": [
            {"name": "NVIDIA RTX 4090", "price": 1800, "details": "24GB GDDR6X"},
            {"name": "AMD RX 7900 XTX", "price": 980, "details": "24GB GDDR6"},
        ],
        "ssd": [
            {"name": "Samsung 990 Pro 2TB", "price": 210, "details": "NVMe Gen4"},
            {"name": "WD Black SN850X 2TB", "price": 200, "details": "NVMe Gen4"},
        ],
        "psu": [
            {"name": "Corsair RM1000x", "price": 220, "details": "1000W 80+ Gold"},
            {"name": "Seasonic Prime TX-1000", "price": 310, "details": "1000W 80+ Titanium"},
        ],
        "case": [
            {"name": "Lian Li O11 Dynamic EVO", "price": 190, "details": "Mid tower"},
            {"name": "NZXT H9 Flow", "price": 170, "details": "Airflow"},
        ],
        "keyboard": [
            {"name": "Keychron Q1 Pro", "price": 220, "details": "Mecanico"},
            {"name": "Logitech G915", "price": 230, "details": "Wireless"},
        ],
        "mouse": [
            {"name": "Logitech G Pro X Superlight", "price": 160, "details": "Ultra ligero"},
            {"name": "Razer DeathAdder V3 Pro", "price": 150, "details": "Wireless"},
        ],
        "monitor": [
            {"name": "ASUS ROG Swift 27\" 240Hz", "price": 780, "details": "1440p"},
            {"name": "LG UltraGear 34\"", "price": 850, "details": "Ultrawide 165Hz"},
        ],
    },
    "media": {
        "motherboard": [
            {"name": "MSI B760 Tomahawk", "price": 220, "details": "DDR5"},
            {"name": "ASUS TUF B650-Plus", "price": 230, "details": "AM5"},
        ],
        "cpu": [
            {"name": "Intel Core i5-14600K", "price": 330, "details": "14 nucleos"},
            {"name": "AMD Ryzen 7 7700", "price": 300, "details": "8 nucleos"},
        ],
        "ram": [
            {"name": "32GB DDR5 5600", "price": 140, "details": "2x16GB"},
            {"name": "16GB DDR5 6000", "price": 95, "details": "2x8GB"},
        ],
        "gpu": [
            {"name": "NVIDIA RTX 4070 Super", "price": 610, "details": "12GB"},
            {"name": "AMD RX 7800 XT", "price": 530, "details": "16GB"},
        ],
        "ssd": [
            {"name": "Crucial P3 Plus 1TB", "price": 90, "details": "NVMe"},
            {"name": "Kingston KC3000 1TB", "price": 110, "details": "NVMe"},
        ],
        "psu": [
            {"name": "Corsair RM750e", "price": 120, "details": "750W 80+ Gold"},
            {"name": "Cooler Master MWE 750", "price": 95, "details": "750W Bronze"},
        ],
        "case": [
            {"name": "Phanteks Eclipse G360A", "price": 100, "details": "Airflow"},
            {"name": "NZXT H5 Flow", "price": 105, "details": "Mid tower"},
        ],
        "keyboard": [
            {"name": "HyperX Alloy Origins", "price": 95, "details": "Mecanico"},
            {"name": "Logitech G413", "price": 85, "details": "Mecanico"},
        ],
        "mouse": [
            {"name": "Logitech G502 X", "price": 70, "details": "Gaming"},
            {"name": "Razer Basilisk V3", "price": 65, "details": "Gaming"},
        ],
        "monitor": [
            {"name": "AOC 27\" 144Hz", "price": 220, "details": "1080p"},
            {"name": "Gigabyte M27Q", "price": 280, "details": "1440p"},
        ],
    },
    "baja": {
        "motherboard": [
            {"name": "Gigabyte H610M", "price": 105, "details": "DDR4"},
            {"name": "ASRock A520M", "price": 95, "details": "AM4"},
        ],
        "cpu": [
            {"name": "Intel Core i3-13100", "price": 140, "details": "4 nucleos"},
            {"name": "AMD Ryzen 5 5500", "price": 120, "details": "6 nucleos"},
        ],
        "ram": [
            {"name": "16GB DDR4 3200", "price": 55, "details": "2x8GB"},
            {"name": "8GB DDR4 3200", "price": 35, "details": "1x8GB"},
        ],
        "gpu": [
            {"name": "NVIDIA RTX 3050", "price": 240, "details": "8GB"},
            {"name": "AMD RX 6600", "price": 220, "details": "8GB"},
        ],
        "ssd": [
            {"name": "Kingston NV2 500GB", "price": 45, "details": "NVMe"},
            {"name": "WD Green 480GB", "price": 40, "details": "SATA"},
        ],
        "psu": [
            {"name": "EVGA 600W", "price": 60, "details": "80+"},
            {"name": "Thermaltake Smart 500W", "price": 55, "details": "80+"},
        ],
        "case": [
            {"name": "DeepCool Matrexx 40", "price": 50, "details": "Micro ATX"},
            {"name": "Antec NX200M", "price": 48, "details": "Micro ATX"},
        ],
        "keyboard": [
            {"name": "Redragon K552", "price": 45, "details": "Mecanico"},
            {"name": "Logitech K120", "price": 20, "details": "Membrana"},
        ],
        "mouse": [
            {"name": "Redragon Cobra", "price": 25, "details": "Gaming"},
            {"name": "Logitech M90", "price": 15, "details": "Basico"},
        ],
        "monitor": [
            {"name": "Samsung 24\" 75Hz", "price": 110, "details": "1080p"},
            {"name": "LG 22\" 75Hz", "price": 95, "details": "1080p"},
        ],
    },
}

