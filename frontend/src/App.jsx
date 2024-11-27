import { useState } from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Authorization from "./components/Authorization.jsx";
import * as React from 'react'
import {ChakraProvider, defaultConfig} from "@chakra-ui/react";
import {createSystem} from "@chakra-ui/react";
import './App.css'
import MainPage from "./components/MainPage/MainPage.jsx";

const colors = {
    primary: {
        100: "#E5FCF1",
        200: "#27EF96",
        300: "#10DE82",
        400: "#0EBE6F",
        500: "#0CA25F",
        600: "#0A864F",
        700: "#086F42",
        800: "#075C37",
        900: "#064C2E"
    }
};

export default function App() {
    const [username, setUsername] = useState("Авторизация");
    const system = createSystem(defaultConfig);
    return (
        <ChakraProvider value={system}>
            <div>
                <MainPage username={username} setUsername={setUsername}></MainPage>
                <Routes>
                    <Route path="/login" element={<Authorization setUsername={setUsername}></Authorization>}></Route>
                </Routes>
            </div>
        </ChakraProvider>
    )
}
