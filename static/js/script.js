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

  
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}