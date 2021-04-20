import React from "react";
import "./app.css";
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom";
import Home from "../home/home";
import Equipment from "../equipment/equipment";
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/equipment" component={Equipment} />
        <Redirect to="/" />
      </Switch>
    </Router>
  );
}

export default App;