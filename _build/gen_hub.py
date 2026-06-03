#!/usr/bin/env python3
# Генератор uslugi.html (хаб услуг) из _build/hub.json + ручные лиды.
# Запуск из корня репо: python3 _build/gen_hub.py
import json, html, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hub=json.load(open(os.path.join(ROOT,'_build/hub.json')))

WLEAD={
 'oformit':'У вас неоформленный, проблемный или реконструированный объект. Берём на себя всю административную, кадастровую и судебную нагрузку — отдаём готовую выписку из ЕГРН без очередей и вашего личного участия.',
 'zashchitit':'Защищаем ваши активы в правовом поле: суды по земле, границам и самострою, оспаривание отказов Росреестра, проверка чистоты и безопасное сопровождение сделок.',
}
SUBHUBS={
 'oformit':[
   ('Оформление «под ключ»','Сквозное юридическое оформление, легализация и регистрация прав на любые объекты — от первичных обмеров на местности до записи в ЕГРН.',
     ['Оформление прав «под ключ»','Градостроительная документация']),
   ('Инженерно-кадастровые работы','Точные данные — фундамент любых операций с недвижимостью: межевые и технические планы, топосъёмка, вынос границ и обмеры собственным GNSS-оборудованием.',
     ['Кадастровые работы и техдокументация','Геодезические изыскания и обмеры']),
 ],
 'zashchitit':[
   ('Судебные споры и защита прав','Представительство в судах Крыма по земельным и имущественным спорам, легализация через суд, экспертизы, установление сервитутов и снижение кадастровой стоимости.',
     ['Судебные споры и защита прав']),
   ('Безопасные сделки и Due Diligence','Проверка юридической чистоты объекта перед покупкой (Due Diligence) и полное сопровождение сделок купли-продажи, аренды, ипотеки и инвестпроектов.',
     ['Безопасные сделки и Due Diligence']),
 ],
}
groups_by_label={g['group']:g['items'] for w in hub for g in hub[w]}
def esc(s): return html.escape(s, quote=True)
def cards(items):
    o=['  <div class="usl-grid">']
    for it in items:
        o.append(f'    <a class="usl-card reveal" href="uslugi/{it["slug"]}.html">\n      <h3>{esc(it["title"])}</h3>\n      <p>{esc(it["short"])}</p>\n      <span class="usl-go">Подробнее →</span>\n    </a>')
    o.append('  </div>'); return '\n'.join(o)
BADGE={'oformit':('blue','<path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>'),
       'zashchitit':('teal','<path d="M12 3 4 6v6c0 5 3.5 7.5 8 9 4.5-1.5 8-4 8-9V6Z"/><path d="m9 12 2 2 4-4"/>')}
WLABEL={'oformit':('Оформить','Инженерно-кадастровое производство: ведём объект от поля до ЕГРН.'),
        'zashchitit':('Защитить','Правовая защита активов: суды, споры и безопасные сделки.')}
def wing(w):
    color,svg=BADGE[w]; name,sub=WLABEL[w]
    h=[f'<div class="usl-wing reveal">\n  <div class="usl-wing-head">\n    <span class="usl-wing-badge {color}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{svg}</svg></span>\n    <div><h2>{name}</h2><p>{sub}</p></div>\n  </div>\n  <p class="subhub-lead" style="max-width:80ch">{esc(WLEAD[w])}</p>']
    for st,sl,gls in SUBHUBS[w]:
        h.append(f'  <div class="subhub">\n    <h3 class="subhub-title">{esc(st)}</h3>\n    <p class="subhub-lead">{esc(sl)}</p>')
        for gl in gls:
            items=groups_by_label.get(gl,[])
            if not items: continue
            if len(gls)>1: h.append(f'    <p class="usl-sub">{esc(gl)}</p>')
            h.append(cards(items))
        h.append('  </div>')
    h.append('</div>'); return '\n'.join(h)

body=f'''<section class="subhero"><div class="wrap subhero-in reveal">
  <nav class="crumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a><span class="sep">/</span><span class="here">Услуги</span></nav>
  <h1>Все услуги по недвижимости</h1>
  <p class="lead">Полный спектр работ с недвижимостью в Ялте и по всему Крыму — от записи в ЕГРН до защиты прав в суде. Два направления: <b>Оформить</b> и <b>Защитить</b>.</p>
</div></section>
<section class="block wrap">
{wing('oformit')}
{wing('zashchitit')}
</section>
<section class="cta wrap"><div class="cta-card reveal">
  <h2>Не нашли свою задачу?</h2>
  <p>Решение нестандартных кейсов на Южном берегу Крыма — наша специализация. Опишите ситуацию, подберём маршрут оформления или защиты.</p>
  <a class="btn-primary" href="kontakty.html">Получить консультацию →</a>
</div></section>'''
shell=open(os.path.join(ROOT,'_build/shell.html')).read()
pkg=json.load(open(os.path.join(ROOT,'_build/pages/uslugi.json')))
page=shell.replace('{{P}}','').replace('{{TITLE}}',esc(pkg['meta_title'])).replace('{{DESC}}',esc(pkg['meta_desc'])).replace('<!--BODY-->',body)
open(os.path.join(ROOT,'uslugi.html'),'w').write(page)
# проставить cache-bust версию
import re
s=open(os.path.join(ROOT,'uslugi.html')).read()
s=re.sub(r'(assets/(?:style\.css|app\.js))(\?v=\d+)?"', r'\1?v=1"', s)
open(os.path.join(ROOT,'uslugi.html'),'w').write(s)
print('uslugi.html сгенерирован:', page.count(chr(10)),'строк, карточек:', body.count('usl-card'))
