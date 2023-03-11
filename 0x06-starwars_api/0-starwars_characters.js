#!/usr/bin/node
const request = require('request');
if (process.argv.length != 3) {
  console.error('Usage: ./0-starwars_characters.js N');
  process.exit(1);
}