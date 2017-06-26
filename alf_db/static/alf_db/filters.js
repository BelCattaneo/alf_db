function clearFilters() {
  $("#filter_form input").val(null);
}

$(document).ready(function() {
  $("#clear").click(clearFilters)
});