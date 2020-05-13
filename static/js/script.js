$(document).ready(function () {
    $('.subjectmodal').modal();
    $('.loginmodal').modal();
    $('.topicmodal').modal();
    $('.notesmodal').modal();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.dropdown-trigger').dropdown();
});
const hamburgerBtn = document.getElementById('hamburgerBtn');
hamburgerBtn.addEventListener('click', () => {
    sidemenunav.classList.toggle('open');
})
/** code by webdevtrick ( https://webdevtrick.com ) **/
var accordions = document.getElementsByClassName("accordion");

for (var i = 0; i < accordions.length; i++) {
    accordions[i].onclick = function () {
        this.classList.toggle('is-open');

        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            // accordion is currently open, so close it
            content.style.maxHeight = null;
        } else {
            // accordion is currently closed, so open it
            content.style.maxHeight = content.scrollHeight + "px";
        }
    }
}

function toggle_complete(topics_id) {
    $.ajax({
        type: "GET",
        url: "/toggle",
        data: topics_id,

        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error);
        }
    });
    event.preventDefault(); 
        return true;
}

