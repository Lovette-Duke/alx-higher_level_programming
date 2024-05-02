#!/usr/bin/node

$(document).ready(function(){
  // When the user clicks on DIV#red_header
  $('div#red_header').click(function(){
    // Update the text color of the header to red
    $('header').css('color', '#FF0000');
  });
});
