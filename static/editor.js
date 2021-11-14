$(document).ready(function(){
    CodeMirror.defineSimpleMode("smt2", {
        start: [
            {
                regex: /(assert|check-sat|check-sat-assuming|declare-const|declare-datatype|declare-datatypes|declare-fun|declare-sort|define-fun|define-fun-rec|define-sort|echo|exit|get-assertions|get-assignment|get-info|get-model|get-option|get-proof|get-unsat-assumptions|get-unsat-core|get-value|pop|push|reset|reset-assertions|set-info|set-logic|set-option)\b/,
                token: "builtin"
            },
            {
                regex: /(ite|and|or|xor|not|in|str\.\+\+|str\.len|str\.substr|str\.indexof|str\.at|str\.contains|str\.prefixof|str\.suffixof|str\.replace|str\.to\.int|int\.to\.str|str\.to\.re|str\.in\.re|re\.allchar|re\.nostr|re\.range|re\.\+\+|re\.\*|re\.\+|re\.opt|re\.loop|re\.union|re\.inter|re\.all|re\.empty)\b/,
                token: "keyword"
            },
            {
                regex: /(\d+|true|false)/,
                token: "number"
            },
            {
                regex: /"(?:[^\\]|\\.)*?(?:"|$)/,
                token: "string"
            },
            {
                regex: /;.*/,
                token: "comment"
            }
        ]
    });
    var code = $("#formula")[0];
    var editor = CodeMirror.fromTextArea(code, {
        lineNumbers: true,
        autofocus: true,
        autoCloseBrackets: true,
        matchBrackets: true
    });
    editor.setSize(null, 450);
})