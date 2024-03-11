#!/usr/bin/node

const cont = process.argv.length

if (cont <= 2) {
    console.log('No argument');
} else if (cont <= 3) {
    console.log('Argument found');
} else {
    console.log("Arguments found");
}
