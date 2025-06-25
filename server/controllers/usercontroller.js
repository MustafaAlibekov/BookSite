const {pool} = require('../db');
 exports.createUser = async (req, res) => 
    {
        const {username, login, password, role} = req.body;
        try
        {
            const result = await pool.query('INSERT INTO users(username, login, password, role) values ($1,$2,$3,$4)',[username, login, password, role]);
            res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
    }

 exports.deleteUser = async (req, res) => 
    {
        const {userID} = req.body;
        try
        {
            const result = await pool.query('DELETE FROM users where "userID" = $1',[userID]);
               res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
    }

 exports.updateUser = async (req, res) => 
    {
        const {userID, username, login, password, role} = req.body;
        try
        {
            const result = await pool.query('Update users SET username = $1, login=$2, password=$3, role = $4 WHERE "userID" = $5',[username, login, password, role, userID]);
        res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
    }
exports.getUser = async (req, res) => {
    const { userID } = req.body;

    try {
        const result = await pool.query(
            'SELECT username, login, role FROM users WHERE "userID" = $1',
            [userID]
        );

        if (result.rows.length === 0) {
            return res.status(404).json({ error: 'User not found' });
        }

        res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
