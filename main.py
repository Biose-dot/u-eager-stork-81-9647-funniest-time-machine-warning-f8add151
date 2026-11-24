import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry = "WARNING: Do not feed the time machine after midnight. It gets hiccups, burps paradoxes, and eats your yesterday."
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
