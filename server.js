require("dotenv").config();

const express = require("express");
const cors = require("cors");

const OpenAI = require("openai");

const app = express();

app.use(cors());

const client = new OpenAI({

baseURL: "https://openrouter.ai/api/v1",

apiKey: process.env.OPENROUTER_API_KEY

});

app.get("/crop/:name", async (req, res) => {

try {

const crop = req.params.name;

const completion =
await client.chat.completions.create({

model: "openai/gpt-3.5-turbo",

messages: [

{
role: "user",

content: `

Give complete farming guide for ${crop} in India.

Include:
- soil types
- best states
- water needs
- fertilizers
- farming process
- diseases
- timeline
- total cost
- selling price
- net profit

`

}

]

});

res.json({

answer:
completion.choices[0].message.content

});

} catch (error) {

console.log(error);

res.json({

answer: error.message

});

}

});

const PORT =
process.env.PORT || 5000;

app.listen(PORT, () => {

console.log(

`Server Running On Port ${PORT}`

);

});