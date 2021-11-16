$(document).ready(function(){
    var rd = $("#roledefinition")[0];
    var editor_rd = CodeMirror.fromTextArea(rd, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_rd.setSize("100%", 400);

    var ra = $("#roleassignments")[0];
    var editor_ra = CodeMirror.fromTextArea(ra, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor_ra.setSize("100%", 400);
})