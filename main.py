import os

LINE = "Judge, I didn’t break production — I gave it a surprise holiday, and I baked you cookies for the verdict, so we’re even."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# The entry line is fixed and deterministic; see README.md for the text.
