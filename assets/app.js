// экспресс-проверка — заглушка (бэкенд позже, легальный путь через специалиста)
  (function(){
    ['checkForm','auditForm'].forEach(function(id){
      var f = document.getElementById(id);
      if(!f) return;
      f.addEventListener('submit', function(e){
        e.preventDefault();
        var inp = f.querySelector('input');
        var v = inp ? inp.value.trim() : '';
        alert(v ? 'Заявка по объекту «'+v+'» принята. Наш специалист свяжется с вами для уточнения и официального запроса.' : 'Введите кадастровый номер, адрес объекта или ваш вопрос.');
      });
    });
  })();
  // плавное появление секций (фолбэк: нет IO / reduced-motion → показать всё)
  (function(){
    var els = document.querySelectorAll('.reveal');
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)){
      els.forEach(function(el){ el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target);} });
    },{threshold:0.1, rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){ io.observe(el); });
  })();
  // анимация счётчиков в hero (фолбэк: нет IO/RAF/reduced-motion → сразу финальное число)
  (function(){
    var stats = document.querySelector('.hero-stats');
    if(!stats) return;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function run(){
      stats.querySelectorAll('.cnt').forEach(function(el){
        var to = parseInt(el.getAttribute('data-to'),10) || 0;
        if(reduce || !('requestAnimationFrame' in window)){ el.textContent = to; return; }
        var dur = 1100, t0 = null;
        function step(ts){
          if(!t0) t0 = ts;
          var p = Math.min((ts - t0)/dur, 1), e = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(to * e);
          if(p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }
    if(!('IntersectionObserver' in window)){ run(); return; }
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){ if(en.isIntersecting){ run(); io.disconnect(); } });
    },{threshold:0.4});
    io.observe(stats);
  })();
  // переключатель светлой/тёмной темы (инициализация — в <head>, без мигания)
  (function(){
    var root = document.documentElement, btn = document.getElementById('themeToggle');
    if(!btn) return;
    btn.addEventListener('click', function(){
      var dark = !root.classList.contains('dark');
      root.classList.toggle('dark', dark);
      try{ localStorage.setItem('oo-theme', dark ? 'dark' : 'light'); }catch(e){}
    });
  })();
