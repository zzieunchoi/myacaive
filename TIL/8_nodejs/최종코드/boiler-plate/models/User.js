const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
// saltrounds
const saltRounds = 10;
const jwt = require('jsonwebtoken');
const userSchema = mongoose.Schema({
  name: {
    type: String,
    maxlength: 50
  },
  email: {
    type: String,
    trim : true,
    unique:1
  },
  password: {
    type: String,
    maxlength: 150
  },
  role : {
    type : Number,
    default: 0
  },
  image: String,
  token: {
    type: String
  },
  tokenExp: {
    type: Number
  }
})

userSchema.pre('save', function(next) {
  // userSchema를 가리킴
  var user = this
  
  // 비밀번호를 변경 할 때만 암호화해야하므로 조건 필요!
  if(user.isModified('password')) {
      // 비밀 번호를 암호화 시킨다.
      bcrypt.genSalt(saltRounds, function(err, salt) {
          if(err) return next(err)
          //salt를 제대로 생성했다면
          bcrypt.hash(user.password, salt, function(err, hash) {
              if(err) return next(err)

              user.password = hash
              // save전에 실행한 거니까 다 되면 save로 넘어감
              next()
          });
      });
  } else {
    next()
  }
})

userSchema.methods.comparePassword = function(plainPassword, cb) {
    bcrypt.compare(plainPassword, this.password, function(err, isMatch) {
        if(err) return cb(err)
        cb(null, isMatch)
    })
}

userSchema.methods.generateToken = function(cb) {
    var user = this;
    //jsonwebtoken을 이용해서 
    var token = jwt.sign(user._id.toHexString(), 'secretToken')
    user.token = token
    user.save(function (err, user) {
        if(err) return cb(err)
        cb(null, user)
    })
}

userSchema.statics.findByToken = function(token, cb) {
  var user = this;
  
  // 토큰을 decode한다
  jwt.verify(token, 'secretToken', function(err, decoded) {
      //유저 아이디를 이용해서 유저를 찾은 다음에 
      //클라이언트에서 가져온 token과 DB에 보관된 토큰이 일치하는지 확인
      user.findOne({"_id" : decoded, "token": token}, function(err, user) {
          if(err) return cb(err);
          cb(null, user)
      })
  })
}
const User = mongoose.model('User', userSchema)

module.exports = {User}