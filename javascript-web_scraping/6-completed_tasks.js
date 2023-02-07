#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
const result = {}
let count = 1
request.get(url, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(res.body);

    data.forEach(element => {
      if (element.completed === true){
        result[count] = element.id;
        count ++;
      }
    });
  }
  console.log(result)
});
