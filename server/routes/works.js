var express = require('express');
var router = express.Router();

var User = require('../schemas/user');
var Work = require('../schemas/work');

/**
 * 작업물 불러오기
 * GET /api/works
 */
router.get('/:user_id', function(req, res, next) {
	const user_id = req.params.user_id || '';
	const limit = Number(req.query.limit) || 5;
	const skip = Number(req.query.skip) || 0;
	const sort = Number(req.query.sort) || -1;
	
	User.findOne({ user_id: user_id }, { _id: true })
		.then((result) => {
			console.log(result);
			return Work.find({ user_oid: result._id }).skip(skip).limit(limit).sort({workedAt: sort});
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