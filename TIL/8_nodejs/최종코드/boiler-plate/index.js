const express = require('express')
const app = express()
const port = 5000
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser')
const config = require('./config/key')
const {User} = require("./models/User");

const {auth} = require('./middleware/auth');

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(cookieParser())
const mongoose = require('mongoose')
mongoose.connect(config.mongoURI, {
  useNewUrlParser: true, useUnifiedTopology:true
}).then(() => console.log("MongoDB connected..."))
.catch(err => console.log(err))

app.get('/', (req, res) => { res.send('안녕하세요') })

app.post('/api/users/register', (req,res) => {
  // 회원가입 할때 필요한 정보들을 client에서 가져오면
  // 그것들을 데이터 베이스에 넣어준다.
    // req.body에 json 형식으로 데이터가 있음
    const user = new User(req.body)


    // 정보 저장
    user.save((err, userInfo) => {
        if(err) return res.json({success :false, err})
        return res.status(200).json({
            success:true
        })
    })
})


app.post('/api/users/login', (req, res) => {
  // 요청된 이메일이 데이터 베이스에 있는지 찾는다
  User.findOne({ email: req.body.email }, (err, user) => {
      if(!user) {
          return res.json({
              loginSuccess:false, 
              message: '이메일에 해당하는 유저가 없습니다.'
          })
      }
      
      // 요청된 이메일이 데이터베이스에 있다면 비밀번호가 맞는지 확인
      user.comparePassword(req.body.password, (err, isMatch) => {
          if(!isMatch)
              return res.json({
                  loginSuccess:false,
                  message: "비밀번호가 틀렸습니다"})
          // 비밀번호가 같다면 token 생성
          user.generateToken((err, user) => {
              if(err) return res.status(400).send(err);
              
              // user에 token이 저장되어있음
              // 토큰을 어디에 저장한다? 자유롭게 저장(쿠키, 로컬 스토리지)할 수 있지만 지금은 쿠키
              res.cookie("x_auth", user.token)
              .status(200)
              .json({loginSuccess:true, userId : user._id})  
          })
      }) 
  })   
})

app.get('/api/users/auth', auth, (req,res) => {
  // 미들웨어를 통과했다 = authentication이 true라는 말
  res.status(200).json({
      _id: req.user._id,
      // role이 0이면 유저 role이 0이 아니면 관리자
      // 나중에 변경 가능
      isAdmin: req.user.role === 0 ? false: true,
      isAuth: true, 
      email: req.user.email,
      name: req.user.name,
      lastname: req.user.lastname,
      role:req.user.role,
      image:req.user.image
  })
})

app.get('/api/users/logout', auth, (req, res) => {
  User.findOneAndUpdate({_id: req.user._id}, { token: ""} , (err, user) => {
      if(err) return res.json({success:false, err});
      return res.status(200).send({
          success:true
      })
  })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})