const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.get("/", (req, res) => res.render("form"));

app.post("/submit", async (req, res) => {
  try {
    const response = await axios.post("http://backend:5000/submit", req.body);
    res.send(`Backend Response: ${response.data.message}`);
  } catch (err) {
    res.send("Error: " + err.message);
  }
});

app.listen(3000, () => console.log("Frontend running on port 3000"));
