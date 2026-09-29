// Idioma persistente entre páginas (misma mecánica que ingrid.ar)
(function () {
  var KEY = "ingridastiz-lang";
  var TITLES = {
    es: "Ingrid Astiz · Consejera independiente",
    en: "Ingrid Astiz · Independent Board Member"
  };
  function apply(lang) {
    document.body.classList.toggle("lang-en", lang === "en");
    document.documentElement.lang = lang;
    if (document.body.dataset.page === "home") document.title = TITLES[lang];
    document.querySelectorAll(".lang-toggle button").forEach(function (b) {
      b.classList.toggle("on", b.dataset.lang === lang);
    });
  }
  function get() {
    try { return localStorage.getItem(KEY) || "es"; } catch (e) { return "es"; }
  }
  function set(lang) {
    try { localStorage.setItem(KEY, lang); } catch (e) {}
    apply(lang);
  }
  document.addEventListener("DOMContentLoaded", function () {
    apply(get());
    document.querySelectorAll(".lang-toggle button").forEach(function (b) {
      b.addEventListener("click", function () { set(b.dataset.lang); });
    });
  });
  // aplicar cuanto antes para evitar parpadeo
  if (document.body) apply(get());
})();
