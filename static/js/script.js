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
});
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
    };
}

function toggle_complete(topics_id) {
    $.ajax({
        type: "POST",
        url: "/toggle/"+topics_id,
        data: topics_id,

        success: function (response) {
            togglecheck(topics_id);
            console.log(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
    event.preventDefault(); 
        return true;
}

function togglecheck(topics_id)
{
    var isComplete = "isComplete" + topics_id;
    var id = document.getElementById(topics_id);
    var section = document.getElementById(isComplete);
    if (id.checked)
    {
        id.checked = false;
        section.classList.remove("isComplete");

    }
    else {
        id.checked = true;
        section.classList.add("isComplete");
    }
}