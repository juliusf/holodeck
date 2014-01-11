$(function() {
    $('a#run').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_interpret', {
        statement: editor.getSession().getValue()
      }, function(data) {
        $("#console").text(data.result);
      });
      return false;
    });
  });