$(function() {

  $("#save-image-button").click(function() {
    $('<input/>')
        .attr('type', 'hidden')
        .attr('name', "stay")
        .attr('value', true)
        .appendTo('.centered-form');

    return true;
  });

})