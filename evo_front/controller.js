$(document).ready(function () {
    
    //Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message){
        $(".evo-message li:first").text(message);
        $('.evo-message').textillate('start');
    }

    //Display Hood
    eel.expose(ShowHood)
    function ShowHood(){
        $("#Oval").attr("hidden", false);
        $("#EvoWave").attr("hidden", true);
    }
});