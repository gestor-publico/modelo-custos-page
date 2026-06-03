# Resumo do hotsite — narrativa NMC + referência GP2

> **Narrativa (eixo):** [`nmc.docx`](nmc.docx) — roteiro em slides.  
> **Referência técnica / validação factual:** [`gp2.docx`](gp2.docx).  
> **Página:** [`index.html`](../index.html)

## Visão em 1 parágrafo

O **Modelo de Custos Aplicado à Digitalização** (SGD, 2020–2025) usa o **Gov.br** e a **API JSON do Estaleiro** como fonte primária, classifica etapas do Portal em macroetapas **Solicitar/Receber** (sobre um rol de **4 etapas** técnicas), combina variáveis Grupo 1 e 2 + **API de Avaliação** (proxy CGAUX), e calcula economia **por serviço** (digital vs presencial), com painéis Power BI e indicadores econômicos, sociais e ambientais.

## Estrutura atual (narrativa Gemini) → seções do hotsite

A página foi reestruturada conforme [`gemini-code-1780508976849.md`](gemini-code-1780508976849.md), em seções sequenciais.

| Seção HTML | Título | Conteúdo |
|------------|--------|----------|
| `#hero` | Modelo de Custos da Transformação Digital | Subtítulo, apoio (SGD/impactos), mini fluxo Gov.br→JSON→Modelo |
| `#historico` | Breve Histórico | Origem do SCM (Holanda/OCDE) e timeline da SGD: 2019, CONECTAGOV 2020, Guia 2022, UFMG 2025, referencial unificado |
| `#integracao` | Automação e Evolução Orgânica | 3 cards: sem formulários, precisão evolutiva, atualização mensal |
| `#servico` | O Serviço como Pilar Central | 4 etapas: Buscar, Coletar, Solicitar, Receber |
| `#motor` | Engenharia e Operacionalização | 5 passos técnicos (JSON, léxico, spaCy/XGBoost, mensuração, BI) |
| `#indicadores` | Mensuração Além dos Custos Financeiros | Prudência + 3 pilares (econômico/social/ambiental) |
| `#transparencia` | Tomada de Decisão Baseada em Evidências | Power BI, filtros, replicabilidade subnacional |

> Conteúdo complementar do gp2 (variáveis Grupo 1/2, histórico SGD, comparativo, SCM, prudência) permanece registrado em [`gp2-extracted.txt`](gp2-extracted.txt) e neste resumo, mas não compõe mais a página.

> Termos técnicos (spaCy, modelo `pt_core_news_lg`, XGBoost, Power BI) validados em [`gp2-extracted.txt`](gp2-extracted.txt).

## Enriquecimento gp2 (revisão factual)

| Bloco | Trechos gp2 incorporados |
|-------|-------------------------|
| Hero | Título oficial; 2020–2025; subnacionais; transparência; prudência |
| `#paradigma` | Página serviços; API `servicos-json`; CONECTAGOV; IBGE/Ipea |
| `#macroetapas` | Rol Buscar/Coletar/Solicitar/Receber; descrições pré/pós |
| `#mensuracao` | Grupo 1/2; CGAUX; extrapolação; renda usuário/prestador |
| `#macrofluxo` | Matriz de serviços; dicionário; soma por ente; extrapolação |
| `#resultados` | Mês nos filtros; bem-estar, congestão, assimetria, ambientais; exportação |
| `#contexto` | 4 princípios; 4 elementos; comparativo detalhado; 4 serviços UFMG; medidas prudência; IA |

## Correções factuais aplicadas

- Relatório UFMG: impactos **social, econômico e ambiental** (não só “governo digital” genérico).
- Volume: proxy **avaliações / planilha CGAUX** (gp2).
- UFMG: amostra de **quatro serviços** explicitada no comparativo.
- Painel: filtro **mês** incluído (gp2).

## Estrutura mantida (sem reexpandir)

- 6 âncoras de navegação; sem tabela comparativa no corpo; sem fórmulas (1)–(13).

---

*Extrações:* [`nmc-extracted.txt`](nmc-extracted.txt) · [`gp2-extracted.txt`](gp2-extracted.txt)
