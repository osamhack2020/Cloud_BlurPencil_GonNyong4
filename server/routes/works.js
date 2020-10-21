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

router.post('/delete/:user_id', function(req, res, next) {
	const user_id = req.params.user_id || '';
	const work_oid = req.body.work_oid || '';
	const fileName = req.body.fileName || '';
	
	Work.deleteOne({ _id: work_oid, fileName: fileName })
		.then((result) => {
			if (result && result.deletedCount > 0 && result.n) {
				const fs = require('fs');
				const path = `./tempUploads/${fileName}`;
				
				fs.unlink(path, (err) => {
					if (err) {
						console.error(err);
					return;
				}});
				res.json(200, { success:true, message:`${fileName}이 삭제되었습니다.`});
			}
			else
				res.json(200, { success:false, message:`파일이름(${fileName}) 혹은 oid값(${work_oido})이 틀렸습니다.`});
		})
		.catch((err) => {
			console.error(err);
			next(err);
		})
});

module.exports = router;