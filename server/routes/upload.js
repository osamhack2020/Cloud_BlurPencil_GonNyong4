var express = require('express');
var router = express.Router();
var path = require('path');

var User = require('../schemas/user');
var Work = require('../schemas/work');

var multer = require('multer');
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'tempUploads/');
  },
  filename: function (req, file, cb) {
    cb(null, new Date().valueOf() + path.extname(file.originalname));
  }
})
const upload = multer({ storage: storage });


/* 
	POST /upload
*/
router.post('/', upload.array('imgUploads'), function(req, res){
	// 아이디를 저장할지 ObjectId를 저장할지 아직 미정이라 임시로 작성합니다.
	// asdf 는 테스트 용도 임시 아이디입니다.
	const user_id = 'asdf';
	
	User.findOne({ user_id: 'asdf' }, '_id')
		.then((user) => {
			const works = [];
			for (var work of req.files) {
				works.push( { user_oid: user._id, fileName: work.filename } );
			}
			return Work.insertMany(works);
		})
		.then((result) => {
			res.send('Uploaded! : '+ req.files);
		})
		.catch((err) => {
			next(err);
		});
});

module.exports = router;