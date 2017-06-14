function elem(tagName, attributes){
  attributes = attributes || {};
  var tag = $("<" + tagName +"></" + tagName + ">");
  Object.keys(attributes).forEach(function(attributeName){
    tag.attr(attributeName, attributes[attributeName]);
  });
  return tag;
}


function createSelect(items, attributes){
  var select = elem("select", attributes);
  items.forEach(function(item) {
    select.append(elem("option").attr("value", item).text(item));
    
  });
  return select;  
}

function createInput(filter_name, filter_type){
  
  var filter = null;
  if(filter_type === "exact"){
    filter = filter_name;
  }else{
    filter = filter_name + '__' + filter_type; 
  } 
  
  var attributes = {
    name: filter,
    id: filter
  }
  var input = elem("input", attributes);
  return input;
}


function onLoad() {
  var filterNames = Object.keys(alfDb.filters);
  filterNames.unshift("Filtros");
  var selectName = createSelect(filterNames, {id:"filter_name"});
  $("#container_filter_name").html(selectName);

  $("#filter_name").change(function(){
    var selectedName = $("#filter_name").val();
    var filterTypes = alfDb.filters[selectedName];
    filterTypes.unshift("Tipo de Filtro");
    var selectType = createSelect(filterTypes, {id:"filter_type"});
    $("#container_filter_type").html(selectType);
  });

  $("#container_filter_type").on("change", "#filter_type", function(){
    var input = createInput($("#filter_name").val(), $("#filter_type").val());
    $("#filter_form").append(input);
  });
  
}



$(onLoad)
