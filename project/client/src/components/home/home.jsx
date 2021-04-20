import React from "react";
import "./home.css";
import NavBar from "../navigationBar/navigationBar";
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import CBRN from "../../images/CBRN.jpg"
import NaturalDisaster from "../../images/NaturalDisaster.jpg"
import Pandemic from "../../images/Pandemic.jpg"
import Crash from "../../images/Crash.jpg"
import Riot from "../../images/Riot.jpg"
import Fire from "../../images/Fire.jpg"
import ActiveShooting from "../../images/ActiveShooting.jpg"
import Supplychain from "../../images/Supplychain.jpg"
import HomeInvasion from "../../images/HomeInvasion.jpg"
import TerroristAttack from "../../images/TerroristAttack.jpg"
import WorldWar from "../../images/WorldWar.jpg"
import Extinction from "../../images/Extinction.jpg"

class Home extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div className="TitleDiv">
          <NavBar />
          <Container fluid>
            <Row>
              <Col className="noPadding">
                <h1 className="Title">Be prepared</h1>
              </Col>
            </Row>
            <Row>
              <Col className="noPadding">
                <h2 className="TitleDescription">It’s not a matter of if a
                disaster will happen, but when. It will be your responsibility
                to protect yourself and your family.</h2>
              </Col>
            </Row>
          </Container>
        </div>
        <div className="ScenarioDiv">
          <Container fluid>
            <Row>
              <Col className="ScenarioPadding">
                <h1 className="ScenarioTitle">Consider every scenario</h1>
              </Col>
            </Row>
            <Row>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={CBRN}/>
                <h2 className="ScenarioDescription">CBRN Disasters</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={NaturalDisaster}/>
                <h2 className="ScenarioDescription">Natural Disasters</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={Pandemic}/>
                <h2 className="ScenarioDescription">Pandemics</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={Crash}/>
                <h2 className="ScenarioDescription">Crashes</h2>
              </Col>
            </Row>
            <Row>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={Riot}/>
                <h2 className="ScenarioDescription">Riots</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={Fire}/>
                <h2 className="ScenarioDescription">Fires</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={ActiveShooting}/>
                <h2 className="ScenarioDescription">Active Shootings</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={Supplychain}/>
                <h2 className="ScenarioDescription">Supplychain Interrumptions</h2>
              </Col>
            </Row>
            <Row>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={HomeInvasion}/>
                <h2 className="ScenarioDescription">Home Invasions</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={TerroristAttack}/>
                <h2 className="ScenarioDescription">Terrorist Attacks</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={WorldWar}/>
                <h2 className="ScenarioDescription">World Wars</h2>
              </Col>
              <Col className="picPadding">
                <Image className="picDim d-block mx-auto" src={Extinction}/>
                <h2 className="ScenarioDescription">Extinctions</h2>
              </Col>
            </Row>
          </Container>
        </div>
      </React.Fragment>
    );
  }
}

export default Home;