#!/bin/bash

echo "🔍 Söker efter misstänkta rader..."

grep -n -r --include="*.tex" "\\usepackage" .
grep -n -r --include="*.tex" "enotez" .
grep -n -r --include="*.tex" "split" .

echo "✅ Färdig."

