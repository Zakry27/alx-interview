#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Executes API request to obtain information about films.
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parses response body to obtain list of character URLs.
  const charURLList = JSON.parse(body).characters;

  // Extracts character information by iterating through character URLs.
  // Requests each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Examines character information and prints name of character. Confirms promise to indicate completion.
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
