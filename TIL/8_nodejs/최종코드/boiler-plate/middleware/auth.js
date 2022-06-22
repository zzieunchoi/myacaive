const {User} = require('../models/User')
let auth = (req, res, next) => {
    //쿠키에서 토큰을 가져온다
    let token = req.cookies.x_auth;
    
    // 토큰을 복호화한후에 유저를 찾는다
    User.findByToken(token, (err, user) => {
        if(err) throw err;
        if(!user) return res.json({isAuth: false, error: true})
        // 이걸 넣어야 index.js의 app.get에서 req.user를 사용할 수 있음!
        req.token = token;
        req.user = user;
        next();
    })
}

module.exports = {auth};