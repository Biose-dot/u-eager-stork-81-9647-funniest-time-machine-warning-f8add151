import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry = "WARNING: Time travelers must not high-five their past selves. The machine charges extra for paradox cleanup."
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
