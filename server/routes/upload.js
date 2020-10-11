var express = require('express');
var router = express.Router();
var path = require('path');

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
	res.send('Uploaded! : '+ req.files);
	res.status(204).end();
});

module.exports = router;