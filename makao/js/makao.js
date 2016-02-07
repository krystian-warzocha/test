var hand = ['2&#9824;', '9&#9824;', '10&#9824;']

$('document').ready(function() {

	$('#hand').sortable({
		connectWith: '.connected',
		placeholder: 'ui-state-highlight'
	});

	$('#table').sortable({
		connectWith: '.connected',
		placeholder: 'ui-state-highlight',
		items: 'li:not(.ui-state-disabled)'
	});

	$('button').button().on('click', function(event) {
		event.preventDefault();
		alert('Button was clicked!');
	});

	$.getScript('js/game.js', function(data, textStatus, jqxnr) {
		console.log(data);
		console.log(textStatus);
		console.log(jqxnr);
		console.log('Load was performed');
	});

});
