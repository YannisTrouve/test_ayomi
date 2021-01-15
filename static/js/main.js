
// function allowing the use of Modal panel
$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})