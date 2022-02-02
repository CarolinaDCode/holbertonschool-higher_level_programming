#!/usr/bin/node
/* script that prints the title of a Star Wars movie */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const episodeNumber = process.argv[2];
request(url + episodeNumber, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
})
