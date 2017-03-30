/**
 * Created by ccatman on 12/3/2016.
 */
function check_create() {
    if(check_title()&&check_area()&&check_content())
        return true;
    alert("You need to give us title,area,category and content. : )");
    return false;
}
function check_title() {

    if($('#title').val().trim()!=null){

         return true;
	}
	return false;
}
function check_area() {
    var area = $('#area').val();
    if(area != -1){
        console.log("area true")
         return true;
	}
	return false;
}

function check_content() {
   var content = $('#noise').val();
   if(content.trim()!=null){
       console.log("content true")
       return true;
   }
   return false;
}