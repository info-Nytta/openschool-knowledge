"""
Modul 6 — Éles üzem: Production konfiguráció verifikáció.
Ellenőrzi, hogy a deployment fájlok és konfigurációk készen állnak.
"""

from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent.parent


def test_docker_compose_prod_exists():
    """A docker-compose.prod.yml létezik."""
    assert (REPO_ROOT / "docker-compose.prod.yml").is_file(), (
        "Hiányzik a docker-compose.prod.yml."
    )


def test_prod_compose_has_restart_policy():
    """A production compose fájlban van restart policy."""
    compose_file = REPO_ROOT / "docker-compose.prod.yml"
    if not compose_file.is_file():
        assert False, "Hiányzik a docker-compose.prod.yml."

    with open(compose_file) as f:
        data = yaml.safe_load(f)

    services = data.get("services", {})
    for name, config in services.items():
        restart = config.get("restart")
        assert restart is not None, (
            f"A '{name}' service-nek legyen restart policy-ja "
            f"a docker-compose.prod.yml-ben (pl. restart: always)."
        )


def test_nginx_config_exists():
    """Az nginx konfiguráció létezik."""
    nginx_paths = [
        REPO_ROOT / "nginx" / "nginx.conf",
        REPO_ROOT / "nginx" / "default.conf",
    ]
    assert any(p.is_file() for p in nginx_paths), (
        "Hiányzik az nginx/nginx.conf."
    )


def test_cd_workflow_exists():
    """A GitHub Actions CD workflow létezik."""
    workflows_dir = REPO_ROOT / ".github" / "workflows"
    if not workflows_dir.is_dir():
        assert False, "Hiányzik a .github/workflows/ mappa."

    workflow_files = list(workflows_dir.glob("*.yml")) + list(workflows_dir.glob("*.yaml"))
    workflow_names = [f.stem for f in workflow_files]
    assert "cd" in workflow_names or "deploy" in workflow_names, (
        "Hiányzik a .github/workflows/cd.yml (vagy deploy.yml). "
        "Hozd létre a CD pipeline-t."
    )


def test_env_prod_not_committed():
    """A .env.prod NEM role a repóban (biztonsági ellenőrzés)."""
    gitignore = REPO_ROOT / ".gitignore"
    if gitignore.is_file():
        content = gitignore.read_text()
        assert ".env.prod" in content or ".env*" in content or ".env" in content, (
            "A .env.prod nincs a .gitignore-ban! "
            "A production környezeti változók ne kerüljenek a repóba."
        )


def test_backup_script_exists():
    """A backup script létezik."""
    backup_paths = [
        REPO_ROOT / "scripts" / "backup.sh",
        REPO_ROOT / "scripts" / "backup.py",
    ]
    assert any(p.is_file() for p in backup_paths), (
        "Hiányzik a scripts/backup.sh (vagy .py). "
        "Hozd létre a PostgreSQL backup scriptet."
    )


def test_prod_compose_no_exposed_db_port():
    """A production compose-ban a DB port ne legyen kívülre nyitva."""
    compose_file = REPO_ROOT / "docker-compose.prod.yml"
    if not compose_file.is_file():
        return  # Már leellenőriztük máshol

    with open(compose_file) as f:
        data = yaml.safe_load(f)

    db_config = data.get("services", {}).get("db", {})
    ports = db_config.get("ports", [])
    assert len(ports) == 0, (
        "A production compose-ban a db service-nek NE legyenek kívülre "
        "nyitott portjai (biztonsági kockázat). Távolítsd el a ports: részt."
    )
