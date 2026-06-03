# Hotsite — Novo Modelo de Custos (draft)

Página HTML estática para apresentação do **Modelo de Custos Aplicado à Digitalização** (SGD), usando o [Design System Gov.br](https://www.gov.br/ds/) 3.7 via CDN.

## Documentos fonte

| Arquivo | Papel |
|---------|--------|
| [`docs/nmc.docx`](docs/nmc.docx) | **Narrativa** — roteiro em slides (estrutura do hotsite) |
| [`docs/gp2.docx`](docs/gp2.docx) | **Referência técnica** — conteúdo validado factualmente no HTML |
| [`docs/gemini-code-1780508976849.md`](docs/gemini-code-1780508976849.md) | Prompt de reestruturação das seções |

## Conteúdo do repositório

| Arquivo | Descrição |
|---------|-----------|
| [`index.html`](index.html) | Hotsite: 7 seções (hero, breve histórico, integração, serviço, motor, indicadores, transparência) |
| [`assets/css/hotsite.css`](assets/css/hotsite.css) | Diagramas e componentes complementares ao DS |
| [`scripts/build-plone-fragment.py`](scripts/build-plone-fragment.py) | Gera o fragmento Plone a partir do index.html |
| [`scripts/build-report-docx.py`](scripts/build-report-docx.py) | Gera o relatório de negócio `.docx` a partir do conteúdo do hotsite |
| [`docs/relatorio-modelo-custos.docx`](docs/relatorio-modelo-custos.docx) | Relatório de negócio (documento Word) com as 7 seções do hotsite |
| [`docs/resumo-guia.md`](docs/resumo-guia.md) | Mapa NMC × GP2 e registro de enriquecimentos |
| [`docs/nmc-extracted.txt`](docs/nmc-extracted.txt) | Texto extraído do nmc.docx |
| [`docs/gp2-extracted.txt`](docs/gp2-extracted.txt) | Texto extraído do gp2.docx |
| [`docs/plone-fragmento.html`](docs/plone-fragmento.html) | Fragmento HTML para colar no Plone |
| [`docs/plone-publicacao.md`](docs/plone-publicacao.md) | Guia de publicação no Plone (editor Gov.br) |

## Publicação no Plone

O `index.html` completo **não** deve ser colado no Plone (o editor descarta o `<head>` e quebra caminhos relativos).

1. Siga o guia [`docs/plone-publicacao.md`](docs/plone-publicacao.md) (verificar tema, subir `hotsite.css`, colar fragmento).
2. Use [`docs/plone-fragmento.html`](docs/plone-fragmento.html) e substitua `{{URL_HOTSITE_CSS}}` pela URL do arquivo no portal.
3. Após alterar o hotsite localmente, regenere o fragmento: `python scripts/build-plone-fragment.py`.

## Como visualizar

```powershell
Set-Location "D:\14-Desenvolvimento\Projetos-VibeCoding-IA\modelo-custos-page"
python -m http.server 8080
```

Abra `http://127.0.0.1:8080/index.html` (requer internet para CDN).

## Relatório de negócio (.docx)

O arquivo [`docs/relatorio-modelo-custos.docx`](docs/relatorio-modelo-custos.docx) reproduz o conteúdo do hotsite como um documento apresentável (título + 7 seções, estilo corporativo neutro). Para regenerá-lo após alterar o conteúdo:

```powershell
pip install python-docx
python scripts/build-report-docx.py
```

## Estrutura da página

1. **Início** (`#hero`) — Modelo de Custos da Transformação Digital  
2. **Breve Histórico** (`#historico`) — SCM, marcos da SGD (2019-2025) e consolidação  
3. **Integração Gov.br** (`#integracao`) — Automação e evolução orgânica (3 cards)  
4. **O serviço** (`#servico`) — 4 etapas: Buscar, Coletar, Solicitar, Receber  
5. **Motor técnico** (`#motor`) — 5 passos (JSON, léxico, spaCy/XGBoost, mensuração, BI)  
6. **Indicadores** (`#indicadores`) — Prudência + econômico/social/ambiental  
7. **Transparência** (`#transparencia`) — Power BI, filtros, replicabilidade  
