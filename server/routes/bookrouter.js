const express = require('express');
const bookController = require('../controllers/bookcontroller');
const router= express.Router();

router.post('/books', bookController.createBook);
router.post('/getBook', bookController.getBook);
router.post('/deleteBook', bookController.deleteBook);
router.post('/updateBook', bookController.updateBook);

module.exports = router;