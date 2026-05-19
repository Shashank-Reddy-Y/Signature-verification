const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth'); 
const addAccountRoutes = require('./scripts/addacc'); 
require('dotenv').config();

const app = express();

// 1. Dynamic Port Binding (Crucial for Render)
const PORT = process.env.PORT || 5000;

// 2. Strict MongoDB Connection Check
if (!process.env.MONGO_URI) {
    console.error("FATAL ERROR: MONGO_URI is not defined in environment variables.");
    process.exit(1);
}

mongoose.connect(process.env.MONGO_URI)
    .then(() => console.log("MongoDB Connected Successfully"))
    .catch(err => console.log("MongoDB Connection Error: ", err));

// 3. Fixed CORS (Removed the duplicate rule!)
app.use(cors({
  // This uses your Vercel URL if available, otherwise allows all for testing
  origin: process.env.FRONTEND_URL || '*', 
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true
}));

// Middleware for payloads
app.use(express.json({ limit: '10mb' })); 

// Root route for health checks
app.get('/', (req, res) => {
  res.send('Node.js Backend is live!');
});

// API routes
app.use('/api/auth', authRoutes); 
app.use('/api/account', addAccountRoutes); 

// Start the server
app.listen(PORT, () => {
  console.log(`Node.js Server running on port ${PORT}`);
});
