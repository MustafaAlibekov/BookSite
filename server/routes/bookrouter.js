const express = require('express');
const bookController = require('../controllers/bookcontroller');
const router= express.Router();

router.post('/createBook', bookController.createBook);
router.get('/getBook', bookController.getBook);
router.delete('/deleteBook', bookController.deleteBook);
router.put('/updateBook', bookController.updateBook);
router.get('/getAllBooks', bookController.getAllBooks);

module.exports = router;