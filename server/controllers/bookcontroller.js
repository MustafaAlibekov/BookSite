const {pool} = require('../db');

exports.createBook = async (req, res) => 
    {
        const {bookname, imagelink, rateid, categoryid, authorid, booklink} = req.body;
        try
        {
            const result = await pool.query('INSERT INTO books(bookname, imagelink, rateid, categoryid, authorid, booklink) values ($1,$2,$3,$4, $5, $6)',[bookname, imagelink, rateid, categoryid, authorid, booklink]);
            res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
    }

exports.getBook = async (req, res) => {
    const { bookname } = req.body;

    try {
        const result = await pool.query(
            'SELECT bookname, imagelink, rateid, categoryid, authorid, booklink FROM books WHERE bookname = $1',
            [bookname]
        );

        if (result.rows.length === 0) {
            return res.status(404).json({ error: 'User not found' });
        }

        res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.deleteBook = async (req, res) => 
    {
        const {bookID} = req.body;
        try
        {
            const result = await pool.query('DELETE FROM books WHERE bookID = $1', [bookID]);
            res.sendStatus(204); // No Content
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
    }

 exports.updateBook = async (req, res) => 
    {
        const {userID, username, login, password, role} = req.body;
        try
        {
            const result = await pool.query('Update books SET bookname = $1, imagelink=$2, rateid=$3, categoryid = $4, authorid = $5, booklink = $6 WHERE "bookID" = $5',[bookname, imagelink, rateid, categoryid, authorid, booklink]);
        res.status(200).json(result.rows[0]); // Всегда используй json()
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
    }