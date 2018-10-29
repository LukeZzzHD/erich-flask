$(document).ready(function(){
  $('.menu-icon').click(function(){
    $(this).toggleClass('arrow-up');
    $('.menu-content').toggleClass('open');
  });
});
