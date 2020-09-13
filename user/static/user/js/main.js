$("#updateInfoForm").submit( function (e) {
  e.preventDefault();
  var formJson = $('#updateInfoForm').serializeJSON();
  
 
  $.ajax({
    url: URL,
    type: "post", // or "get"
    data: formJson,
    headers: { "X-CSRFToken": CSRF_TOKEN }, // for csrf token
    success: function (data) {
      $("#h2_username").text(data.user.username)
      $("#p_email").text(data.user.email)
    },
    error:function (data) {
        console.log('erreur');
        console.error(data);
    },
  });
  return false;
});

