var express = require('express');
var router = express.Router();
var User = require('../schemas/user');

/* GET users listing. */
// router.get('/', function(req, res, next) {
// 	res.send('respond with a resource');
// });

router.post('/checkuser', function (req, res) {
	const user = new User({
		user_id: req.body.user
	});
  	User.findOne({ user_id: user.user_id })
		.then((result) => {
			console.log("ASDF");
			res.json(200, {data : result});
		})
		.catch((err) => {
			console.error(err);
			next(err);
		});
});

/**
 * 로그인
 * POST /api/users/login
 */
router.post('/login', function(req, res, next) {
	console.log('login in');
	const user = new User({
		user_id: req.body.user.id,
		user_pw: req.body.user.password
	});
		
	User.findOne({ user_id: user.user_id })
		.then((result) => {
			if (!result) {
				// 이메일도 비밀번호도 틀림
				res.json(200, { success:false, message:`아이디도 비밀번호도 틀림` });
			} else if (result.user_pw === user.user_pw) {
				// 로그인 성공
				res.json(200, { success:true, message:`${user.user_id} : 로그인 성공` });
			} else {
				// 이메일만 성공
				res.json(200, { success:false, message:`비밀번호가 틀림` });
			}
		})
		.catch((err) => {
			console.error(err);
			next(err);
		});
});


/**
 * 회원가입
 * POST /api/users/register
 */
router.post('/register', function(req, res, next) {
	console.log('register in');
	const user = new User({
		user_id: req.body.user.id,
		user_pw: req.body.user.password
	});
	
	user.save()
		.then((result) => {
			console.log(result);
			res.json(200, { success:true, message:'회원가입에 성공했습니다. 같은 메세지' });
		})
		.catch((err) => {
			console.error(err);
			next(err);
		});
	
});



module.exports = router;
