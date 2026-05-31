# Дизайн 2026: как делать классно (ресёрч)

Синтез шести направлений глубокого веб-ресёрча о том, как в 2026 производить премиальный, не-generic веб-дизайн с помощью AI в Claude Code. Все ссылки сохранены, уверенность/хайп помечены честно.

---

## TL;DR

- **Generic — это математика, а не плохой промпт.** Generative-модели оптимизируют среднюю точность → output регрессирует к центроиду датасета (Inter, purple→blue градиент, centered-hero+3-cards). Подтверждено академически (arXiv 2503.01033, MIT). Вывод: бороться надо **внешними ограничениями + референсами**, а не «лучшими словами». [confidence: high]
- **Ни один prompt-to-app тул сам по себе не даёт «вау».** v0/Lovable/Bolt/Stitch/Replit все тянут к shadcn+Tailwind дефолту. Премиальность даёт **процесс**: залоченное направление + свои токены/референсы → тул как сырьё → перекрас → визуальный критик-луп. [confidence: high]
- **Главный недостающий рычаг — грундинг на РЕАЛЬНЫЕ референсы и DESIGN.md в корне репо.** Mobbin MCP (621k живых экранов, отдаёт base64 для multimodal) / Refero MCP + skill + DESIGN.md (реальные CSS-токены Stripe/Linear/Vercel) бьют скриншоты, потому что дают точные значения, а не интерпретацию. [confidence: medium-high]
- **Screenshot-критик-луп работает, но НЕ как self-review.** Anthropic прямо пишет: агент уверенно хвалит свой мусор. Нужен **отдельный generator/evaluator split** — субагент-судья смотрит реальный рендер через Playwright/Chrome DevTools MCP по 4 калиброванным критериям. [confidence: high]
- **Цвет и моушен — детерминируй, не «подбирай на глаз».** OKLCH+APCA (Harmonizer) дают предсказуемый контраст без ручной подстройки. Числа моушена Эмила Ковальски (durations <300ms, кастомные cubic-bezier, только transform/opacity) — точные значения, которые AI сам не выдаёт. [confidence: high]
- **Лицензионный подарок года: GSAP стал 100% бесплатным** (Webflow, апрель 2025) включая SplitText/ScrollTrigger/MorphSVG. Awwwards-tier scroll-сторителлинг теперь бесплатно. [confidence: high]
- **Стек уже на 70% собран.** Chrome DevTools + Playwright MCP, impeccable, taste-skill, shadcnblocks, frontend-design стоят. Не хватает: design-review субагента (gstack-стиль), грундинга на референсы (Mobbin/Refero), привычки класть DESIGN.md в корень, Vercel agent-skills как QA-gate. [confidence: high]

---

## Рекомендованный стек/тулчейн (ранжированно)

### AI-генераторы дизайна (внешние тулы — как СЫРЬЁ, не финал)

| # | Тул | Роль | Ссылка | Conf. |
|---|-----|------|--------|-------|
| 1 | **v0 (Vercel)** | Лучший ЧИСТЫЙ код (shadcn/Tailwind/TS, production). Визуал «serious/conventional» — обязательно перекрашивать под токены | https://v0.dev | high |
| 2 | **Subframe** | Визуальный редактор поверх настоящих React+Tailwind, MCP для Claude Code + CLI sync, работа от ТВОИХ токенов. Системная премиальность, не творческое вау | https://www.subframe.com | high |
| 3 | **Google Stitch** | Самый высокий визуальный потолок среди free-тулов (Gemini 3), 350 ген/мес бесплатно. Для исследования НАПРАВЛЕНИЯ, не для прод-кода (HTML/CSS сырой) | https://stitch.withgoogle.com | medium |
| 4 | **Lovable** | Самые полишенные дефолты + двусторонний GitHub-sync + Supabase. Но «more shine and sparkles», generic. Проверять RLS вручную | https://lovable.dev | high |
| 5 | **Framer AI** | Реально красивые сайты с motion (близко к Awwwards), НО код заперт в рантайме. Только как **референс-генератор** | https://www.framer.com | medium |
| – | **Magic Patterns** | Промпт/скриншот → React под ТВОЮ дизайн-систему | https://www.magicpatterns.com | medium |
| – | **Bolt.new / Replit** | Про скорость и бэкенд, дизайн вторичен. Низкий приоритет для премиум-UI | https://bolt.new · https://replit.com | high |
| – | **Onlook** (open-source) | «Cursor для дизайнеров»: bi-directional sync с ТВОИМ React/Next кодом, локально, бесплатно | https://onlook.com | medium |

**Вывод по генераторам:** screenshot-to-code (v0/Bolt/Lovable/Codia) НЕ pixel-perfect — дают 80% каркаса, последние 20% деградируют код за итерации. Codia «95% accuracy» = маркетинг [confidence: high]. Использовать как стартер каркаса, не как источник дизайна.

### Claude Code: skills / MCP / субагенты

**Поставить (ранжировано по рычагу):**

| # | Что | Тип | Зачем | Ссылка | Conf. |
|---|-----|-----|-------|--------|-------|
| 1 | **Vercel agent-skills** (web-design-guidelines + react-best-practices + composition-patterns + react-view-transitions) | Skills | Сильнейший QA/perf-gate 2026. Закрывает дыру по React-производительности и composition. ~27k звёзд, MIT | https://github.com/vercel-labs/agent-skills | high |
| 2 | **gstack design-review** (Garry Tan / YC) | Skill | Готовый screenshot-critic loop: 80-пунктный аудит + числовой AI Slop Score + автофиксы атомарными коммитами с before/after | https://github.com/garrytan/gstack | high |
| 3 | **Mobbin MCP** | MCP | Грундинг на 621k реальных экранов, отдаёт base64 (видно multimodal). Прямой фикс dataset-mean. Запуск 12 мая 2026 | https://chatforest.com/reviews/mobbin-mcp-server/ | medium |
| 4 | **Refero MCP + refero_skill** | MCP+Skill | Research-first процесс с reference-lock + anti-slop + craft-знания. 130-150k экранов | https://github.com/referodesign/refero_skill | medium |
| 5 | **UI-UX-Pro-Max** (85.5k звёзд) | Skill/plugin | Анти-slop источник решений: 67 стилей, 161 палитра, 57 пар шрифтов под нишу. Для aesthetic-lock | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | high |
| 6 | **VoltAgent ui-designer + design-bridge** | Субагенты | Изолированное дизайн-рассуждение в отдельном контексте (бережёт основной). ~21k звёзд | https://github.com/VoltAgent/awesome-claude-code-subagents | high |
| 7 | **shadcn MCP** (уже стоит) | MCP | Фундамент: AI тянет реальный код из реестров, не галлюцинирует пропсы. CLI 3.0 мульти-registry | https://ui.shadcn.com/docs/mcp | high |
| 8 | **Chrome DevTools + Playwright MCP** (уже стоят) | MCP | Глаза агента для screenshot-critic loop. Без них любой «вкус» в промпте — слепая вера | — | high |
| – | **Owl-Listener designer-skills** (выборочно: design-systems / ui-design / visual-critique) | Plugin | Процессная строгость, 63 скилла — бери 3 | https://github.com/Owl-Listener/designer-skills | medium |
| – | **Julian Oczkowski designer-skills** (Design Review, Grill Me) | Skills | Full-cycle процесс, 7 скиллов, чище Owl-Listener | https://github.com/julianoczkowski/designer-skills | medium |
| – | **Официальный Figma MCP** (generate_figma_design + Code Connect) | MCP | ТОЛЬКО если платный Figma + нужен Code Connect/reverse-flow. Иначе Framelink | https://help.figma.com/hc/en-us/articles/39888612464151 | high |
| – | **21st.dev Magic MCP** (`/ui`) | MCP | High-craft компоненты в сессии. Нужен API-ключ, npm может не встать (ECONNRESET) | https://21st.dev/magic | high |

> **Безопасность (твой watchdog):** skill = исполняемые инструкции. Ставь только из проверенных репо (Vercel, Anthropic, известные авторы). Малозвёздные плагины не глядя не подключать — это внешний ввод в агент. Framelink Figma MCP имеет telemetry-утечку file keys в PostHog — проверь флаги отключения.

### Библиотеки-сырьё (дистрибутят исходник в твой репо → ты владеешь и перекрашиваешь)

| Что | Лицензия | Роль | Ссылка | Conf. |
|-----|----------|------|--------|-------|
| **Aceternity UI** (free + Pro) | free copy-paste | Главный источник wow-секций «designed by in-house team» | https://ui.aceternity.com/ | high |
| **Magic UI** (free) | MIT | Лучший animation-polish слой поверх shadcn, идеален для лендинга | https://magicui.design/ | high |
| **React Bits** (jsrepo) | MIT+Commons Clause | Крупнейший пул text-эффектов и анимированных фонов, 110+ комп. | https://github.com/DavidHDev/react-bits | high |
| **paper-design/shaders-react** | npm | Тёплые mesh-grain фоны вместо запрещённого purple→blue градиента | https://shaders.paper.design/ | high |
| **Cult UI** | MIT | Distinctive компоненты + AI-Agent паттерны (под CRM) | https://github.com/nolly-studio/cult-ui | high |
| **Tailark** (blocks) | MIT | Бесплатные marketing-блоки на Tailwind v4, под перекрас | https://tailark.com/ | high |
| **Kibo UI** | free OSS | Сложные app-компоненты: Gantt/Kanban/таблицы — под CRM-фазу | https://www.kibo-ui.com/ | high |
| **Origin UI / COSS** | MIT + AGPLv3 | Продвинутые примитивы (формы/инпуты/диалоги). ВНИМАНИЕ на AGPL-части | https://github.com/origin-space/originui | medium |
| **Tailwind Plus / Catalyst** | $149-299 one-time | Эталонный app/dashboard baseline для CRM | https://tailwindcss.com/plus/ui-kit | high |
| **Shadcnblocks** (skill стоит) | $79-149 one-time | 1338 premium + 1189 free блоков, AI-установка через MCP | https://www.shadcnblocks.com/ | high |
| **Motion v12** (`motion/react`) | MIT | Базовый motion-движок, на нём построены все киты | https://motion.dev/ | high |
| **GSAP free + Lenis** | free (с 2025) | SplitText/ScrollTrigger/MorphSVG для cinematic scroll | https://gsap.com/ | high |

### Design-to-code (Figma/референс → код)

| Что | Когда брать | Ссылка | Conf. |
|-----|-------------|--------|-------|
| **Framelink Figma MCP** | Самый частый сценарий «прочитать Figma → код под мои конвенции». Descriptive JSON, не диктует фреймворк. Бесплатно (обычный Figma API) | https://github.com/GLips/Figma-Context-MCP | high |
| **Официальный Figma Dev Mode MCP** | get_variable_defs = реальные токены + Code Connect 1:1. Только при зрелой системе + платном Dev seat (6 вызовов/мес free) | https://www.figma.com/blog/introducing-figma-mcp-server/ | high |
| **TypeUI DESIGN.md Extractor** (Chrome ext) | Вытащить DESIGN.md из любого референс-сайта за 1 клик, локально (MIT) | https://github.com/bergside/design-md-chrome | high |
| **Refero Styles / designmd.app** | 423+ готовых брендовых DESIGN.md для инжекта | https://styles.refero.design/ai-agents/design-md-examples | medium |
| **Builder.io Visual Copilot CLI** | Production Figma→code: сканит кодбазу, реюзит твои компоненты. Для серьёзных проектов | https://www.builder.io/blog/visual-copilot-cli | medium |
| **Style Dictionary v4 + Tokens Studio** | Только под зрелую дизайн-систему (CI/CD токенов). Для лендинга — оверкилл | https://docs.tokens.studio/transform-tokens/style-dictionary | high |

### QA / ревью

| Что | Роль | Ссылка | Conf. |
|-----|------|--------|-------|
| **Generator/evaluator split** (Anthropic) | Отдельный субагент-судья смотрит рендер по 4 критериям (design quality / originality / craft / functionality). Self-review НЕ работает | https://www.anthropic.com/engineering/harness-design-long-running-apps | high |
| **gstack design-review** | 80-пунктный аудит + AI Slop Score + автофиксы с before/after | https://github.com/garrytan/gstack | high |
| **Vercel web-design-guidelines** | 100+ правил: a11y, focus, формы, типографика, dark mode | https://github.com/vercel-labs/agent-skills | high |
| **Harmonizer** (OKLCH+APCA) | Перцептивно-консистентные палитры, экспорт в Tailwind @theme | https://harmonizer.evilmartians.com/ | high |
| **baseline-ui / audit** (стоят) | AI-slop линтер + технический аудит | — | high |
| **axe + Lighthouse-CI** | a11y + бюджеты LCP/CLS/INP перед merge | — | high |

---

## Методология (что реально убирает generic)

Подтверждено независимо ×6 направлений. **AI = усилитель вкуса, а не его источник. Нельзя запромптить то, что не можешь назвать.**

1. **Референсы ДО кода (главный рычаг).** 5-8 живых референсов (Awwwards/Mobbin 600k+/SiteInspire), под каждый — 1 фраза ПОЧЕМУ работает. Через Mobbin/Refero MCP агент тянет реальные экраны как картинку. Это сдвигает распределение от центроида. [confidence: high]

2. **Aesthetic lock — одно смелое направление вслух** (editorial/brutalist/luxury/retro-futuristic/industrial/organic) + добро ДО JSX. «Clean & modern» — это не направление, это безопасное среднее. [confidence: high]

3. **Числовые ограничения композиции** (эссе Verdigris «каждый минимум требует максимума — машина оптимизирует то, что ты НЕ ограничил»): доминирующий цвет ~70%, максимум 2 акцентные зоны, запрет «стробоскопа» (чередование dark/light секций), saturation contrast (большие зоны near-zero chroma против маленьких зон полной насыщенности). Переводит вкус в проверяемые правила. [confidence: high]

4. **DESIGN.md в КОРНЕ репо (самый дешёвый недооценённый фикс).** YAML-токены + Markdown-проза правил, ~1.5-3k токенов, грузится агентом первым. Корневая причина slop: LLM обрабатывает каждый промпт изолированно → каждый компонент = свежая регрессия к среднему. DESIGN.md = постоянный референс. Rationale-проза решает то, что JSON не может («primary только для главного действия»). Можно вытащить из эталонного сайта (TypeUI Extractor) или взять брендовый (Refero Styles), но **перекрашивать под свои oklch**, не клонировать чужой бренд 1:1. [confidence: high]

5. **Токены ДО компонентов** (W3C DTCG 2025.10: primitive→semantic→component). Цвет — OKLCH+APCA через Harmonizer: лочишь L для текста, крутишь C/H под контраст-таргет (chroma ~0.2 норма, 0.10-0.15 софт, 0.3+ vivid). Запрет hex/rgb/hsl через stylelint. Типографика — fluid clamp() scale (правило: max ≤ 2.5×min → всегда проходит WCAG 1.4.4) + вариативный характерный шрифт (Fraunces, не Inter). [confidence: high]

6. **Моушен по числам, последним.** Эмил Ковальски: durations <300ms (кнопка 100-160, dropdown 150-250, modal 200-500), кастомные cubic-bezier вместо встроенных weak ease, НИКОГДА ease-in на UI, entry только scale(0.95)+opacity (не scale(0)), анимировать только transform/opacity, stagger 30-80ms, частотность определяет наличие анимации (100+ раз/день → без). Всегда prefers-reduced-motion. GSAP free для scroll-сторителлинга, Motion для компонентов. [confidence: high]

7. **Screenshot-критик-луп через generator/evaluator SPLIT (критично).** Anthropic: агент при self-review уверенно хвалит мусор. Решение — ОТДЕЛЬНЫЙ evaluator-субагент открывает живую страницу через Playwright/Chrome DevTools MCP, скриншотит на 375/768/1024/1440px, оценивает по 4 калиброванным few-shot критериям, возвращает правки с измерениями. Проверяет ОПТИКУ (выравнивание иконок к тексту, баланс border-radius), а не только rule-compliance — Rauno Freiberg: оптика > жёсткая консистентность. **Первый вывод никогда не финал.** [confidence: high]

8. **QA-gate перед merge:** Vercel web-design-guidelines + react-best-practices + axe + Lighthouse-CI (бюджеты) + baseline-ui + gstack AI Slop Score.

---

## Что подключить в Claude Code прямо сейчас (пошагово)

> **ВАЖНО:** на этой машине npm/npx даёт ECONNRESET. Ставить через `git clone` в `~/.claude/skills/` либо через `/plugin marketplace add` (CC-slash, не bash). GitHub/git работает.

**1. Vercel agent-skills (QA/perf-gate — первым):**
```bash
git clone --depth 1 https://github.com/vercel-labs/agent-skills.git /tmp/vsk
cp -r /tmp/vsk/skills/web-design-guidelines /tmp/vsk/skills/react-best-practices \
      /tmp/vsk/skills/composition-patterns /tmp/vsk/skills/react-view-transitions \
      ~/.claude/skills/
```

**2. gstack design-review (screenshot-critic loop):**
```bash
git clone --depth 1 https://github.com/garrytan/gstack ~/.claude/skills/gstack
# Можно взять только design-review/SKILL.md + 80-пунктный чеклист и переложить на
# свой Chrome DevTools MCP (уже Connected), не таща весь 23-tool gstack (нужен bun≥1.3.10)
```

**3. VoltAgent дизайн-субагенты (изоляция контекста):**
```bash
git clone https://github.com/VoltAgent/awesome-claude-code-subagents /tmp/va
cp /tmp/va/categories/01-core-development/ui-designer.md \
   /tmp/va/categories/01-core-development/design-bridge.md ~/.claude/agents/
```

**4. UI-UX-Pro-Max (анти-slop база решений) — через marketplace:**
```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

**5. Mobbin MCP или Refero MCP (грундинг на референсы):**
```bash
# Mobbin — remote HTTP + OAuth (claude mcp add по endpoint, авторизация в браузере)
# Refero skill + craft-знания (работают без аккаунта):
git clone https://github.com/referodesign/refero_skill ~/.claude/skills/refero_skill
# Refero MCP: claude mcp add --transport http refero https://api.refero.design/mcp  (Bearer)
```

**6. Owl-Listener designer-skills (выборочно):**
```
/plugin marketplace add Owl-Listener/designer-skills
# бери design-systems / ui-design / visual-critique, не все 63
```

**7. Привычка (не команда):** класть `DESIGN.md` в корень КАЖДОГО UI-проекта (oklch-токены + правила), ссылаться из проектного CLAUDE.md чтобы грузился первым. TypeUI Extractor (Chrome ext) для вытаскивания токенов с референса.

**8. Опционально (после фикса npm / при платном Figma):** 21st.dev Magic MCP (`/ui`), официальный Figma MCP (`claude plugin install figma@claude-plugins-official`). НЕ запускать Framelink и официальный Figma MCP одновременно.

---

## Хайп vs реально работает (честная разбраковка)

**Реально работает (high confidence):**
- Reference-driven + aesthetic-lock ДО кода — прямая контрмера к доказанной регрессии к среднему.
- Generator/evaluator split для критик-лупа — self-review подтверждённо не работает (Anthropic).
- OKLCH+APCA+Harmonizer — детерминированный контраст без ручной подстройки.
- DESIGN.md в корне — дешёвый, нулевая инфра, бьёт «Tailwind-starter aesthetic».
- shadcn MCP + дистрибуция исходника — AI не галлюцинирует, ты владеешь кодом.
- GSAP free + числа Эмила — конкретные значения, которые AI сам не выдаёт.
- Vercel agent-skills — реальный perf/composition-gate от вендора фреймворка.

**Хайп / осторожно:**
- **Screenshot-to-code «pixel-perfect»** (v0/Bolt/Lovable/Codia) — НИКТО не pixel-perfect. Codia «95% accuracy» = маркетинг. Дают generic-версию + деградируют код за итерации. Только черновик каркаса. [high]
- **«Лучший тул решит всё»** — нет. Все регрессируют к среднему без процесса. [high]
- **Figma Make / First Draft код** — не production, не accessible, не semantic. На выброс, только как источник токенов/референса. [medium]
- **Framer AI как источник кода** — экспорт грязный/платный/сторонний. Только референс-генератор. [medium]
- **Замена subjective taste на VLM-критик** — VLM иногда галлюцинирует оценку. Нужен human-in-the-loop на финале; независимых бенчмарков мало (вендорские цифры). [medium]
- **Style Dictionary / Tokens Studio для лендинга** — оверкилл. Только под зрелую дизайн-систему/команду. [high]
- **Machine-readable design systems через MCP** (Spotify/Indeed) — enterprise-паттерн, для соло-вайбкодера сейчас избыточен; применим в миниатюре когда соберётся UI-кит CRM. [medium]
- **SuperDesign** — IDE-расширение (VS Code/Cursor), не нативный CLI skill/MCP. Для Claude Code маргинально. [medium]

---

## Источники

**Генераторы:** getmocha.com/blog/best-ai-app-builder-2026 · weavai.app (v0 vs Bolt vs Lovable 2026) · nxcode.io (vibe-design tools compared) · rogerwong.me/2025/04/beyond-the-prompt · annaarteeva.medium.com (AI prototyping stack) · subframe.com · magicpatterns.com · 21st.dev/magic · onlook.com · stitch.withgoogle.com · framer.com · v0.dev · lovable.dev

**Claude Code экосистема:** firecrawl.dev/blog/best-claude-code-skills · snyk.io/articles/top-claude-skills-ui-ux-engineers · composio.dev/content/top-design-skills · github.com/vercel-labs/agent-skills · github.com/nextlevelbuilder/ui-ux-pro-max-skill · github.com/VoltAgent/awesome-claude-code-subagents · github.com/julianoczkowski/designer-skills · github.com/Owl-Listener/designer-skills · github.com/garrytan/gstack · anthropic.com/news/claude-design-anthropic-labs · github.com/rohitg00/awesome-claude-design · github.com/superdesigndev/superdesign · github.com/21st-dev/magic-mcp · ui.shadcn.com/docs/mcp · help.figma.com (Claude Code + Figma MCP)

**Методология вкуса:** arxiv.org/pdf/2503.01033 (variance reduction) · news.mit.edu/2023/generative-ai-must-innovate-engineering-design-1019 · vds-taste-essay.vercel.app (Verdigris) · anthropic.com/engineering/harness-design-long-running-apps · github.com/emilkowalski/skill · ui.land/interviews/rauno-freiberg · rauno.me/craft/interaction-design · evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl · harmonizer.evilmartians.com · giangallegos.com (design with AI 2026) · github.com/anthropics/skills (frontend-design) · fluid-type-scale.com · designtokens.org/tr/drafts/format · gsap.com/resources/getting-started/Easing · tweag.github.io/agentic-coding-handbook · medium.com/built-to-adapt (8pt grid) · brianlovin.com/app-dissection

**UI-ресурсы:** ui.shadcn.com/docs/mcp + changelog cli-3-mcp · registry.directory · shadcn.io/awesome/registries · ui.aceternity.com · magicui.design · github.com/DavidHDev/react-bits · github.com/nolly-studio/cult-ui · github.com/origin-space/originui · tailark.com · kibo-ui.com · eldoraui.site · skiper-ui.com · motion-primitives.com · gsap.com · motion.dev · shaders.paper.design · tailwindcss.com/plus · shadcnblocks.com · hover.dev · animata.design

**Design-to-code:** chatforest.com/reviews/mobbin-mcp-server · businesswire.com (Mobbin MCP launch) · github.com/referodesign/refero_skill · refero.design/mcp · styles.refero.design · pasqualepillitteri.it (DESIGN.md library) · github.com/bergside/design-md-chrome · github.com/GLips/Figma-Context-MCP · figma.com/blog/introducing-figma-mcp-server · builder.io/blog/visual-copilot-cli · aimultiple.com/screenshot-to-code · evilmartians.com/opensource/harmonizer · docs.tokens.studio

**Frontier:** github.com/garrytan/gstack/blob/main/design-review/SKILL.md · techcrunch.com (Garry Tan Claude Code setup) · github.com/leonxlnx/taste-skill · developersdigest.tech (taste-skills review) · github.com/VoltAgent/awesome-design-md · intodesignsystems.com (Spotify AI-ready) · alexop.dev (AI QA engineer Claude+Playwright) · bug0.com (Playwright MCP 2026)

---

## Предложение: новая дизайн-секция для CLAUDE.md

> Лаконичная замена удалённой анти-slop системы. Принципы + мини-процесс + ссылки, без душащих глобальных банов. Вставить в глобальный конфиг.

### Дизайн — принципы 2026

**Почему AI-дизайн выходит generic:** модель регрессирует к среднему датасета (Inter, purple→blue градиент, centered-hero+3-cards). Это математика objective-функции, не плохой промпт. Лечится **ограничениями + референсами + внешним визуальным аудитом**, а не «лучшими словами». AI = усилитель вкуса, не источник. Нельзя запромптить то, что не можешь назвать.

**Обязательный мини-процесс (порядок строгий):**
1. **Референсы:** 3-5 живых сайтов (Awwwards/Mobbin/SiteInspire или через Mobbin/Refero MCP), под каждый — фраза ПОЧЕМУ работает.
2. **Направление вслух:** одно смелое (editorial/brutalist/luxury/retro-futuristic/industrial/organic) + добро юзера ДО кода. «Clean & modern» — не направление.
3. **DESIGN.md в корень репо:** oklch-токены (1 brand + 1 accent + 3-5 нейтралей, OKLCH+APCA через Harmonizer) + fluid clamp() type scale + характерный variable-шрифт (не Inter) + правила-проза. Грузится первым в каждом промпте. Можно вытащить с референса (TypeUI Extractor) и перекрасить под себя.
4. **Build:** shadcn MCP + Aceternity/Magic UI/React Bits/Cult как сырьё → перекрасить под токены, kit-default не отдавать. Modern CSS (Grid/subgrid, container queries, logical props, clamp()).
5. **Моушен последним:** Motion v12 для компонентов, GSAP free для scroll. Числа Эмила (durations <300ms, кастомные cubic-bezier, только transform/opacity). Всегда prefers-reduced-motion.
6. **Критик-луп (не self-review!):** отдельным проходом снять рендер через Chrome DevTools / Playwright MCP → оценить spacing/иерархию/APCA-контраст/оптику по критериям → чинить по пикселям. Первый вывод не финал.

**Композиционные числа (а не вкус):** доминирующий цвет ~70%, максимум 2 акцентные зоны, нет «стробоскопа» dark/light секций, контраст размеров H1↔body как главный рычаг иерархии, оптическое выравнивание > геометрическое.

**Стек:** OKLCH+APCA (Harmonizer) · Tailwind v4 @theme · clamp() type scale · Motion v12 + GSAP free + Lenis · paper-design/shaders (фоны вместо градиентов) · shadcn MCP + Aceternity/Magic UI/React Bits/Cult/Kibo · Chrome DevTools + Playwright MCP. Skills: impeccable / frontend-design / taste-skill / emil-design-eng / Vercel web-design-guidelines / baseline-ui.

**Мягкие ориентиры (не жёсткие баны):** избегать Inter/Roboto/Geist по умолчанию, purple→blue→white градиента, glass-everywhere, equal-padding grid, emoji-вместо-иконок, hardcoded hex/px в компонентах. Если направление осознанно требует — можно, но назови это вслух.
