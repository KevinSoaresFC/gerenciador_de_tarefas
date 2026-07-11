import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.task_manager import TaskManager


def test_create_task_success():
    manager = TaskManager()
    task = manager.create_task("Carga Perecível", "Entrega na Zona Sul", priority="Crítica")
    assert task["id"] == 1
    assert task["title"] == "Carga Perecível"
    assert task["priority"] == "Crítica"
    assert task["status"] == "A Fazer"

def test_create_task_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.create_task("", "Descrição da Carga")

def test_update_status_success():
    manager = TaskManager()
    manager.create_task("Descarregar Carga", "Doca 4")
    updated_task = manager.update_status(1, "Em Progresso")
    assert updated_task["status"] == "Em Progresso"

def test_delete_task_success():
    manager = TaskManager()
    manager.create_task("Remessa Cancelada", "Doca 2")
    deleted_task = manager.delete_task(1)
    assert deleted_task["id"] == 1
    assert len(manager.read_tasks()) == 0