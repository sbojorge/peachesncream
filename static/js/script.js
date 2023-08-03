// sidebar initialization
document.addEventListener("DOMContentLoaded", function () {
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
});

// select initialization
document.addEventListener("DOMContentLoaded", function () {
  let elems = document.querySelectorAll("select");
  M.FormSelect.init(elems, options);
});
