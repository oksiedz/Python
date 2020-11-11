$(function() {
  function deselect(e) {
    $('.pop').slideFadeToggle(function() {
      e.removeClass('selected');
    });
  }

  $.fn.slideFadeToggle = function(easing, callback) {
    return this.animate({ opacity: 'toggle', height: 'toggle' }, 'fast', easing, callback);
  };

  $('.brochure-download').on('click', function(o) {
    console.log("Clicked");
    if($(this).hasClass('selected')) {
      deselect($(this));
    } else {
      $(this).addClass('selected');
      $('.pop').slideFadeToggle();
    }
    return false;
  });

  $('#messagepop_close').on('click', function() {
    deselect($('.brochure-download'));
    return false;
  });
});
