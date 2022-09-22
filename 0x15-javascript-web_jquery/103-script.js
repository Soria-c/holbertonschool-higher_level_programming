window.onload = () => {
  function action() {
    console.log(event);
    const value = $("#language_code").val();
    $.ajax({
      type: "GET",
      url: `https://stefanbohacek.com/hellosalut/?lang=${value}`,
      success: function (data) {
        $("#hello").text(data.hello);
      },
      error: function () {
        alert("Error getting response");
      },
    });
  }

  $("#btn_translate").click(() => {
    action();
  });
  $("#language_code").keypress((event) => {
    if (event.key === "Enter") action();
  });
};
