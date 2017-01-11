$(document).ready(function() {
    $('#card-introduction > div.card-content > .activator').on({
        'click': function() {
            $('.edit-interests').siblings('input.select-dropdown').on({
                'focus': function() {
                    $('#card-introduction').addClass('card-overflow');
                },

            });
        },
    });
    $('#card-introduction > div.card-reveal > h5').on({
        'click': function() {
            $('#card-introduction').removeClass('card-overflow');
        },
    });
});
var UploadProfilePic = (function() {
    function profilePicUpload() {
        var $uploadCrop;

        function readFile(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function(e) {
                    $('.upload-profile-pic').addClass('ready');
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

        $uploadCrop = $('#upload-profile-pic').croppie({
            viewport: {
                width: 250,
                height: 250,
                type: 'circle'
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
                $('.profile-pic').attr('src', resp);
            });
        });
    }

    function init() {
        profilePicUpload();
    }

    return {
        init: init
    };
})();
UploadProfilePic.init();

var dialogBirthday = new mdDateTimePicker.default({
    type: 'date',
    past: moment().subtract(100, 'years'),
});
var toggleButtonBirthday = document.getElementById('birthday');
toggleButtonBirthday.addEventListener('focus', function() {
    dialogBirthday.toggle();
});
dialogBirthday.trigger = document.getElementById('birthday');
document.getElementById('birthday').addEventListener('onOk', function() {
    this.value = dialogBirthday.time.format('L').toString();
    Materialize.updateTextFields();
});
