function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });
  });

window.onload = function() {
    $('#up').click(function() {
        var pk = $(this).attr('name')
        let upValue = 1
        $.ajax({
            url : pk,
            type : 'POST',
            data: { 'pk': pk ,'value' : upValue,},
            success:function(response){
                console.log(response.count, '성공')
                $('#countValue').html(response.count)
            },
            error:function(){
                alert('실패');
            }
        });
    });
    $('#down').click( function() {
        var pk = $(this).attr('name')
        let upValue = -1
        $.ajax({
            url : pk,
            type : 'POST',
            data: { 'pk': pk ,'value' : upValue,},
            success:function(response){
                console.log(response.count, '성공')
                $('#countValue').html(response.count)
            },
            error:function(){
                alert('실패');
            }
        });
    });
}