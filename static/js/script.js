$(document).ready(function(){
  $('.menu-icon').click(function(){
    $(this).toggleClass('arrow-up');
    $('.menu-content').toggleClass('open');
  });
});

//JQuery file, macht das menu aufklappen möglich, indem es dem menu inhalt eine CSS-Klasse gibt und wieder nimmt.
//Das Menu ist je nach aktueller klasse dann sichtbar oder nicht.
