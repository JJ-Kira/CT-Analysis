# Charge Transfer Analysis

## Overview

**Charge Transfer Analysis** is a standalone Python project derived from the PyBEST framework.
It quantifies how much **electronic charge moves between predefined molecular domains** during excitation or charge redistribution events.
This is essential for studying donor–acceptor systems, excited-state character, and intermolecular electron flow.

The analysis combines **orbital information** with **user-defined domains**, producing a **Charge Transfer (CT) matrix** where each element `CT(A→B)` represents the amount of charge transferred from domain A to domain B.

---

## Features

- **Domain-based charge decomposition** — assigns atoms to user-defined fragments.
- **Computation of the Charge Transfer matrix** from orbital coefficients.
- **Integration-ready architecture** — easily pluggable into larger frameworks such as PyBEST.
- **Optional GUI** (based on PySide6 + 3Dmol.js) for visual domain definition.
- **Reproducibility and modularity** — designed for both standalone use and automated testing.

---

## Conceptual Workflow

![Class Diagram](https://github.com/JJ-Kira/CT-Analysis/tree/main/docs/figures/class_diagram.png?raw=true)


Each step is modular, allowing the user to either interact with the data programmatically or through an optional GUI.

---

## Example Structure

```
ct-analysis/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
│
├── src/
│   └── ct_analysis/                # import ct_analysis
│       ├── __init__.py
│       ├── __main__.py             # enables: python -m ct_analysis
│       │
│       ├── cli/                    # CLI entry point
│       │   ├── __init__.py
│       │   └── main.py             # parses args; calls core.run()
│       │
│       ├── core/                   # core analysis modules
│       │   ├── __init__.py
│       │   ├── domain_spec.py      # atom→domain mapping, validation, colors
│       │   ├── ct_matrix.py        # charge transfer matrix construction
│       │   ├── analysis.py         # orchestrates CT computation
│       │   └── io.py               # checkpoint/orbital and XYZ I/O
│       │
│       └── gui/                    # Qt + 3Dmol.js GUI
│           ├── __init__.py
│           ├── picker.py           # selection / assign / unassign logic
│           ├── viewer.py           # QtWebEngine wrapper
│           └── assets/
│               ├── index.html      # 3Dmol canvas + toolbar
│               ├── viewer.js       # JS glue for selection tools
│               └── 3dmol/
│                   └── 3Dmol.min.js
│
├── tests/
│   ├── __init__.py
│   ├── test_domain_spec.py
│   ├── test_ct_matrix.py
│   └── test_cli_integration.py
│
├── examples/
│   ├── example_water_ct.py
│   └── molecules/
│       └── water.xyz
│
└── docs/                           # optional
    └── figures
```

---

## Usage Example

```bash
python -m ct_analysis --input molecule.chk --domains molecule_domains.xyz
```

If all domains are properly defined in the `.xyz` file, the analysis runs automatically.
Otherwise, a graphical interface will launch for interactive domain selection.

---

## Credits

Developed by **Julia Szczuczko** as part of Python 3 coursework.
Originally inspired by and integrated with **PyBEST (Pythonic Black-box Electronic Structure Tool)**.

---

## License

This project is distributed under the GNU General Public License v3 (GPLv3).

---

© 2025 Julia Szczuczko. All rights reserved.
