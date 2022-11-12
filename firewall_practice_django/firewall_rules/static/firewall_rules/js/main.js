//boolean night_mode default to false
var night_mode = false;

function change_night_mode(){
    if (night_mode){
        //if night mode set to on, change the background color to white
        $("body").attr("style","background-color:white");
        $("#change_night_mode").text("Night");
        night_mode=false;
    }else{
        //if night mode set to off, change the background color to black
        $("body").attr("style","background-color:black");
        $("#change_night_mode").text("Day");
        night_mode=true;
    }
}