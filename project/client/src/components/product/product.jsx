import React from 'react';
import "./product.css";
import NavBar from "../navigationBar/navigationBar";
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import SigSauer220R45LEGION from "../../images/Sig_Sauer_220R_45_LEGION.jpg"
import SigSauerP365XROMEOZERO from "../../images/Sig_Sauer_P365X_ROMEOZERO.jpg"

const API = 'https://survivalwebsite.herokuapp.com/';
const DEFAULT_QUERY = 'SurvivalApp/get/product';

class Product extends React.Component {
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
    const nameList = result.map(d => <h2 className="productProductDiv productPaddingTop">{d.product_name}</h2>)
    const priceList = result.map(d => <h2 className="productProductDiv">${d.product_price}</h2>)
    return (
      <React.Fragment>
        <div className="productTitleDiv">
          <NavBar />
          <Container fluid>
            <Row>
              <Col>
                <h1 className="productTitle">Products</h1>
              </Col>
            </Row>
            <Row>
              <Col>
                <h2 className="productTitleDescription">We offer the best products in
                the market. Each item has been tested by our experts and will
                help survive when the time comes.</h2>
              </Col>
            </Row>
          </Container>
        </div>
        <div className="productProductDiv">
          <Container fluid className="noPaddingMargin">
            <Row>
              <Col xs="3" className="noPaddingMargin">
              </Col>
              <Col>
                <Row className="productGridLines">
                  <Col xs="3" className="noPaddingMargin">
                    <Image className="picDim d-block" src={SigSauer220R45LEGION}/>
                  </Col>
                  <Col>
                    <Row>
                      <a href="">{nameList[0]}</a>
                    </Row>
                    <Row>
                      <h2 className="productProductDiv">Stars</h2>
                    </Row>
                    <Row>
                      <h2>{priceList[0]}</h2>
                    </Row>
                  </Col>
                </Row>
                <Row className="productGridLines">
                  <Col xs="3" className="noPaddingMargin">
                    <Image className="picDim d-block" src={SigSauerP365XROMEOZERO}/>
                  </Col>
                  <Col>
                    <Row>
                      <a href="">{nameList[1]}</a>
                    </Row>
                    <Row>
                      <h2 className="productProductDiv">Stars</h2>
                    </Row>
                    <Row>
                      <h2>{priceList[1]}</h2>
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

export default Product;