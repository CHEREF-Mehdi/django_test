$("#updateInfoForm").submit(function (e) {
  e.preventDefault();

  $.ajax({
    url: URL,
    type: "post", // or "get"
    data: $("#updateInfoForm").serialize(),
    headers: { "X-CSRFToken": CSRF_TOKEN }, // for csrf token
    success: function (data) {
      if (data.type === "success") {
        $("#card_username").text(data.user.username);
        $("#p_email").text(data.user.email);
        $(".p_first_name").text(data.user.first_name);
        $("#UserModal").modal("hide");
        slideMessage("alertDiv", data.type, data.message);
      } else {
        if (data.type === "danger") {
          const error = Object.keys(data.error);
          $("#id_" + error[0]).addClass("is-invalid");
          const errorMsg = data.error[error[0]][0].message;
          slideMessage("alertUpdateForm", data.type, errorMsg, true);
        }
      }
    },
    error: function (error) {
      slideMessage("alertUpdateForm", "danger", error.message);
    },
  });
  return false;
});

$(document).ready(function () {
  $("#UserModal").on("hidden.bs.modal", function () {
    $("#alertUpdateForm").html("");
    $("#id_username").val(userName);
    $("#id_first_name").val(firstName);
    $("#id_email").val(userEmail);
    $("#id_email,#id_username").removeClass("is-invalid");
  });
});
