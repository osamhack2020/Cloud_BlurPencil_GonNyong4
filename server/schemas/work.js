const mongoose = require('mongoose');

const { Schema } = mongoose;
const { Types: { ObjectId } } = Schema;
const workSchema = new Schema({
	// 유저 아이디
	user_oid: {
		type: ObjectId,
		ref: 'User',
		required: true
	},
	// 작업내역
	fileName: {
		type: String,
		default: '',
		required: true
	},
	score: {
		type: Number,
		default: 0
	},
	nms: {
		type: Number,
		default: 0	
	},
	// 작업날짜
	workedAt: {
		type: Date,
		default: Date.now
	}
});

module.exports = mongoose.model('Work', workSchema);