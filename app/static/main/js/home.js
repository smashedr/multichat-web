// Document Dot Ready
$(document).ready(function() {
    // Add Bot Function
    $('#add-bot-btn').click(function () {
        console.log('button clicked...');
        $('#add-bot-form').submit();
        return false;
    });
});
