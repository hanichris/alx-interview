#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js N');
  process.exit(1);
}

const movieId = process.argv[2];
const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-charset': 'utf-8'
  }
};

request(options, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    displayCharacters(characters)
      .then(result => {
        for (const name of result) {
          console.log(name);
        }
      })
      .catch(error => { console.log(error); });
  }
});

const displayCharacters = async people => {
  const data = [];
  for (const person of people) {
    data.push(await new Promise((resolve, reject) => {
      request(person, (err, res, body) => {
        if (err) {
          console.error(err);
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    }));
  }
  return data;
};
