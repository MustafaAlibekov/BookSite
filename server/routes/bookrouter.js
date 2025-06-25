const express = require('express');
const bookController = require('../controllers/bookcontroller');
const router= express.Router();

router.post('/books', bookController.createBook);
router.post('/getBook', bookController.getBook);

module.exports = router;