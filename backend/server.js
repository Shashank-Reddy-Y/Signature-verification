const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth'); // Import auth routes
const addAccountRoutes = require('./scripts/addacc'); // Import add-account routes
require('dotenv').config();
const app = express();

mongoose.connect(process.env.MONGO_URI)
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

// Enable CORS for requests from the frontend
app.use(cors({
  origin: 'http://localhost:3000', // Allow frontend on port 3000
}));

app.use(cors());

// Middleware to parse JSON requests and handle large payloads
app.use(express.json({ limit: '10mb' })); // Allow large payloads for Base64 images

// Define the root route for handling requests to '/'
app.get('/', (req, res) => {
  res.send('Welcome to the backend server!');
});

// Define the API routes
app.use('/api/auth', authRoutes); // Mount auth routes on /api/auth path
app.use('/api/account', addAccountRoutes); // Mount add-account routes on /api/account path

// Start the server
app.listen(process.env.PORT, () => {
  console.log('Server running on port 5000');
});