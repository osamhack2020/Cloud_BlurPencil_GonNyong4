const mongoose = require('mongoose');

const { Schema } = mongoose;
const { Types: { ObjectId } } = Schema;
const folderSchema = new Schema({
	folderName: {
		type: String,
		default: '임시폴더',
		required: true
	},
	owner: {
		type: ObjectId,
		ref: 'User',
		required: true
	},
	share: [{
		type: ObjectId,
		ref: 'User'
	}]
});

module.exports = mongoose.model('Folder', folderSchema);