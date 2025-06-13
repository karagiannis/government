import os
import re

def find_broken_footnotes(root_dir):
    pattern = re.compile(r'\\footnote\{(.*?)\}', re.DOTALL)

    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.endswith('.tex'):
                path = os.path.join(dirpath, fname)
                with open(path, encoding='utf-8') as f:
                    content = f.read()

                    for match in pattern.finditer(content):
                        note_text = match.group(1)
                        if '\n\n' in note_text:
                            print(f"\n⚠️ Möjlig tom rad i fotnot: {path}")
                            lines = note_text.strip().splitlines()
                            for i, line in enumerate(lines):
                                print(f"  {i+1:02}: {line}")
                            print("  " + "-"*30)

find_broken_footnotes(".")

