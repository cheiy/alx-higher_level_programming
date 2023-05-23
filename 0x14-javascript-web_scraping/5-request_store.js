#!/usr/bin/node
const req = require('request');
const process = require('process');
const file = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

req(url).pipe(file.createWriteStream(filePath, 'utf8'));
