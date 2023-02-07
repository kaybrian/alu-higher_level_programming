#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(res.body);
    fs.writeFile(filePath, data, (err) => {
      if (err) {
        console.log(err);
      } else {
        fs.readFileSync(filePath, 'utf8');
      }
    });
  }
});
