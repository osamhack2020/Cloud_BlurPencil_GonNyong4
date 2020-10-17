var express = require('express');
var router = express.Router();

var User = require('../schemas/user');
var Work = require('../schemas/work');

/**
 * 작업물 불러오기
 * GET /api/works
 */
router.get('/', function(req, res, next) {
	const user_id = req.query.user_id;
	
	User.findOne({ user_id: user_id }, { _id: true })
		.then((result) => {
			console.log(result);
			return Work.find({ user_oid: result._id });
		})
		.then((result) => {
			result.success = true;
			res.json(200, result);
			console.log(result);
		})
		.catch((err) => {
			console.error(err);
			next(err);
		})
});

module.exports = router;