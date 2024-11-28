import { useState } from "react";
import { Row, Col, Drawer } from "antd";
import { withTranslation, TFunction } from "react-i18next";
import Container from "../../common/Container";
import { SvgIcon } from "../../common/SvgIcon";
import { Button } from "../../common/Button";
import {useNavigate} from "react-router-dom";
import {
  HeaderSection,
  LogoContainer,
  Burger,
  NotHidden,
  Menu,
  CustomNavLinkSmall,
  Label,
  Outline,
  Span,
} from "./styles";

export default function  Header (props: any) {
  const [visible, setVisibility] = useState(false);
  const navigate = useNavigate()
  const toggleButton = () => {
    setVisibility(!visible);
  };

  const MenuItem = (props: any) => {
    const scrollTo = (id: string) => {
      const element = document.getElementById(id) as HTMLDivElement;
      element.scrollIntoView({
        behavior: "smooth",
      });
      setVisibility(false);
    };

    const handleLogout = () => {
      fetch('http://localhost/api/auth/logout', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
          'accept': 'application/json'
        },
      })
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
            // Handle data
          })
          .catch((err) => {
            console.log(err.message);
          });
      props.setSubmitted(false)
      navigate('/')
    };

    return (
      <>
        <CustomNavLinkSmall onClick={() => navigate('/')}>
          <Span>{"Главная"}</Span>
        </CustomNavLinkSmall>
        <CustomNavLinkSmall onClick={() => navigate('/customization')}>
          <Span>{"Кастомизация"}</Span>
        </CustomNavLinkSmall>
        <CustomNavLinkSmall onClick={() => scrollTo("product")}>
          <Span>{"Панель администратора"}</Span>
        </CustomNavLinkSmall>
        {
          props.submitted ? <>
            <CustomNavLinkSmall
                style={{ width: "100px" }}
                onClick={() => navigate('/login')}
            >
              <Span>
                <Button>{"Профиль"}</Button>
              </Span>
            </CustomNavLinkSmall>
            <CustomNavLinkSmall
            style={{ width: "120px" }}
            onClick={() => {props.setSubmitted(false); navigate('/')}}
          >
          <Span>
            <Button>{"Выйти"}</Button>
          </Span>
          </CustomNavLinkSmall>
            </> : <>
            <CustomNavLinkSmall
                style={{ width: "100px" }}
                onClick={() => navigate('/login')}
            >
              <Span>
                <Button>{"Войти"}</Button>
              </Span>
            </CustomNavLinkSmall>
            <CustomNavLinkSmall
                style={{ width: "120px" }}
                onClick={() => navigate('/register')}
            >
              <Span>
                <Button>{"Регистрация"}</Button>
              </Span>
            </CustomNavLinkSmall>
          </>
        }
      </>
    );
  };

  return (
    <HeaderSection>
      <Container>
        <Row justify="space-between">
          <LogoContainer to="/" aria-label="homepage">
            <SvgIcon src="2.svg" width="120px" height="84px" />
          </LogoContainer>
          <NotHidden>
            <MenuItem submitted = {props.submitted} setSubmitted = {props.setSubmitted} />
          </NotHidden>
          <Burger onClick={toggleButton}>
            <Outline />
          </Burger>
        </Row>
        <Drawer closable={false} open={visible} onClose={toggleButton}>
          <Col style={{ marginBottom: "2.5rem" }}>
            <Label onClick={toggleButton}>
              <Col span={12}>
                <Menu>Menu</Menu>
              </Col>
              <Col span={12}>
                <Outline />
              </Col>
            </Label>
          </Col>
          <MenuItem />
        </Drawer>
      </Container>
    </HeaderSection>
  );
};
