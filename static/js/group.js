var dialogStartDate = new mdDateTimePicker.default({
    type: 'date',
    past: moment().subtract(0, 'years'),
    future: moment().add(21, 'years')
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
    type: 'date',
    past: moment().subtract(0, 'years'),
    future: moment().add(21, 'years')
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
    type: 'date',
    past: moment().subtract(0, 'years'),
    future: moment().add(21, 'years')
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

var UploadGroupPic = (function() {
    function groupPicUpload() {
        var $uploadCrop;

        function readFile(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function(e) {
                    $('.upload-group-pic').addClass('ready');
                    $('.upload-result').addClass('ready');
                    console.log('ready');
                    $uploadCrop.croppie('bind', {
                        url: e.target.result
                    }).then(function() {
                        console.log('jQuery bind complete');
                    });

                }

                reader.readAsDataURL(input.files[0]);
            } else {
                swal("Sorry - you're browser doesn't support the FileReader API");
            }
        }

        $uploadCrop = $('#upload-group-pic').croppie({
            viewport: {
                width: 300,
                height: 220,
            },
        });

        $('#upload').on('change', function() {
            readFile(this);
        });
        $('.upload-result').on('click', function(ev) {
            $uploadCrop.croppie('result', {
                type: 'canvas',
                size: 'viewport'
            }).then(function(resp) {
                $('.group-pic').attr('src', resp);
                $('#new-group-image').attr('value', resp);
                $.post('',{ "image":resp , "update_group_pic": "true" });
            });
            
        });
    }

    function init() {
        groupPicUpload();
    }

    return {
        init: init
    };
})();
UploadGroupPic.init();

function initMap() {
    var input = document.getElementById('location');
    var autocomplete = new google.maps.places.Autocomplete(input);
}