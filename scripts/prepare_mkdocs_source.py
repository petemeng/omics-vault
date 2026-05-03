from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "webdocs"

CONTENT_DIRS = [
    "_concepts",
    "_meta",
    "00-foundations",
    "01-genomics",
    "02-GWAS",
    "03-bulk-RNAseq",
    "04-scRNAseq",
    "05-snRNAseq",
    "06-spatial",
    "07-BCR-TCR",
    "08-ATAC",
    "09-methylation",
    "10-ChIP-CUTRUN",
    "11-3D-genome",
    "12-proteomics",
    "13-metabolomics",
    "14-microbiome",
    "15-multiomics-integration",
    "assets",
]


def copy_path(src: Path, dst: Path) -> None:
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", ".obsidian"))
    else:
        shutil.copy2(src, dst)


def main() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir()

    copy_path(ROOT / "README.md", TARGET / "README.md")
    for dirname in CONTENT_DIRS:
        src = ROOT / dirname
        if src.exists():
            copy_path(src, TARGET / dirname)

    print(f"Prepared MkDocs source: {TARGET}")


if __name__ == "__main__":
    main()

