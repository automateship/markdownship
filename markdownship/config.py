
default_template='''<!DOCTYPE HTML>
<html>

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style type="text/css">
      html {
        font-family: verdana, arial;
      }
      body {
        color             : #000;
        background-color  : #fff;
      }
  
      table {
        font-family: mono;
        font-size         : 80%;
        border-width      : 1px;
        border-color      : #666;
        border-collapse   : collapse;
      }
      table th {
        border-width      : 1px;
        padding           : 8px;
        border-style      : solid;
        border-color      : #666;
        background-color  : #eee;
      }
      table td {
        border-width      : 1px;
        padding           : 8px;
        border-style      : solid;
        border-color      : #666;
      }
  
      code {
        color             : #000;
        background-color  : #eee;
        padding           : 2px;
        margin            : 0px;
      }
      .codehilite {
        color             : #000;
        background-color  : #eee;
        border-style      : solid;
        border-width      : 1px;
        border-color      : #666;
        border-radius     : 5px;
        padding           : 6px;
        overflow          : auto;
      }
      .codehilite code {
        background-color  : #eee;
        padding           : 0px;
        margin            : 0px;
      }

      blockquote {
        padding-left      : 5px;
        border-color      : #aaa;
        border-style      : solid;
        border-width      : 0 0 0 5px;
      }
  
      #wrapper {
        width             : 700px;
        margin            : 0 auto;
        padding           : 0px;
      }
      #contents {
        background-color  : #fff;
        margin            : 10px 0 10px 0;
        padding           : 10px;
        border-style      : solid;
        border-width      : 1px;
        border-color      : #ddd;
        border-radius     : 3px;
      }

      h1 {
        border-style      : solid;
        border-width      : 0 0 1px 0;
        border-color      : #aaa;
      }
  
      h2 {
        border-style      : solid;
        border-width      : 0 0 1px 0;
        border-color      : #ddd;
      }
  
    </style>
  </head>

  <body>
    <div id='wrapper'>
      <div id='contents'>
        %markdown%
      </div>
    </div>
  </body>

</html>
'''
