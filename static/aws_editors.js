$(document).ready(function(){
    var policy1 = $("#policy1")[0];
    var editor1 = CodeMirror.fromTextArea(policy1, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor1.setSize("100%", 400);

    var policy2 = $("#policy2")[0];
    var editor2 = CodeMirror.fromTextArea(policy2, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor2.setSize("100%", 400);
})