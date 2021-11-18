$(document).ready(function(){
    var rd = $("#roledefinitions")[0];
    var editor_rd = CodeMirror.fromTextArea(rd, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_rd.setSize("100%", 400);

    var ra1 = $("#roleassignment1")[0];
    var editor_ra1 = CodeMirror.fromTextArea(ra1, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_ra1.setSize("100%", 180);

    var ra2 = $("#roleassignment2")[0];
    var editor_ra2 = CodeMirror.fromTextArea(ra2, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_ra2.setSize("100%", 180);
})