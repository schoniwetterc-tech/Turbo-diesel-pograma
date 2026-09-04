# 🚦 Radar de Fluxo

## Sistema Inteligente de Orquestração Dinâmica de Ordens de Serviço

Projeto desenvolvido para a empresa **Turbo Diesel**, com o objetivo de melhorar o planejamento, a organização e o acompanhamento das Ordens de Serviço (O.S.).

---

## 📌 Sobre o projeto

O **Radar de Fluxo** é um sistema desenvolvido para auxiliar na organização das Ordens de Serviço, buscando identificar possíveis atrasos, gargalos e sobrecargas de recursos.

A proposta é analisar as O.S. e auxiliar na decisão de:

- Qual O.S. deve ser executada primeiro;
- Quais serviços apresentam maior risco de atraso;
- Onde estão os gargalos do processo;
- Se a capacidade dos recursos disponíveis será suficiente;
- Como reorganizar a fila quando ocorrerem imprevistos.

O sistema busca transformar o planejamento de O.S. em um processo mais **dinâmico, previsível e orientado por dados**.

---

## 🎯 Objetivo

Desenvolver um sistema capaz de analisar as Ordens de Serviço e auxiliar na tomada de decisões relacionadas à:

- Priorização;
- Sequenciamento;
- Capacidade produtiva;
- Identificação de gargalos;
- Previsão de atrasos;
- Reprogramação da fila de serviços.

---

## ⚙️ Como o sistema funciona

O fluxo proposto é:

```text
Entrada da O.S.
       ↓
Classificação e prioridade
       ↓
Estimativa de tempo
       ↓
Verificação de peças e dependências
       ↓
Análise de capacidade
       ↓
Identificação de gargalos
       ↓
Sequenciamento das O.S.
       ↓
Execução
       ↓
Atualização dos dados
       ↓
Reprogramação dinâmica

# ROADMAP DE DESENVOLVIMENTO

## V4 — Estruturação da Base Operacional

* Melhorar a estrutura do banco de dados.
* Organizar o cadastro de recursos.
* Melhorar o cadastro das O.S.
* Registrar informações operacionais.
* Preparar os dados para cálculo de capacidade.
* Preparar os dados para cálculo de risco.
* Preservar as funcionalidades existentes da V3.

### Banco de Dados

* `orders`

  * id
  * cliente
  * serviço
  * prioridade
  * prazo
  * tempo estimado
  * tempo real
  * status
  * risco
  * peças
  * mecânico
  * bancada
  * data de criação
  * data de início
  * data de término
  * tempo de espera por peças
  * bloqueio
  * motivo do bloqueio

* `resources`

  * mecânicos
  * bancadas
  * bancada de testes

### Recursos

* 4 mecânicos.
* 3 bancadas de trabalho.
* 1 bancada de testes.

### Capacidade

* Segunda a sexta: 40 horas semanais.
* Sábado: 4 horas disponíveis.
* Capacidade semanal por mecânico: 44 horas.

---

# V4.1 — Indicadores e Análise Operacional

* Transformar os indicadores do Dashboard em dados calculados pelo banco.
* Calcular O.S. ativas.
* Calcular O.S. atrasadas.
* Calcular O.S. em risco.
* Calcular O.S. aguardando peças.
* Calcular carga de trabalho.
* Calcular capacidade disponível.
* Calcular utilização dos recursos.
* Identificar recursos próximos da saturação.
* Criar classificação inicial de risco.
* Registrar tempo real de execução.
* Registrar tempo de espera.
* Registrar bloqueios.
* Registrar motivos de bloqueio.

### Classificação de Utilização

* 0%–74% → Normal
* 75%–89% → Atenção
* 90% ou mais → Crítico

### Classificação Inicial de Risco

Considerar:

* prioridade;
* prazo;
* tempo estimado;
* peças pendentes;
* bloqueios;
* utilização dos recursos;
* tamanho das filas.

---

# V4.2 — Motor de Prioridade e Sequenciamento

* Criar Índice de Prioridade.
* Criar pontuação para cada O.S.
* Considerar prioridade.
* Considerar prazo.
* Considerar risco.
* Considerar tempo estimado.
* Considerar disponibilidade de peças.
* Considerar disponibilidade de mecânicos.
* Considerar disponibilidade de bancadas.
* Considerar filas.
* Considerar impacto sobre gargalos.
* Gerar ranking das O.S.
* Recomendar a próxima O.S. a ser executada.
* Exibir justificativa da recomendação.

### Exemplo

```text
1º O.S. 2490
2º O.S. 2491
3º O.S. 2487
```

A justificativa deverá indicar os fatores que levaram determinada O.S. a receber maior prioridade.

---

# V4.3 — Radar de Gargalos Inteligente

* Detectar automaticamente gargalos.
* Analisar utilização dos mecânicos.
* Analisar utilização das bancadas.
* Analisar utilização da bancada de testes.
* Analisar tamanho das filas.
* Analisar tempo de espera.
* Detectar O.S. bloqueadas.
* Detectar peças pendentes.
* Identificar recursos saturados.
* Identificar excesso de carga.
* Identificar O.S. afetadas pelos gargalos.

### Informações apresentadas

```text
Recurso
Utilização
Fila
O.S. afetadas
Situação
Possível impacto
```

---

# V4.4 — Simulação de Cenários

* Criar simulação da sequência atual.
* Criar simulação de uma sequência reorganizada.
* Comparar diferentes sequenciamentos.
* Comparar quantidade de O.S. atrasadas.
* Comparar utilização dos recursos.
* Comparar capacidade disponível.
* Avaliar utilização do sábado.
* Avaliar cenários combinados.

### Cenários

```text
Cenário A — Sequência atual

Cenário B — Sequenciamento reorganizado

Cenário C — Utilização do sábado

Cenário D — Sequenciamento + sábado
```

### Comparação

```text
O.S. atrasadas
Capacidade utilizada
Recursos críticos
Carga prevista
Risco de atraso
```

---

# V4.5 — Reprogramação Dinâmica

* Permitir atualização do planejamento.
* Reprogramar quando uma peça atrasar.
* Reprogramar quando uma O.S. for bloqueada.
* Reprogramar quando um mecânico ficar indisponível.
* Reprogramar quando uma bancada ficar indisponível.
* Reprogramar quando o tempo real ultrapassar o estimado.
* Recalcular capacidade.
* Recalcular riscos.
* Recalcular prioridades.
* Gerar nova sequência.

### Fluxo

```text
Imprevisto
↓
Atualização da O.S.
↓
Atualização dos recursos
↓
Recalculo da capacidade
↓
Recalculo do risco
↓
Novo sequenciamento
↓
Nova recomendação
```

---

# V4.6 — Indicadores e Relatórios Avançados

* Criar histórico operacional.
* Melhorar os relatórios.
* Criar indicadores de desempenho.
* Criar análises por período.
* Criar análise de atrasos.
* Criar análise de lead time.
* Criar análise de utilização dos recursos.
* Criar análise de tempo de espera.
* Criar análise de bloqueios.
* Criar análise de retrabalho.
* Identificar os principais motivos de atraso.

### Indicadores

* Total de O.S.
* O.S. concluídas.
* O.S. atrasadas.
* Percentual de atraso.
* Lead time médio.
* Tempo médio de execução.
* Tempo médio de espera.
* Utilização dos recursos.
* Capacidade utilizada.
* Capacidade ociosa.
* Quantidade de bloqueios.
* Tempo total de bloqueio.
* Retrabalho.

---

# V5 — Machine Learning

* Estruturar histórico suficiente das O.S.
* Preparar os dados para treinamento.
* Avaliar modelos estatísticos.
* Criar previsão de tempo de execução.
* Criar previsão de risco de atraso.
* Identificar padrões de execução.
* Comparar previsão com tempo real.
* Melhorar continuamente as estimativas.

### Dados utilizados

* tipo de serviço;
* tempo estimado;
* tempo real;
* prazo;
* prioridade;
* mecânico;
* bancada;
* peças;
* tempo de espera;
* bloqueios;
* retrabalho;
* início;
* término.

### Aplicações

```text
Histórico das O.S.
↓
Processamento dos dados
↓
Modelo estatístico / ML
↓
Previsão
↓
Atualização do planejamento
```

---

# V6 — Arquitetura Multiusuário

* Avaliar migração do SQLite local para banco centralizado.
* Criar API.
* Permitir múltiplos usuários.
* Criar autenticação.
* Criar controle de permissões.
* Centralizar os dados.
* Permitir acesso simultâneo.
* Avaliar criação de dashboard web.
* Separar interface, API e banco de dados.

### Arquitetura futura

```text
Interface
    ↓
API
    ↓
Banco de Dados
    ↓
Motor de Planejamento
    ↓
Análise / Previsões
```

---

# ORDEM DE IMPLEMENTAÇÃO

```text
V4
↓
Estrutura do banco e recursos

V4.1
↓
Indicadores e capacidade real

V4.2
↓
Prioridade e sequenciamento

V4.3
↓
Detecção automática de gargalos

V4.4
↓
Simulação de cenários

V4.5
↓
Reprogramação dinâmica

V4.6
↓
Histórico e relatórios avançados

V5
↓
Machine Learning

V6
↓
Arquitetura multiusuário
```

