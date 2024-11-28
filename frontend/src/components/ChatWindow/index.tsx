import React, {Component, useEffect} from 'react'
import {addResponseMessage, setQuickButtons, Widget} from "react-chat-widget";
import './styles.css';

const buttons = [{label: 'first', value: '1'}, {label: 'second', value: '2'}];

let color = "#1b17d8"

export default function ChatWindow(props: any) {

    useEffect(() => {
        console.log(props.color)
        addResponseMessage('Welcome to this awesome chat!');
    }, []);

    const handleNewUserMessage = (newMessage: any) => {
        console.log(`New message incoming! ${newMessage}`);
        console.log(props.color)
        color = props.color
        // Now send the message through the backend API
        addResponseMessage("OK");
    };

   const  handleQuickButtonClicked = (data:any) => {
        console.log(data);
        setQuickButtons(buttons.filter(button => button.value !== data));
    };
    var resizableProps = {heightOffset:105, widthOffset:35}

    var emojis: Boolean = true

    return (
      <>
          <Widget
              handleNewUserMessage={handleNewUserMessage}
              handleQuickButtonClicked={handleQuickButtonClicked}
              title="Ассистент"
              subtitle="MDLIV Chads GPT"
              resizableProps = {resizableProps}
              emojis = {emojis}
              style = {{'--color' : `${props.color}`}}
          />
      </>
    );
}