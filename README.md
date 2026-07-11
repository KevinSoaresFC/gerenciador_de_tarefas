# TechFlow Solutions - Sistema de Gestão de Cargas e Tarefas Logísticas

Este projeto consiste em um sistema de gerenciamento de tarefas desenvolvido para uma startup de logística. O objetivo principal é permitir o acompanhamento do fluxo de trabalho em tempo real, a priorização de tarefas críticas e o monitoramento do desempenho da equipe operativa.

O projeto foi construído aplicando conceitos fundamentais de Engenharia de Software, utilizando versionamento semântico, testes automatizados e integração contínua (CI).

---

## 📋 Escopo Inicial do Projeto

O sistema foi planejado inicialmente para cobrir as operações básicas de controle de fluxo de cargas através de um CRUD (Create, Read, Update, Delete) em memória. As principais funcionalidades mapeadas foram:
* **Cadastrar Tarefas:** Registrar novas demandas logísticas (ex: Carregamento, Entrega, Separação).
* **Listar Tarefas:** Visualizar a esteira de trabalho em tempo real.
* **Atualizar Status:** Mover tarefas entre os estados operacionais.
* **Remover Tarefas:** Cancelar ou arquivar registros.

---
``
## ⚙️ Metodologia Ágil Adotada

Para a gestão deste projeto, foi adotada uma abordagem ágil **Híbrida (Scrum + Kanban)**:
* **Kanban:** Utilizado através da aba *Projects* do GitHub para dar visibilidade total ao fluxo de trabalho nas colunas **To Do** (A Fazer), **In Progress** (Em Progresso) e **Done** (Concluído).
* **Scrum:** Divisão das metas de desenvolvimento em incrementos funcionais (representados pelos commits e issues rastreáveis), garantindo entregas rápidas e feedback contínuo.

---

## ⚠️ Gestão de Mudanças (Alteração de Escopo)

> **Justificativa de Negócio:** Durante o ciclo de desenvolvimento, a startup de logística identificou a necessidade crítica de diferenciar o tratamento de cargas comuns de **cargas perecíveis**, que correm risco de perda. 
> 
> **Adaptação:** O escopo inicial foi alterado para incluir uma propriedade de **Prioridade Crítica** no modelo de dados. Essa alteração foi documentada no Backlog do produto, gerando um novo card no quadro Kanban e uma nova suíte de testes automatizados para validar a regra de negócio emergencial.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.10+
* **Controle de Qualidade / Testes:** PyTest
* **Integração Contínua (CI):** GitHub Actions
* **Gestão do Projeto:** GitHub Projects (Kanban)

---