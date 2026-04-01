from __future__ import annotations

from pathlib import Path


def test_compose_starts_app_with_milvus_dependency() -> None:
    compose_content = Path("docker-compose.yml").read_text(encoding="utf-8")

    assert "app:" in compose_content
    assert "standalone:" in compose_content
    assert "depends_on:" in compose_content
    assert "condition: service_healthy" in compose_content
    assert "MILVUS_HOST: standalone" in compose_content
    assert "MILVUS_PORT: 19530" in compose_content
