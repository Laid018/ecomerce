$(document).ready(function () {
  console.log("jquery is working!");
  $(".menu-btn").click(function () {
    console.log("clicked");
    $(".sub-menu").toggleClass("active");
  });

  $(".btn-burguer").click(function () {
    console.log("clicked");
    $(".sidebar").toggleClass("active");
  });
});
