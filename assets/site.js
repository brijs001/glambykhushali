// Mobile menu
(function () {
  var btn = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  if (!btn || !menu) return;
  btn.addEventListener("click", function () {
    var open = menu.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
  menu.addEventListener("click", function (e) {
    if (e.target.tagName === "A") {
      menu.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    }
  });
})();

// Contact form (posts to the existing site-builder contact endpoint)
(function () {
  var form = document.getElementById("contact-form-el");
  if (!form) return;
  var fields = document.getElementById("contact-fields");
  var submit = document.getElementById("contact-submit");
  var ok = document.getElementById("contact-success");
  var fail = document.getElementById("contact-failure");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    submit.disabled = true;
    fail.classList.add("hidden");
    var data = new FormData(form);
    fetch(form.dataset.endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "omit",
      body: JSON.stringify({
        name: String(data.get("name") || ""),
        email: String(data.get("email") || ""),
        message: String(data.get("message") || "")
      })
    })
      .then(function (r) { return r.ok; })
      .catch(function () { return false; })
      .then(function (sent) {
        if (sent) {
          fields.classList.add("hidden");
          ok.classList.remove("hidden");
        } else {
          fail.classList.remove("hidden");
          submit.disabled = false;
        }
      });
  });
})();
