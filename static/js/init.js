(function($) {
    $(function() {

        $('.button-collapse').sideNav();
        $('.parallax').parallax();

        $('body').css("height", $(document).height());
        $('main').css("height", $(document).height());
        $('main>.row').css("height", $(document).height());
        $('.right-side').css("height", $(document).height());

    }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function() {
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
    $('select').material_select();
});

$(document).ready(function() {
    $('.catagory-list').pushpin({
        top: $('nav').height(),
        offset: 0
    });
});


$('.catagory-list').each(function() {
    var $this = $(this);
    var $target = $('#' + $(this).attr('data-target'));
    $this.pushpin({
        top: $target.offset().top,
        bottom: $target.offset().top + $target.outerHeight() - $this.height()
    });
});
