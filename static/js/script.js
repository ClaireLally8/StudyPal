const hamburgerBtn = document.getElementById('hamburgerBtn');
hamburgerBtn.addEventListener('click', () => {
  sideMenu.classList.toggle('open');
})

function serializeDate(date) {
  // this YYYY-MM-DD format is the same serialization used in HTML date input values
  return date.toISOString().split("T")[0];
}
  let startDate = new Date();
  $("#startDate").val(serializeDate(startDate));

  let endDate = new Date();
  endDate.setDate(startDate.getDate() + 365);
  $("#endDate").val(serializeDate(endDate));

  let milSec = 1000 * 60 * 60 * 24;
  let scheduleLength = Math.round((endDate - startDate)/milSec);
  $("#scheduleLength").html(scheduleLength);