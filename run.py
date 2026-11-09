#!/usr/bin/env python3
"""Lance une solution d'Advent of Code, quel que soit le langage.

Le dépôt est organisé par exercice :

    <année>/dayNN/partN.<py|c|rs>   les solutions (une par partie)
    <année>/inputs/dayNN.txt        l'entrée du puzzle, partagée par les parties

Exemples
--------
    python3 run.py 2025 1 1          # 2025, jour 1, partie 1
    python3 run.py 2025 1            # les deux parties du jour 1
    python3 run.py 2015              # tous les exercices de 2015
    python3 run.py --all             # tout le dépôt
    python3 run.py 2025 12 1 --lang rust
    python3 run.py 2015 1 1 -i mon_input.txt
    python3 run.py --list            # inventorier les exercices

Chaque solution lit `inputs/dayNN.txt` par défaut ; on peut passer une autre
entrée en argument, et sinon les données sont lues sur l'entrée standard.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGUAGES = ("python", "c", "rust")
EXTENSION_TO_LANGUAGE = {".py": "python", ".c": "c", ".rs": "rust"}
TOOLCHAINS = {"c": "gcc", "rust": "rustc"}


# --------------------------------------------------------------------------- #
# Découverte des exercices
# --------------------------------------------------------------------------- #
def part_of(source: Path) -> int:
    """Déduit le numéro de partie depuis le nom du fichier (part1/part2/main)."""
    stem = source.stem.lower()
    if stem.endswith("2") or stem == "part2":
        return 2
    return 1


def discover() -> list[dict]:
    """Renvoie la liste des solutions trouvées, triées par année/jour/partie."""
    found = []
    for year_dir in sorted(ROOT.glob("[0-9][0-9][0-9][0-9]")):
        if not year_dir.is_dir():
            continue
        for day_dir in sorted(year_dir.glob("day[0-9][0-9]")):
            for source in sorted(day_dir.iterdir()):
                if not source.is_file() or source.suffix not in EXTENSION_TO_LANGUAGE:
                    continue
                found.append(
                    {
                        "year": int(year_dir.name),
                        "day": int(day_dir.name[3:]),
                        "part": part_of(source),
                        "language": EXTENSION_TO_LANGUAGE[source.suffix],
                        "source": source,
                        "input": year_dir / "inputs" / f"{day_dir.name}.txt",
                    }
                )
    return sorted(found, key=lambda e: (e["year"], e["day"], e["part"], e["language"]))


# --------------------------------------------------------------------------- #
# Exécution
# --------------------------------------------------------------------------- #
def compile_to_tmp(source: Path, compiler: str, flags: list[str]) -> Path:
    """Compile C ou Rust dans un dossier temporaire (pas de binaire versionné)."""
    tmpdir = Path(tempfile.mkdtemp(prefix="aoc-"))
    binary = tmpdir / source.stem
    subprocess.run(
        [compiler, *flags, "-o", str(binary), str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
    return binary


def run_entry(entry: dict, puzzle_input: Path, timeout: int) -> tuple[bool, str]:
    source, language = entry["source"], entry["language"]
    try:
        if language == "python":
            command = [sys.executable, str(source), str(puzzle_input)]
        elif language == "c":
            command = [str(compile_to_tmp(source, "gcc", ["-O2"])), str(puzzle_input)]
        else:
            command = [str(compile_to_tmp(source, "rustc", ["-O"])), str(puzzle_input)]
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError as exc:
        return False, f"outil manquant : {exc.filename}"
    except subprocess.CalledProcessError as exc:
        return False, (exc.stderr or exc.stdout or "échec de compilation").strip()
    except subprocess.TimeoutExpired:
        return False, f"délai dépassé ({timeout} s)"

    if result.returncode != 0:
        return False, (result.stderr or result.stdout).strip()
    return True, (result.stdout or "").strip()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lance les solutions d'Advent of Code du dépôt.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("year", nargs="?", type=int, help="année, ex. 2025")
    parser.add_argument("day", nargs="?", type=int, help="jour, ex. 1")
    parser.add_argument("part", nargs="?", type=int, help="partie (1 ou 2)")
    parser.add_argument("--all", action="store_true", help="lancer tous les exercices")
    parser.add_argument("--lang", choices=LANGUAGES, help="limiter à un langage")
    parser.add_argument("-i", "--input", type=Path, help="utiliser une autre entrée")
    parser.add_argument(
        "--timeout", type=int, default=120, help="délai par solution (s, défaut 120)"
    )
    parser.add_argument("--list", action="store_true", help="lister les exercices sans les lancer")
    args = parser.parse_args()

    entries = discover()
    if args.year:
        entries = [e for e in entries if e["year"] == args.year]
    if args.day:
        entries = [e for e in entries if e["day"] == args.day]
    if args.part:
        entries = [e for e in entries if e["part"] == args.part]
    if args.lang:
        entries = [e for e in entries if e["language"] == args.lang]

    if not entries:
        print("Aucun exercice ne correspond à cette sélection.", file=sys.stderr)
        return 1

    if args.list:
        for e in entries:
            has_input = "" if e["input"].exists() else "  (sans entrée → stdin)"
            print(
                f"{e['year']}  jour {e['day']:02d}  partie {e['part']}  "
                f"{e['language']:<6} {e['source'].relative_to(ROOT)}{has_input}"
            )
        return 0

    failures = 0
    skipped = 0
    for entry in entries:
        puzzle_input = Path(args.input) if args.input else entry["input"]
        label = (
            f"{entry['year']} jour {entry['day']:02d} partie {entry['part']} "
            f"[{entry['language']}]"
        )

        tool = TOOLCHAINS.get(entry["language"])
        if tool and shutil.which(tool) is None:
            print(f"✗ {label} : {tool} n'est pas installé")
            failures += 1
            continue

        has_input = puzzle_input.exists()
        if not has_input and not args.input:
            # Pas d'entrée versionnée pour ce jour : inutile de lancer avec stdin vide.
            print(f"⊘ {label} : entrée absente ({entry['input'].relative_to(ROOT)} à ajouter)")
            skipped += 1
            continue

        ok, output = run_entry(entry, Path(puzzle_input), args.timeout)

        if ok:
            print(f"✓ {label} → {output}")
        else:
            failures += 1
            print(f"✗ {label} : échec")
            for line in output.splitlines()[-5:]:
                print(f"    {line}")

    ran = len(entries) - failures - skipped
    summary = f"\n{ran}/{len(entries)} solution(s) exécutée(s) sans erreur."
    if skipped:
        summary += f" {skipped} sans entrée (ignorées)."
    print(summary)
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
