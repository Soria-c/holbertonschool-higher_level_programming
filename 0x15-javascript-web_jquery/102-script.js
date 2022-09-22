window.onload = () => {

$("#add_item").click(() => {
  $(".my_list").append("<li>Item</li>");
});

$("#remove_item").click(() => {
  
  $(".my_list").children().last().remove();
})


$("#clear_list").click(() => {
  $(".my_list").text("");
})
};
