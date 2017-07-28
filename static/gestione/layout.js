
$(document).ready(function(){
    $('.dropdown').mouseenter(function(){
        if(!$('.navbar-toggle').is(':visible')) { // disable for mobile view
            if(!$(this).hasClass('open')) { // Keeps it open when hover it again
                $('.dropdown-toggle', this).trigger('click');
            }
        }
    });
});