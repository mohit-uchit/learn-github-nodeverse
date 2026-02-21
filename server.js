const express = require("express")
const port = 3000

const app = express()

app.get("/", (req,res) => {
    res.send("this is get process")
})

app.listen(port, () => {
    console.log(`this server is running on ${port} http://localhost:${port}`)
})