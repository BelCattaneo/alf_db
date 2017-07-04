function resizeImage($img, parentWidth, parentHeight) {
  if($img.width() > $img.height()) {
    $img.height(parentHeight); 
  } else {
    $img.width(parentWidth);
  }
}

function centerImage($img, parentWidth, parentHeight) {
  var left = ($img.width() - parentWidth) / 2;
  var top = ($img.height() - parentHeight) / 2;

  $img.css({ left: -left, top: -top });
}


$(function() {

   $(".thumbnail-image").each(function(index, img) {
     var $img = $(img);
     var $parentContainer = $img.closest(".image-container");
     
     var parentWidth = $parentContainer.width();
     var parentHeight = $parentContainer.height();

     $img.one("load", function() {
      resizeImage($img, parentWidth, parentHeight);
      centerImage($img, parentWidth, parentHeight);
     });
     
   });

});