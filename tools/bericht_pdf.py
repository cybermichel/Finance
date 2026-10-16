#!/usr/bin/env python3
"""Wandelt einen Analyse-Bericht (Markdown) in ein gut lesbares A4-PDF um.

Nutzung:  python3 tools/bericht_pdf.py "Analysen/<Aktie>/Bericht.md"
Ergebnis: Bericht.pdf im selben Ordner.

Benötigt pandoc und Chromium/Chrome (Fallback: LibreOffice).
"""
import glob, os, re, shutil, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(HIER, "bericht.css")

# Emojis, die Standardschriften nicht darstellen können, durch lesbare Zeichen ersetzen
ERSATZ = {
    "️": "", "✅": "✓", "❌": "✗", "⭐": "★",
    "🔴": '<span style="color:#c0392b">●</span>',
    "🟡": '<span style="color:#d4a017">●</span>',
    "🟢": '<span style="color:#27ae60">●</span>',
    "⚠": '<span class="w">⚠</span>',
}


def finde_chrome():
    kandidaten = sorted(glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome"), reverse=True)
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        pfad = shutil.which(name)
        if pfad:
            kandidaten.append(pfad)
    kandidaten.append("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    return next((k for k in kandidaten if os.path.exists(k)), None)


def main():
    if len(sys.argv) != 2:
        sys.exit("Nutzung: python3 tools/bericht_pdf.py <Pfad/zu/Bericht.md>")
    md_pfad = os.path.abspath(sys.argv[1])
    pdf_pfad = os.path.splitext(md_pfad)[0] + ".pdf"
    if not shutil.which("pandoc"):
        sys.exit("Fehler: pandoc ist nicht installiert.")

    text = open(md_pfad, encoding="utf-8").read()
    for alt, neu in ERSATZ.items():
        text = text.replace(alt, neu)
    # Links auf lokale Dateien (z. B. Excel) funktionieren im PDF nicht -> nur den Namen zeigen
    text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", text)
    titel = re.search(r"^#\s+(.+)$", text, re.M)
    titel = titel.group(1) if titel else "Aktienanalyse"

    with tempfile.TemporaryDirectory() as tmp:
        md_tmp = os.path.join(tmp, "bericht.md")
        html = os.path.join(tmp, "bericht.html")
        open(md_tmp, "w", encoding="utf-8").write(text)
        subprocess.run(["pandoc", md_tmp, "-f", "gfm+hard_line_breaks", "-t", "html5", "-s",
                        "--metadata", f"pagetitle={titel}", "-c", CSS, "--embed-resources",
                        "-o", html], check=True)
        chrome = finde_chrome()
        if chrome:
            subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                            "--no-pdf-header-footer", f"--print-to-pdf={pdf_pfad}",
                            "file://" + html], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif shutil.which("soffice"):
            subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, html],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            shutil.move(os.path.join(tmp, "bericht.pdf"), pdf_pfad)
        else:
            sys.exit("Fehler: Weder Chromium/Chrome noch LibreOffice gefunden.")
    print(pdf_pfad)


if __name__ == "__main__":
    main()
