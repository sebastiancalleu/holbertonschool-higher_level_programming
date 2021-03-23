#!/usr/bin/node

const ob1 = require('./100-data');
const lt1 = ob1.list;
const lt2 = lt1.map((currElement, index) => { return currElement * index; });
console.log(lt1);
console.log(lt2);
