# 📄 Juridiskt dokument i LaTeX

Detta är ett LaTeX-baserat dokument med juridiskt och politiskt innehåll, strukturerat för professionell PDF-export. All text skrivs med `babel=swedish` och korrekt typografisk hantering för svenska myndigheter, domstolar och internationell kommunikation.

## 🛠️ Kompilera till PDF

Följ instruktionerna nedan beroende på ditt operativsystem.

---

## 💻 Linux

De flesta Linux-distributioner (t.ex. Ubuntu, Debian, Arch) har `TeX Live` tillgängligt i pakethanteraren:

```bash
sudo apt install texlive-full  # Ubuntu/Debian
sudo pacman -S texlive-most    # Arch Linux
```

Sedan kompilerar du så här:

pdflatex main.tex


🍎 macOS
Installera först MacTeX via Homebrew (eller ladda ner från tug.org/mactex):
brew install --cask mactex

Kompilera:

pdflatex main.tex



🪟 Windows
Installera MiKTeX eller TeX Live for Windows.

Sedan kan du:

Öppna TeXworks (som följer med MiKTeX).

Ladda main.tex.

Tryck på den gröna pilen ("Typeset").

Eller kör via kommandoprompt:

pdflatex main.tex

