const hamburgerBtn = document.getElementById('hamburgerBtn');
hamburgerBtn.addEventListener('click', () => {
  sideMenu.classList.toggle('open');
})
// default the dates to today and 12 months from now
  let today = new Date();
  $("#startDate").val(serializeDate(today));

  let endDate = new Date();
  endDate.setDate(today.getDate() + 365);
  $("#endDate").val(serializeDate(endDate));
