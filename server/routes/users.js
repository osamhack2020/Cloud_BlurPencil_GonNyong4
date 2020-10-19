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
 * 유저정보
 * GET /api/users
 */
router.get('/', function(req, res, next) {
	const user_id = req.query.user_id;
	
	User.findOne({ user_id: user_id }, { user_pw: false })
		.then((result) => {
			if (result)
				res.json(200, { success:true, data:result, message:`${user_id} 의 정보` });
			else
				res.json(404, { success:false, message:`${user_id}는 없는 유저입니다.` });
		})
		.catch((err) => {
			console.error(err);
			next(err);
		})
});


/**
 * 로그인
 * POST /api/users/login
 */
router.post('/login', function(req, res, next) {
	const user = new User({
		user_id: req.body.user.id,
		user_pw: req.body.user.password
	});
		
	User.findOne({ user_id: user.user_id })
		.then((result) => {
			if (!result) {
				// 이메일도 비밀번호도 틀림
				return { success:false, message:`아이디도 비밀번호도 틀림` };
			} else if (result.user_pw === user.user_pw) {
				// 로그인 성공
				return User.updateOne({ user_id: user.user_id }, { user_updatedAt: new Date().toISOString() });		
			} else {
				// 이메일만 성공
				return { success:false, message:`비밀번호가 틀림` };
			}
		})
		.then((result) => {
			if (result.ok)
				res.json(200, { success:true, message:`${user.user_id} : 로그인 성공` });
			else
				res.json(200, result);
			
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
	const user = new User({
		user_id: req.body.user.id,
		user_email: req.body.user.email,
		user_pw: req.body.user.password
	});
	
	user.save()
		.then((result) => {
			res.json(200, { success:true, message:'회원가입에 성공했습니다. 같은 메세지' });
		})
		.catch((err) => {
		    if (err) {
				if (err.name === 'MongoError' && err.code === 11000)
					res.send({ success: false, message: '이미 존재한 아이디입니다.' });
				else
					next(err);
			}
		});
	
});


/**
 * 비밀번호 변경
 * PATCH /api/users/password
 */
router.patch('/password', function(req, res, next) {
	const user_id = req.body.user_id;
	const user_prev_pw = req.body.user_prev_pw;
	const user_want_pw = req.body.user_want_pw;
		
	User.findOne({ user_id: user_id, user_pw: user_prev_pw })
		.then((result) => {
			if (result)
				return User.updateOne({ user_id: user_id , user_pw: user_prev_pw }, { user_pw: user_want_pw });
			return { success:false, message:`아이디 혹은 비밀번호가 틀렸습니다.` };
		})
		.then((result) => {
			if (result.ok && result.nModified)
				res.json(200, { success:true, message:`${user_id}의 비밀번호가 변경되었습니다.` });
			else
				res.json(400, result);
		})
		.catch((err) => {
			console.error(err);
			next(err);
		});
});

/**
 * 비밀번호 분실시
 * POST /api/users/password
 * TODO : 차후 이메일 인증 기능을 넣게 되면 이메일 인증코드를 받고나서 가능하도록 변경해야함.
 */
router.post('/password', function(req, res, next) {
	const user_id = req.body.user_id;
	const user_email = req.body.user_email;
	const user_want_pw = req.body.user_want_pw;
	
	User.updateOne({ user_id: user_id, user_email: user_email }, { user_pw: user_want_pw })
		.then((result) => {
			if (result.ok && result.nModified)
				res.json(200, { success:true, message:`${user_id}의 비밀번호가 변경되었습니다.` });
			else
				res.json(400, result);
		})
		.catch((err) => {
			console.error(err);
			next(err);
		});
});

/**
 * 회원 탈퇴
 * POST /api/users/delete
 */
router.post('/delete', function(req, res, next) {
	const user_id = req.body.user_id, 
		  user_pw = req.body.user_pw;
	
	User.deleteOne({ user_id: user_id, user_pw: user_pw })
		.then((result) => {
			console.log(result);
			res.json(200, { success:true, message:`${user_id} : 회원탈퇴`});
		})
		.catch((err) => {
			console.error(err);
			next(err);
		})
});

module.exports = router;
