import {ChangeEvent, lazy, useEffect, useState} from "react";
import Input from "../../common/Input";
import {Button} from '../../common/Button'
import TextArea from "../../common/TextArea"
import {useNavigate} from "react-router-dom"
import { Flex, ChakraProvider } from "@chakra-ui/react";
import { ColorPicker, useColor } from "react-color-palette";
import "react-color-palette/css";

import * as React from "react";

import CustomizationPage from "../../content/CustomizationPage.json";

const Contact = lazy(() => import("../../components/ContactForm"));
const MiddleBlock = lazy(() => import("../../components/MiddleBlock"));
const Container = lazy(() => import("../../common/Container"));
const ScrollToTop = lazy(() => import("../../common/ScrollToTop"));
const ContentBlock = lazy(() => import("../../components/ContentBlock"));

export default function Customization(props: any) {
    return (
      <>
          <Container>
              <MiddleBlock
                  title={CustomizationPage.title}
                  content={CustomizationPage.text} button={""} />
              <ColorPicker hideInput={["rgb", "hsv"]} color={props.color} onChange={props.setColor} />
          </Container>
      </>
    );
}