(function($) {
    $(function() {

        $('.button-collapse').sideNav();
        $('.parallax').parallax();

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

var dialogStartDate = new mdDateTimePicker.default({
    type: 'date'
});
var toggleButtonStartDate = document.getElementById('event-start-date');
toggleButtonStartDate.addEventListener('focus', function() {
    dialogStartDate.toggle();
});
dialogStartDate.trigger = document.getElementById('event-start-date');
document.getElementById('event-start-date').addEventListener('onOk', function() {
    this.value = dialogStartDate.time.format('L').toString();
    Materialize.updateTextFields();
});

var dialogStartTime = new mdDateTimePicker.default({
    type: 'time'
});
var toggleStartTime = document.getElementById('event-start-time');
toggleStartTime.addEventListener('focus', function() {
    dialogStartTime.toggle();
});
dialogStartTime.trigger = document.getElementById('event-start-time');
document.getElementById('event-start-time').addEventListener('onOk', function() {
    this.value = dialogStartTime.time.format('LT').toString();
    Materialize.updateTextFields();
});

var dialogEndDate = new mdDateTimePicker.default({
    type: 'date'
});
var toggleButtonEndDate = document.getElementById('event-end-date');
toggleButtonEndDate.addEventListener('focus', function() {
    dialogEndDate.toggle();
});
dialogEndDate.trigger = document.getElementById('event-end-date');
document.getElementById('event-end-date').addEventListener('onOk', function() {
    this.value = dialogEndDate.time.format('L').toString();
    Materialize.updateTextFields();
});

var dialogEndTime = new mdDateTimePicker.default({
    type: 'time'
});
var toggleEndTime = document.getElementById('event-end-time');
toggleEndTime.addEventListener('focus', function() {
    dialogEndTime.toggle();
});
dialogEndTime.trigger = document.getElementById('event-end-time');
document.getElementById('event-end-time').addEventListener('onOk', function() {
    this.value = dialogEndTime.time.format('LT').toString();
    Materialize.updateTextFields();
});

var dialogDeadlineDate = new mdDateTimePicker.default({
    type: 'date'
});
var toggleButtonDeadlineDate = document.getElementById('task-end-date');
toggleButtonDeadlineDate.addEventListener('focus', function() {
    dialogDeadlineDate.toggle();
});
dialogDeadlineDate.trigger = document.getElementById('task-end-date');
document.getElementById('task-end-date').addEventListener('onOk', function() {
    this.value = dialogDeadlineDate.time.format('L').toString();
    Materialize.updateTextFields();
});

var dialogDeadlineTime = new mdDateTimePicker.default({
    type: 'time'
});
var toggleDeadlineTime = document.getElementById('task-end-time');
toggleDeadlineTime.addEventListener('focus', function() {
    dialogDeadlineTime.toggle();
});
dialogDeadlineTime.trigger = document.getElementById('task-end-time');
document.getElementById('task-end-time').addEventListener('onOk', function() {
    this.value = dialogDeadlineTime.time.format('LT').toString();
    Materialize.updateTextFields();
});
