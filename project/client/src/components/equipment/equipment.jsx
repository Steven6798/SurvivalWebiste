import React from 'react';
import "./equipment.css";
import NavBar from "../navigationBar/navigationBar";
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import SigSauer220R45LEGION from "../../images/Sig-Sauer-220R-45-LEGION.jpg"
import SigSauerP365XROMEOZERO from "../../images/Sig-Sauer-P365X-ROMEOZERO.jpg"

const API = 'http://127.0.0.1:5000/';
const DEFAULT_QUERY = 'SurvivalApp/get/product';

class Equipment extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      result: []
    };
  }

  componentDidMount() {
    fetch(API + DEFAULT_QUERY)
      .then(response => response.json())
      .then(data => this.setState({result: data}));
  }

  render() {
    const {result} = this.state;
    const nameList = result.map(d => <h2 className="EquipmentProductDescription">{d.product_name}</h2>)
    const priceList = result.map(d => <h2 className="EquipmentProductDescription">${d.product_price}</h2>)
    return (
      <React.Fragment>
        <div className="EquipmentTitleDiv">
          <NavBar />
          <Container fluid>
            <Row>
              <Col className="equipmentnoPadding">
                <h1 className="EquipmentTitle">Equipment</h1>
              </Col>
            </Row>
            <Row>
              <Col className="equipmentnoPadding">
                <h2 className="EquipmentTitleDescription">We offer the best products in
                the market. Each item has been tested by our experts and will
                help survive when the time comes.</h2>
              </Col>
            </Row>
          </Container>
        </div>
        <div className="EquipmentProductDiv">
          <Container fluid className="equipmentnoPadding">
            <Row>
              <Col xs="3" className="equipmentnoPadding">
              </Col>
              <Col className="equipmentnoPadding">
                <Row className="equipmentnoPadding equipmentGridLines">
                  <Col xs="3" className="equipmentnoPadding">
                    <Image className="picDim d-block" src={SigSauer220R45LEGION}/>
                  </Col>
                  <Col className="equipmentnoPadding">
                    <Row className="equipmentnoPadding equipmentPaddingTop">
                      <h2 className="EquipmentProductDescription">{nameList[0]}</h2>
                    </Row>
                    <Row className="equipmentnoPadding">
                      <h2 className="EquipmentProductDescription">Stars</h2>
                    </Row>
                    <Row className="equipmentnoPadding">
                      <h2 className="EquipmentProductDescription">{priceList[0]}</h2>
                    </Row>
                  </Col>
                </Row>
                <Row className="equipmentnoPadding equipmentGridLines">
                  <Col xs="3" className="equipmentnoPadding">
                    <Image className="picDim d-block" src={SigSauerP365XROMEOZERO}/>
                  </Col>
                  <Col className="equipmentnoPadding">
                    <Row className="equipmentnoPadding equipmentPaddingTop">
                      <h2 className="EquipmentProductDescription">{nameList[1]}</h2>
                    </Row>
                    <Row className="equipmentnoPadding">
                      <h2 className="EquipmentProductDescription">Stars</h2>
                    </Row>
                    <Row className="equipmentnoPadding">
                      <h2 className="EquipmentProductDescription">{priceList[1]}</h2>
                    </Row>
                  </Col>
                </Row>
              </Col>
            </Row>
          </Container>
        </div>
      </React.Fragment>
    );
  }
}

export default Equipment;