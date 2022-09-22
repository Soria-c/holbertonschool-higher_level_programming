window.onload = () => {

  $("#btn_translate").click(() => {
    const value = $("#language_code").val()
    $.ajax({
      type: 'GET',
      url: `https://stefanbohacek.com/hellosalut/?lang=${value}`,
      success: function(data){
        $('#hello').text(data.hello);
      },
      error: function() {
        alert('Error for loading API');
      }
    });
  });
};
