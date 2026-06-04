# Napa's Flooring — Notas de Sessão / Handoff SEO-GEO

> Última sessão: **2026-06-03** · Consultoria SEO/GEO (Claude)
> Retomar daqui na próxima sessão. Tudo que é código está commitado e no ar.

---

## 📍 Localização & stack

- **Repo local:** `C:\Users\lucia\Projetos\napasflooring`
- **GitHub:** https://github.com/lucianodornfeld18-creator/napasflooring (branch `main`)
- **Deploy:** Cloudflare Pages, auto-build a cada push na `main`
- **Site:** https://napasflooring.com
- **Plano de ação manual (HTML):** `C:\Users\lucia\Desktop\napas-acoes-manuais.html`
- **Script de auditoria:** `C:\Users\lucia\Projetos\_audit_napas.py` (gera `_audit_result.json`)

### Como buildar (Windows)
```
# Python = launcher "py" (NÃO "python"/"python3" — esses são alias da Store)
# Precisa de UTF-8 senão quebra no print final:
set PYTHONUTF8=1   (ou: export PYTHONUTF8=1 no bash)
py _build_home.py && py _build_pages.py && py _build_cities.py && py _build_services.py && py _build_blog.py && py _build_sitemap.py
```
- Fonte única de verdade: `_data.py` (negócio, cidades, serviços, preços, reviews, blog)
- Design system / schema / componentes: `_gen.py`
- Builders por seção: `_build_*.py` · **nunca editar HTML solto**, sempre editar fonte e rebuildar
- git `core.autocrlf=true` → arquivos no working tree são CRLF (normal)

---

## ✅ FEITO nesta sessão (3 commits na main)

1. **Google Tag GA4** `G-8G1FS3VQN5` nas 124 páginas (embutida no `head()` do `_gen.py`)
2. **robots.txt liberando 14 crawlers de IA** + **llms.txt** novo (gerador em `_build_sitemap.py`)
3. **Schema:** removido `aggregateRating` duplicado (estava em Organization E LocalBusiness); adicionado `streetAddress` (NAP completo)
4. **H1 corrigido** em about/contact/financing/warranty (bug: variável `hero` era criada mas nunca inserida no body)
5. **16 fotos `real-*.jpg` → WebP** (−42%, rotação EXIF corrigida) + refs atualizadas em `_build_home.py`
6. **Logos** com `width`/`height` reais (era `width="auto"` → causava CLS)
7. **Blog index** 801 → 1.158 palavras (conteúdo "answerable" p/ GEO)
8. **Build system portável** (paths `os.path.dirname(__file__)`, antes hardcoded `/home/claude/napas`)
9. **GBP ligado ao site:** `google_profile` e `google_review_url` = `https://share.google/6ZiLBnQqDXLEHQezV` (substituiu placeholder `g.page/napas-flooring` em 64 páginas)
10. **Facebook real** no schema sameAs: `https://www.facebook.com/p/Napas-Flooring-100070103477156/`

### Cloudflare (feito pelo Luciano no painel)
- ✅ "Block AI training bots" = **Do not block (allow crawlers)**
- ✅ "Manage your robots.txt" = **desligado** → parou de injetar `Content-Signal: ai-train=no`
- ✅ **Verificado ao vivo:** robots.txt agora limpo, todos os bots de IA com `Allow: /`

---

## ⏳ PENDENTE (ações manuais do Luciano)

Detalhes completos com campos copy-paste em: `Desktop\napas-acoes-manuais.html`

1. 🔴 **Search Console + Sitemap** (Luciano sabe fazer)
   - Propriedade (Domínio): `napasflooring.com` (verificar via TXT no DNS Cloudflare)
   - Enviar sitemap: `https://napasflooring.com/sitemap.xml`
   - Solicitar indexação da home + 3-4 city pages
2. 🔴 **Terminar o GBP** — categorias, áreas, horário, descrição, serviços "From", 15-20 fotos
   - Categoria primária: **Flooring Contractor**
   - ⚠️ Se endereço não for físico real → configurar **Service-Area Business** com endereço OCULTO
3. 🔴 **Diretórios** (NAP idêntico): Yelp, Bing Places, Apple Business Connect, BBB, Angi, Thumbtack, Houzz, HomeAdvisor, Nextdoor
4. 🟡 **Reviews:** roadmap 15 → 45 mantendo ≥4.9★
5. 🟡 **Decisão:** número local **941** (atual 407 é de Orlando)

---

## 🔧 O que Claude faz quando o Luciano voltar com os dados

| Luciano traz | Claude edita | Onde |
|---|---|---|
| Link direto "escrever avaliação" do GBP | `google_review_url` | `_data.py:40` |
| Links dos diretórios criados | `yelp`/`thumbtack`/`angi`/`houzz`/`bbb` (entram no `sameAs`) | `_data.py:43-47` |
| Instagram | `instagram` | `_data.py:42` |
| Decisão nº 941 | `phone`/`phone_display`/`phone_tel` (troca global) | `_data.py:15-17` |
| Fotos novas de jobs | converter p/ WebP + add na galeria | `images/` + `_build_home.py` |

**Sempre:** editar `_data.py` → `set PYTHONUTF8=1` → rodar os 6 `_build_*.py` → `git add -A && git commit && git push`.

---

## 📊 Estado da auditoria (baseline)

- 124 páginas · sitemap 122 URLs · 0 duplicatas de title/desc · 0 canonical errados
- 0 links quebrados reais (o "sms:" é falso positivo do crawler — URI válido)
- Schema: WebSite, Organization, LocalBusiness+HomeAndConstructionBusiness, BreadcrumbList, FAQPage, Article, Service — todos OK, 0 parse errors
- Word count saudável: city 2.784 · service 2.626 · service×city 2.785 (mediana)
- Profundidade máx. 2 cliques da home · nav/footer consistentes

## 🎯 Gap competitivo (resumo)
- SERP #1 atual (`bradentonflooringpros.com`) = referral raso, ~15 páginas, 1 depoimento
- Líder local (Manasota) = Yelp **2.4★** / Chamber 3.4★
- **Napa's ganha no on-site/conteúdo com folga.** O jogo está em GBP + diretórios + volume de reviews. Janela aberta.

---
*Segurança: nenhum segredo no repo. `access_key` do Web3Forms (contact) é público por design. Remote git sem token exposto.*
