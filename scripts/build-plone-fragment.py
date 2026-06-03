#!/usr/bin/env python3
"""
Gera docs/plone-fragmento.html a partir de index.html.

Remove header/footer, envolve o main em .hotsite-plone e substitui
br-accordion por details/summary (funciona sem core.min.js no Plone).
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
OUT = ROOT / "docs" / "plone-fragmento.html"

ACCORDION_PATTERN = re.compile(
    r'<div class="br-accordion">.*?</div>\s*(?=</section>)',
    re.DOTALL,
)

DETAILS_BLOCK = """          <div class="hotsite-details-group" role="group" aria-label="Contexto expandível">
            <details class="hotsite-details">
              <summary>Princípios e elementos do modelo (gp2)</summary>
              <div class="hotsite-details-body">
                <p><strong>Princípios fundamentais:</strong></p>
                <ul class="hotsite-compact-list">
                  <li>Facilidade de catalogação dos serviços</li>
                  <li>Replicabilidade por entes subnacionais</li>
                  <li>Estimativas conservadoras (subestimação dos impactos)</li>
                  <li>Atualização contínua de variáveis e resultados</li>
                </ul>
                <p><strong>Elementos incorporados dos estudos anteriores:</strong></p>
                <ul class="hotsite-compact-list">
                  <li>Padronização das etapas (rol pré-estabelecido)</li>
                  <li>Quantidade de documentos por serviço</li>
                  <li>Variáveis atualizáveis e séries históricas</li>
                  <li>Renda de usuários e de prestadores de serviço</li>
                </ul>
              </div>
            </details>
            <details class="hotsite-details">
              <summary>Histórico SGD</summary>
              <div class="hotsite-details-body">
                <ul class="hotsite-compact-list">
                  <li>
                    <strong>2019+</strong> — Mensuração da economia de custos na
                    digitalização
                  </li>
                  <li>
                    <strong>2020</strong> — Calculadora de Interoperabilidade
                    (CONECTAGOV)
                  </li>
                  <li>
                    <strong>2022</strong> — Guia Prático – Modelo de Custos de Serviços
                    Públicos (SGD)
                  </li>
                  <li>
                    <strong>2025</strong> — Relatório SGD/UFMG (impactos social,
                    econômico e ambiental da governo digital)
                  </li>
                  <li>
                    <strong>Atual</strong> — Referencial unificado (gp2), integrado ao
                    Portal Gov.br
                  </li>
                </ul>
              </div>
            </details>
            <details class="hotsite-details">
              <summary>Comparativo Guia 2022 × UFMG 2025</summary>
              <div class="hotsite-details-body">
                <p>
                  <strong>Guia Prático (SGD, 2022) —</strong> Positivos: padronização de
                  etapas; amplo catálogo; documentos por serviço; renda média; percentual
                  de atendimento digital. Atenção: pouca segmentação (transporte,
                  internet fixa/móvel); dependência de formulários aos gestores, com
                  estimativas heterogêneas.
                </p>
                <p>
                  <strong>Relatório SGD/UFMG (2025) —</strong> Positivos: fundamentação
                  teórica; georreferenciamento; variáveis atualizáveis; categorização por
                  renda e tipo de usuário; doses de tratamento. Atenção: formato
                  “cookbook”; alta individualização; aplicação a apenas
                  <strong>quatro serviços</strong>; georreferenciamento pouco escalável em
                  larga escala.
                </p>
              </div>
            </details>
            <details class="hotsite-details">
              <summary>Referencial SCM (internacional)</summary>
              <div class="hotsite-details-body">
                <p>
                  O <em>Standard Cost Model</em> (Holanda, início dos anos 2000) isolou
                  custos administrativos de cumprimento de obrigações de informação ao
                  Estado. Foi adotado pela Comissão Europeia (Better Regulation) e
                  recomendado pela OCDE — referência histórica para mensuração
                  regulatória, distinta do núcleo operacional deste modelo centrado nos
                  serviços digitais do Gov.br.
                </p>
              </div>
            </details>
            <details class="hotsite-details">
              <summary>Notas metodológicas e prudência (gp2)</summary>
              <div class="hotsite-details-body">
                <p><strong>Boas práticas:</strong> fontes oficiais (IBGE, Ipea, portais); simplificação de variáveis; prudência nas estimativas.</p>
                <p><strong>Medidas de prudência (exemplos):</strong></p>
                <ul class="hotsite-compact-list">
                  <li>Não contabilizar impressão pré-digitalização pelos usuários</li>
                  <li>Assumir que o usuário já possui os documentos exigidos</li>
                  <li>Custos físicos do governo (papel, energia pré-digital) só no pós-digitalização, quando aplicável</li>
                  <li>Mesma quantidade de documentos pré e pós quando a redução não é mensurada</li>
                </ul>
                <p>
                  <strong>IA (transitório):</strong> variáveis globais pesquisadas com LLM
                  multiagente (deep research) e revisão humana — sujeitas a novo estudo
                  aprofundado.
                </p>
              </div>
            </details>
          </div>"""

HEADER = """<!--
  Fragmento para Plone (editor Gov.br) — Novo Modelo de Custos
  Gerado por: python scripts/build-plone-fragment.py

  ANTES DE COLAR:
  1. Suba assets/css/hotsite.css como Arquivo no Plone e copie a URL de download.
  2. Substitua {{URL_HOTSITE_CSS}} abaixo pela URL absoluta (https://...).
  3. Se o tema NÃO carregar o DS, descomente os links opcionais e preencha {{URL_CORE_CSS}}.
  4. Cole no modo HTML da página (não cole index.html inteiro).

  Ver: docs/plone-publicacao.md
-->

<link rel="stylesheet" href="{{URL_HOTSITE_CSS}}" />

<!--
  Opcional — só se o tema do portal não incluir @govbr-ds/core 3.7:
<link rel="stylesheet" href="https://cdngovbr-ds.estaleiro.serpro.gov.br/design-system/fonts/rawline/css/rawline.css" />
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway:300,400,500,600,700,800,900&display=swap" />
<link rel="stylesheet" href="{{URL_CORE_CSS}}" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
-->

<div class="hotsite-plone">
"""


FOOTER = """
</div>
"""


def main() -> None:
    """Extrai main do index, aplica transformações e grava o fragmento Plone."""
    html = INDEX.read_text(encoding="utf-8")
    match = re.search(r"<main id=\"conteudo\">(.*?)</main>", html, re.DOTALL)
    if not match:
        raise SystemExit("Não foi possível localizar <main id=\"conteudo\"> em index.html")

    main_inner = match.group(1)
    main_inner, count = ACCORDION_PATTERN.subn(DETAILS_BLOCK, main_inner)
    if count > 1:
        raise SystemExit(f"Esperava no máximo 1 br-accordion, encontrados: {count}")

    body = (
        HEADER
        + f'  <main id="conteudo" class="hotsite-main">{main_inner}  </main>\n'
        + FOOTER
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(body, encoding="utf-8")
    print(f"Gerado: {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
