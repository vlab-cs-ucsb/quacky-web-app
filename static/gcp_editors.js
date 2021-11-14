$(document).ready(function(){
    var role = $("#role")[0];
    var editor_role = CodeMirror.fromTextArea(role, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_role.setSize("100%", 400);

    var rb = $("#rolebindings")[0];
    var editor_rb = CodeMirror.fromTextArea(rb, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_rb.setSize("100%", 400);
})