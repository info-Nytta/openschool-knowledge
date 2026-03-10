"""
Modul 7 — Open source és közösség: Közösségi fájlok verifikáció.
Ellenőrzi, hogy a repó készen áll kontribútorok fogadására.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent


def test_license_exists():
    """A LICENSE fájl létezik."""
    license_paths = [
        REPO_ROOT / "LICENSE",
        REPO_ROOT / "LICENSE.md",
        REPO_ROOT / "LICENSE.txt",
    ]
    assert any(p.is_file() for p in license_paths), (
        "Hiányzik a LICENSE fájl. Adj hozzá egy nyílt forrású licencet (pl. MIT)."
    )


def test_license_is_not_empty():
    """A LICENSE fájl nem üres."""
    for name in ["LICENSE", "LICENSE.md", "LICENSE.txt"]:
        path = REPO_ROOT / name
        if path.is_file():
            content = path.read_text().strip()
            assert len(content) > 50, (
                f"A {name} fájl túl rövid. Használj teljes licencszöveget."
            )
            return
    assert False, "Nem található LICENSE fájl."


def test_contributing_exists():
    """A CONTRIBUTING.md létezik."""
    assert (REPO_ROOT / "CONTRIBUTING.md").is_file(), (
        "Hiányzik a CONTRIBUTING.md. "
        "Írj útmutatót az új kontribútoroknak."
    )


def test_contributing_has_content():
    """A CONTRIBUTING.md tartalmaz legalább alapvető információt."""
    contrib = REPO_ROOT / "CONTRIBUTING.md"
    if not contrib.is_file():
        assert False, "Hiányzik a CONTRIBUTING.md."

    content = contrib.read_text().lower()
    # Ellenőrizzük, hogy tartalmaz-e tipikus szekciókat
    has_fork = "fork" in content
    has_pr = "pull request" in content or "pr" in content
    has_issue = "issue" in content
    assert has_fork or has_pr or has_issue, (
        "A CONTRIBUTING.md-nek tartalmaznia kell útmutatót a forkhoz, "
        "PR-ekhez vagy issue-khoz."
    )


def test_issue_templates_exist():
    """Az issue template-ek léteznek."""
    template_dir = REPO_ROOT / ".github" / "ISSUE_TEMPLATE"
    assert template_dir.is_dir(), (
        "Hiányzik a .github/ISSUE_TEMPLATE/ mappa. "
        "Hozz létre bug report és feature request template-eket."
    )
    templates = list(template_dir.glob("*.md")) + list(template_dir.glob("*.yml"))
    assert len(templates) >= 2, (
        f"Legalább 2 issue template kell (bug report + feature request). "
        f"Jelenleg: {len(templates)}"
    )


def test_pr_template_exists():
    """A PR template létezik."""
    pr_paths = [
        REPO_ROOT / ".github" / "pull_request_template.md",
        REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
    ]
    assert any(p.is_file() for p in pr_paths), (
        "Hiányzik a .github/pull_request_template.md."
    )


def test_readme_mentions_license():
    """A README.md említi a licencet."""
    readme = REPO_ROOT / "README.md"
    if not readme.is_file():
        return

    content = readme.read_text().lower()
    assert "license" in content or "licenc" in content, (
        "A README.md-ben szerepeljen a licenc típus."
    )


def test_readme_mentions_contributing():
    """A README.md hivatkozik a CONTRIBUTING.md-re."""
    readme = REPO_ROOT / "README.md"
    if not readme.is_file():
        return

    content = readme.read_text().lower()
    assert "contributing" in content or "kontribút" in content or "hozzájárul" in content, (
        "A README.md-ben hivatkozz a CONTRIBUTING.md-re."
    )
