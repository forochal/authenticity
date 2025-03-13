//H STANDS FOR HEATHLANDS
//A STANDS FOR AN ABANDONED BUILDING
//U STANDS FOR RUINS

const http = require('http');
const fs = require("fs");
const { Buffer } = require('node:buffer');

const homePage = fs.readFileSync('./index.html');
const homeStyles = fs.readFileSync('./styles.css');
//const homeJS = fs.readFileSync('./authenticity.js'); //this doesn't work for some reason

const server = http.createServer(
function (req, res) 
{
	if (req.url === '/')
	{
		res.setHeader("Content-Type", "text/html")
            	res.write(homePage);
		res.write('Date: ' + Game1.date + '\n');
		res.write('Money: ' + Game1.money + '\n');
		res.write('Population: ' + Game1.population + '\n');
		res.write('Current residential tax: ' + Game1.residential_tax + '\n');
		res.write('Current industrial tax: ' + Game1.industrial_tax + '\n');
		res.write('Current commercial tax: ' + Game1.commercial_tax + '\n');
		res.write('<br>');
		res.write('Land use map:');
		res.write('<br>');
		for (let i = 0; i < land_use.length; i++)
		{
			res.write(JSON.stringify(land_use[i]));
			res.write('<br>');
		}
		res.write('<br>');
		res.write('Pollution map:');
		res.write('<br>');
		
		for (let i = 0; i < pollution.length; i++)
		{
			res.write(JSON.stringify(pollution[i]));
			res.write('<br>');
		}
		res.write('<br>');
		res.write('Life expectancy map:');
		res.write('<br>');
		for (let i = 0; i < life_expectancy.length; i++)
		{
			res.write(JSON.stringify(life_expectancy[i]));
			res.write('<br>');
		}
		//res.send(`&lt;img src="./images/zone_residential.png" alt="Zone Residential"&gt;`);
	 	res.end();
	}
	else if(req.url === '/styles.css')
	{
		res.writeHead(200, {'content-type': 'text/css'});
		res.write(homeStyles);
		res.end();
        }
        /*else if(req.url === '/authenticity.js') //this doesn't work for some reason
	{
		res.writeHead(200, {'content-type': 'text/javascript'});
		res.write(homeJS);
		res.end();
        }*/
});

var land_use = new Uint8Array();
var pollution = new Uint8Array();
var life_expectancy = new Uint8Array();


land_use = [["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"]];
pollution = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]];
life_expectancy = [[70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0]];

//var buf1 = Buffer.alloc(7);
//var buf2 = Buffer.alloc(7);
//var buf3 = Buffer.alloc(7);


//console.log('test message');

function Game() {
    this.money = "10000";
    this.date = "1900.0";
    this.population = "1";
    this.industrial = "0";
    this.commercial = "0";
    this.seervices = "0";
    this.residential_demand = "50";
    this.industrial_demand = "50";
    this.commercial_demand = "50";
    this.residential_tax = "11";
    this.industrial_tax = "11";
    this.commercial_tax = "11";
    this.electric_power = Boolean(0);
    this.failed = Boolean(0);
}

// Add a method to set a variable value
Game.prototype.setVariable =
    function (Game) {
        //this.electric_power = Boolean(1);
    };

// Add a method to display text
Game.prototype.main =
    function () {
        console.log(
            "Date: {} " + this.date +
            "Money: {}" + this.money +
            "Population: {}" + this.population +
            "Zone residential, commercial, industrial, build a public seervices building (p), build a generator (g), do nothing (n)?" +
            "Current taxes: "
        );
    };

// Create an object
var Game1 = new Game();

//server.on('connection', (socket)
server.listen(3000);

console.log('Listening on port 3000....');

// Call the method
Game1.main();
