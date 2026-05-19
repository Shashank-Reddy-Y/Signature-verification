project-root/
│
├── backend/
│   ├── config/
│   │   └── db.js                # Database connection setup
│   ├── models/
│   │   └── User.js              # User schema for authentication
│   │   └── Signature.js         # Signature schema for verification
│   │   └── Account.js           # Account schema for storing account details and images
│   ├── routes/
│   │   └── auth.js              # Authentication routes (e.g., login, signup)
│   │   └── signature.js         # Signature verification routes
│   │   └── account.js           # Account routes for adding, fetching, and updating accounts
│   ├── controllers/
│   │   └── accountController.js # Controller logic for managing account-related operations
│   ├── middleware/
│   │   └── authMiddleware.js    # Middleware for authentication (e.g., JWT validation)
│   ├── uploads/
│   │   └── sample1.png          # Example images for conversion to Base64
│   ├── server.js                # Entry point for the backend server
│   ├── .env                     # Environment variables (MongoDB URI, JWT secret, etc.)
│   ├── package.json             # Backend dependencies and scripts
│
├── frontend/
│   ├── public/
│   │   └── index.html           # Main HTML file
│   ├── src/
│   │   ├── components/
│   │   │   └── Navbar.js        # Navigation bar
│   │   │   └── Home.js          # Home page
│   │   │   └── Signup.js        # Signup page
│   │   │   └── Login.js         # Login page
│   │   │   └── Verify.js        # Signature verification page
│   │   │   └── About.js         # About Us page
│   │   │   └── AddAccount.js    # Page for displaying accounts (if required in frontend)
│   │   ├── App.js               # Main React app component
│   │   ├── index.js             # Entry point for the React app
│   │   ├── index.css            # CSS styles for the frontend
│   ├── package.json             # Frontend dependencies and scripts
│
└── package.json                 # Shared package.json for managing global dependencies
