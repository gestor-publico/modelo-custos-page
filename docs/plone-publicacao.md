# Publicação no Plone (editor Gov.br)

Guia para integrar o hotsite **sem perder estilos**, com acesso apenas de **editor de conteúdo** (sem alterar tema global).

## Arquivos deste repositório

| Arquivo | Uso |
|---------|-----|
| [`plone-fragmento.html`](plone-fragmento.html) | HTML para colar no campo da página (modo código-fonte) |
| [`../assets/css/hotsite.css`](../assets/css/hotsite.css) | Enviar ao Plone como **Arquivo** |
| [`../scripts/build-plone-fragment.py`](../scripts/build-plone-fragment.py) | Regenerar o fragmento após mudanças no `index.html` |

---

## 1. Verificar o que o tema já carrega

Antes de publicar, abra **qualquer página interna** do mesmo portal e use as ferramentas do navegador (F12 → **Rede** / Network). Recarregue a página e procure:

| Recurso | O que procurar | Se encontrar |
|---------|----------------|--------------|
| CSS do DS | `core.min.css`, `@govbr-ds`, `govbr-ds` | **Não** descomente `{{URL_CORE_CSS}}` no fragmento |
| JS do DS | `core.min.js` | Accordion nativo do DS pode funcionar em outras páginas; o fragmento usa `<details>` e **não depende de JS** |
| Fontes | `rawline.css`, `Raleway` | Opcional descomentar links de fonte no fragmento |
| Ícones | `font-awesome`, `fas fa-` | Se ícones aparecem quebrados, descomente o link Font Awesome no fragmento |

**Teste rápido:** em outra página do site, existe botão ou card com classe `br-button` / `br-card` estilizado? Se sim, o tema provavelmente já inclui o DS 3.x.

Anote a versão se aparecer na URL (ideal: **3.7.0**, igual ao [`index.html`](../index.html)).

---

## 2. Publicar o CSS no Plone

1. No ZMI ou interface de conteúdo, vá à pasta onde ficará a página (ex.: `modelo-de-custos`).
2. **Adicionar → Arquivo** (ou equivalente).
3. Envie o arquivo [`assets/css/hotsite.css`](../assets/css/hotsite.css).
4. Publique o arquivo.
5. Copie a **URL absoluta de download** (ex.: `https://www.seuorgao.gov.br/portal/.../hotsite.css/@@download/file/hotsite.css`).

Guarde essa URL — substituirá `{{URL_HOTSITE_CSS}}` no fragmento.

### Se o tema não carregar o Design System

Baixe no computador (uma vez):

- CSS: https://cdn.jsdelivr.net/npm/@govbr-ds/core@3.7.0/dist/core.min.css  
- (Opcional) JS: https://cdn.jsdelivr.net/npm/@govbr-ds/core@3.7.0/dist/core.min.js  

Envie cada um como **Arquivo** no Plone e use a URL de download em `{{URL_CORE_CSS}}` (e no script, se necessário). Muitos portais **bloqueiam** jsDelivr no corpo da página — hospedar no portal é mais confiável.

---

## 3. Preparar e colar o fragmento

1. Abra [`plone-fragmento.html`](plone-fragmento.html) em um editor de texto.
2. Substitua `{{URL_HOTSITE_CSS}}` pela URL absoluta do passo 2.
3. Se necessário, descomente o bloco de links opcionais no topo e preencha `{{URL_CORE_CSS}}`.
4. Crie ou edite uma **Página** no Plone.
5. No editor, mude para **HTML / código-fonte** (não apenas visual).
6. Cole **todo** o conteúdo do fragmento (do comentário inicial até `</div>` final).
7. Salve e publique.

**Não cole** o `index.html` inteiro: o Plone descarta `<head>`, quebra `assets/css/...` e duplica cabeçalho/rodapé do tema.

### Se o sanitizador remover `<link>`

- Cole o conteúdo de `hotsite.css` dentro de `<style>...</style>` no início do bloco, **ou**
- Peça à equipe de TI liberar `<link rel="stylesheet">` para URLs do próprio portal.

---

## 4. Regenerar o fragmento (após editar o hotsite)

```powershell
Set-Location "D:\14-Desenvolvimento\Projetos-VibeCoding-IA\modelo-custos-page"
python scripts/build-plone-fragment.py
```

Depois, repita a substituição de `{{URL_HOTSITE_CSS}}` antes de colar no Plone.

---

## 5. Checklist de validação

Após publicar, confira na página ao vivo:

- [ ] Tipografia e cores dos componentes `.br-card`, `.br-message`
- [ ] Diagramas de fluxo (`.hotsite-flow`, `.hotsite-stepper`) e cards 3 colunas (`.hotsite-grid--3`)
- [ ] Seções renderizadas: `#hero`, `#integracao`, `#servico`, `#motor`, `#indicadores`, `#transparencia`
- [ ] Ícones Font Awesome visíveis (se o tema não os trouxer, descomente o link no fragmento)

---

## Referências oficiais do DS Gov.br 3.7

| Recurso | URL |
|---------|-----|
| Rawline (CDN Serpro) | `https://cdngovbr-ds.estaleiro.serpro.gov.br/design-system/fonts/rawline/css/rawline.css` |
| Raleway | `https://fonts.googleapis.com/css?family=Raleway:300,400,500,600,700,800,900&display=swap` |
| Core CSS (download / hospedar) | `https://cdn.jsdelivr.net/npm/@govbr-ds/core@3.7.0/dist/core.min.css` |
| Font Awesome 5 | `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css` |
| Roteiro DS | https://gov.br/ds/wiki/desenvolvimento/guias/roteiro/ |

O preview local continua em [`index.html`](../index.html) (com header/footer e `br-accordion` + JS).
