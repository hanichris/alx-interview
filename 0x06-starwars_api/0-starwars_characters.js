#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js N');
  process.exit(1);
}

const movieId = process.argv[2]
const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Accept-charset': 'utf-8'
  }
};

request(options, (err, res, body) => {
  let characters = JSON.parse(body).characters;
  for (const element of characters) {
    request(element, (err, res, body) => {
      console.log(JSON.parse(body).name);
    })
  }
});