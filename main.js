var experience = [
    "Use this to search for possible illnesses",
    "And helpful information for cures",
    "Hello, welcome to medi helper"

];
var len = experience.length;
var i = 0;
function fadeInAndOut(divID, experience, interval) {
    setInterval(function () {
        $(divID).fadeOut('slow', function() {
            $(this).text(experience[i]);
            $(this).fadeIn('slow');
            i += 1;
            if (i == len) {
               i = 0
            }
        });
    }, interval);
}
fadeInAndOut("#heading", experience, 3000);