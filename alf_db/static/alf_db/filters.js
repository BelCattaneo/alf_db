function clearFilters() {
  $("#filter_form input").val(null);
  $('#id_customer').val(null)
  $('#select2-id_customer-container.select2-selection__rendered').html("");

}

$(document).ready(function() {
  $("#clear").click(clearFilters)
});