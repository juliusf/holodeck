$(function() {
    $('a#run').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_interpret', {
        statement: $('textarea[name="input"]').val()
      }, function(data) {
        $("#console").text(data.result);
      });
      return false;
    });
  });