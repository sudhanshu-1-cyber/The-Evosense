$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn"
        },
        out:{
            effect: "bounceOut"
        }
    });
    //Evo Wave configuration
    var siriWave = new SiriWave({
        container: document.getElementById("evo-wave"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed : "0.2",
        autostart: true
    });
    //Evo message animation
    $('.evo-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync: true,
        },
        out:{
            effect: "fadeOutUp",
            sync: true,
        }
    });
    //Mic button click event
    $("#MicBtn").click(function () { 
        eel.playEvoSound()
        $("#Oval").attr("hidden", true);
        $("#EvoWave").attr("hidden", false);
        eel.allCommands()
    });
    
});