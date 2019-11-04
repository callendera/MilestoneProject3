var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var userSchema = new Schema({
  user_name: { type: String,  required: [true, 'Username must be provided'] },
  password: { type: String , required: [true,  'Password cannot be left blank']},
  
});
module.exports = mongoose.model('users', userSchema);

//Code above from: 'http://programmerblog.net/nodejs-user-registration-tutorial/'