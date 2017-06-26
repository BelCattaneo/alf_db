$("#clear").on('click', function({
  $('.form-group').val(null).trigger("change");
}))