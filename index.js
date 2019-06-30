const testAddon = require('./build/Release/mylib.node')

console.log('addon', testAddon)
msg = testAddon.hello()
console.log(msg)

module.exports = testAddon
