# Ensamblador de PC con Patron Composite

Programa en Python que aplica el patron **Composite** para construir una configuracion de PC por ramas de gama:
- Alta
- Media
- Baja

Despues de elegir la gama, el programa pregunta los componentes en orden de prioridad:
1. Motherboard
2. CPU
3. RAM
4. GPU
5. SSD
6. PSU
7. Gabinete
8. Teclado
9. Mouse
10. Monitor

Cada componente tiene **2 opciones** y el usuario elige una.

## Estructura

- `main.py`: punto de entrada
- `src/pc_builder/composite.py`: clases del patron Composite
- `src/pc_builder/catalog.py`: catalogo por gama y prioridad
- `src/pc_builder/cli.py`: flujo interactivo
- `tests/`: pruebas basicas

## Ejecutar

```powershell
python .\main.py
```

## Probar

```powershell
python -m unittest discover -s .\tests -p "test_*.py"
```

