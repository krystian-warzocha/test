console.log('Script has been loaded');

var Card = function(symbol, color) {
	this.symbol = symbol;
	this.color = color;
}

var Hand = function(cards) {
	this.cards = cards;
}
