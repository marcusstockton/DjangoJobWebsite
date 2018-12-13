$(document).ready(function () {
    console.log("ready!");

    $("#createDemoUserBtn").click(function () {
        $.ajax({
            url: 'https://randomuser.me/api/',
            dataType: 'json',
            success: function (data) {
                var data = data.results[0];
                $('#id_username').val(data.login.username);
                $('#id_birth_date').val(data.dob.date.split('T')[0])
                $('#id_first_name').val(data.name.first)
                $('#id_last_name').val(data.name.last)
                $('#id_email').val(data.email)
            },
        });
        
    });

});