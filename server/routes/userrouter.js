const express = require('express');
const UserController = require('../controllers/usercontroller');
const router= express.Router();

router.post('/users', UserController.createUser);
// router.get('/users', UserController.getAllUsers);
router.get('/user', UserController.getUser);
router.put('/users/:id', UserController.updateUser);
router.delete('/users/:id', UserController.deleteUser);


module.exports = router;

