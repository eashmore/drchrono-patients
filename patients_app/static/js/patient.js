function showLoadingScreen() {
  $('#save-screen').removeClass('display-none');
}

(function() {
  $('#nav-patient').addClass('active');
  $('#update-patient-btn').click(showLoadingScreen);
})();
