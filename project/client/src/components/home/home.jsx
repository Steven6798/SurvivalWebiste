import React from 'react';
import "./home.css";
import NavBar from "../navigationBar/navigationBar";
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import CBRN from "../../images/home_CBRN.jpg"
import NaturalDisaster from "../../images/home_natural_disaster.jpg"
import Pandemic from "../../images/home_pandemic.jpg"
import Crash from "../../images/home_crash.jpg"
import Riot from "../../images/home_riot.jpg"
import Fire from "../../images/home_fire.jpg"
import ActiveShooting from "../../images/home_active_shooting.jpg"
import Supplychain from "../../images/home_supplychain.jpg"
import Invasion from "../../images/home_invasion.jpg"
import TerroristAttack from "../../images/home_terrorist_attack.jpg"
import WorldWar from "../../images/home_world_war.jpg"
import Extinction from "../../images/home_extinction.jpg"

class Home extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div className="TitleDiv">
          <NavBar />
          <Container fluid>
            <Row>
              <Col>
                <h1 className="Title">Be prepared</h1>
              </Col>
            </Row>
            <Row>
              <Col>
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
              <Col>
                <h1 className="ScenarioTitle ScenarioPadding">Consider every scenario</h1>
              </Col>
            </Row>
            <Row>
              <Col>
                <Image className="picDim d-block mx-auto" src={CBRN}/>
                <h2 className="ScenarioDescription picPadding">CBRN Disasters</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={NaturalDisaster}/>
                <h2 className="ScenarioDescription picPadding">Natural Disasters</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={Pandemic}/>
                <h2 className="ScenarioDescription picPadding">Pandemics</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={Crash}/>
                <h2 className="ScenarioDescription picPadding">Crashes</h2>
              </Col>
            </Row>
            <Row>
              <Col>
                <Image className="picDim d-block mx-auto" src={Riot}/>
                <h2 className="ScenarioDescription picPadding">Riots</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={Fire}/>
                <h2 className="ScenarioDescription picPadding">Fires</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={ActiveShooting}/>
                <h2 className="ScenarioDescription picPadding">Active Shootings</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={Supplychain}/>
                <h2 className="ScenarioDescription picPadding">Supplychain Interrumptions</h2>
              </Col>
            </Row>
            <Row>
              <Col>
                <Image className="picDim d-block mx-auto" src={Invasion}/>
                <h2 className="ScenarioDescription picPadding">Home Invasions</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={TerroristAttack}/>
                <h2 className="ScenarioDescription picPadding">Terrorist Attacks</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={WorldWar}/>
                <h2 className="ScenarioDescription picPadding">World Wars</h2>
              </Col>
              <Col>
                <Image className="picDim d-block mx-auto" src={Extinction}/>
                <h2 className="ScenarioDescription picPadding">Extinctions</h2>
              </Col>
            </Row>
          </Container>
        </div>
      </React.Fragment>
    );
  }
}

export default Home;