function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




$("#modal__sign__in").submit(function(e) {
    e.preventDefault();
    $('#modal__page').html('<div class="loading__modal__page"><div class="loader"></div></div>')
    let data = {};
    data.csrfmiddlewaretoken = getCookie('csrftoken');
    data.email = $('#modal__sign__in [name="email"]').val();
    data.password = $('#modal__sign__in [name="password"]').val();
    $.ajax({
        type: "POST",
        url: $(this).attr('action'),
        data: data,
        success: function(data) {
            if (data.errors) {
                $('.modal-errors').html('<p class="m-0" style="color: red">'+ data.errors.__all__ +'</p>')
            } else {
                $('.modal-errors').remove()
            }
            $('.loading__modal__page').remove()
            if (data.success) {
                window.location.href = document.location.href
            }
        }
    });
});

$("#sign__in").submit(function(e) {
    e.preventDefault();
    $('#loading__auth__page').html('<div class="loading__auth"><div class="loader"></div></div>')
    let data = {};
    data.csrfmiddlewaretoken = $('#sign__in [name="csrfmiddlewaretoken"]').val();
    data.email = $('#sign__in [name="email"]').val();
    data.password = $('#sign__in [name="password"]').val();
    $.ajax({
        type: "POST",
        url: $(this).attr('action'),
        data: data,
        success: function(data) {
            if (data.errors) {
                $('.form-auth-errors').html('<p class="m-0" style="color: red">'+ data.errors.__all__ +'</p>')
            } else {
                $('.form-auth-errors').remove()
            }
            $('.loading__auth').remove()
            if (data.success) {
                window.location.href = document.location.href
            }
        }
    });
});