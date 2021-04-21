import React from "react";
import "./navigationBar.css";
import { Link } from "react-router-dom";

function navigationBar() {
    return (
        <div className="nav">
          <ul>
            <Link to="/" className="navButton">
              <li className="navButton">Home</li>
            </Link>
            
            <Link to="/product" className="navButton">
              <li className="navButton">Products</li>
            </Link>
    
            <Link to="/login" className="navButton">
              <li className="navButton">Log In</li>
            </Link>
          </ul>
        </div>
      );
}

export default navigationBar;