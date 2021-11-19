$(document).ready(function(){
    var role = $("#role")[0];
    var editor_role = CodeMirror.fromTextArea(role, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_role.setSize("100%", 400);

    var rb1 = $("#rolebindings1")[0];
    var editor_rb1 = CodeMirror.fromTextArea(rb1, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_rb1.setSize("100%", 180);

    var rb2 = $("#rolebindings2")[0];
    var editor_rb2 = CodeMirror.fromTextArea(rb2, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_rb2.setSize("100%", 180);
})