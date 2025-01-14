# Package Sorter - Thoughtful AI Technical Assessment
This is a package sorter that sorts packages into one of three categories:
- STANDARD: neither bulky nor heavy
- SPECIAL: either bulky or heavy but not both
- REJECTED: bulky and heavy

A **heavy** package has a mass >= 20kg.
A **bulky** package has at least one dimension >= 150cm *OR* a volume >= 1000000 cm^3, where volume=width\*height\*length


## How to Run:
```shell
python -m package_sort
```

## How to Test:
First set up a virtual environment and install pytest:
```shell
python -m venv .venv
source .venv/bin.activate
pip install -r requirements.txt
```

Then run the following command:
```shell
python -m pytest -v
```
