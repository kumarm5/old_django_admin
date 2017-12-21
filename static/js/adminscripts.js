$(document).ready(function(){
    
    winheight = $(window).height();
    $('body').slimScroll({
        height: winheight,
        allowPageScroll: true, 
        alwaysVisible: true
    });

});
