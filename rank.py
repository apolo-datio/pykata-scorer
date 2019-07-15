from pathlib import Path
import importlib

participants = Path("participants")

for file in participants.glob("*.py"):
    part_module = importlib.import_module(str(file))
    dr_func = getattr(part_module, "digital_root")