#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  let i = 0 ;
  while ((l - i) > 0) {
    const aux = list[l];
    list[l] = list[i];
    list[i] = aux;
    i++;
    l--;
  }
  return list;
};
