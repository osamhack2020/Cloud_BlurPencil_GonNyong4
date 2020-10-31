var express 	= require('express');
var path 		= require('path');
var favicon 	= require('serve-favicon');
var logger 		= require('morgan');
var cookieParser= require('cookie-parser');
var bodyParser 	= require('body-parser');
var cors 		= require('cors')

var index 		= require('./routes/index');
var upload 		= require('./routes/upload');
var uploadpage 	= require('./routes/uploadpage');
var users 		= require('./routes/users');
var works 		= require('./routes/works');
var folders		= require('./routes/folders');

var connectMongoDB = require('./schemas');

var app = express();
connectMongoDB();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(cors());
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'tempUploads')));

app.use('/', index);
app.use('/api/upload', upload);
app.use('/api/users', users);
app.use('/api/works', works);
app.use('/api/folders', folders);
app.use('/uploadpage',uploadpage);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

app.listen(process.env.PORT || 3000, () => console.log('Example app listening on port 3000!'));

module.exports = app;
