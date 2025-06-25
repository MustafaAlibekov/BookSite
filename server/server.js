const express = require("express");
const userRoutes = require('./routes/userrouter')
const bookRoutes = require('./routes/bookrouter')
const app = express();

app.use(express.json());  // Готов принять JSON


app.use("/api", userRoutes);
app.use("/books", bookRoutes);

app.listen(3000, ()=>
    {
        console.log("server is working");
    });