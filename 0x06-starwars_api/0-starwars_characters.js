#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      const responseBody = JSON.parse(body);

      if (error) {
        reject(error);
      } else {
        resolve(responseBody.name);
      }
    });
  });
}

function fetchData () {
  request(url, async function (error, response, body) {
    const responseBody = JSON.parse(body);

    if (error) {
      console.error('error:', error);
    }

    for (let i = 0; i < responseBody.characters.length; ++i) {
      const name = await getCharacterName(responseBody.characters[i]);

      console.log(name);
    }
  });
}

fetchData();
