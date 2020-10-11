var express = require('express');
var path = require("path");
var router = express.Router();

/* 
	GET /
*/
router.get('/', function(req, res, next) {
  // res.render('fileUpload', { title: 'Express' });
	res.sendFile(path.join(__dirname, '../public','index.html'));
});
router.get('/upload', function(req, res, next) {
  // res.render('fileUpload', { title: 'Express' });
	res.sendFile(path.join(__dirname, '../public','index.html'));
});
router.get('/login', function(req, res, next) {
  // res.render('fileUpload', { title: 'Express' });
	res.sendFile(path.join(__dirname, '../public','index.html'));
});
router.get('/main', function(req, res, next) {
  // res.render('fileUpload', { title: 'Express' });
	res.sendFile(path.join(__dirname, '../public','index.html'));
});

module.exports = router;
