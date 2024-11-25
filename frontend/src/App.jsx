import { useState } from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Authorization from "./components/Authorization.jsx";
import * as React from 'react'
import './App.css'
import MainPage from "./components/MainPage/MainPage.jsx";

export default function App() {
    const [username, setUsername] = useState("Авторизация");
    return (
        <div>
            <MainPage username = {username} setUsername = {setUsername}></MainPage>
            <Routes>
                <Route path = "/login" element = {<Authorization setUsername = {setUsername}></Authorization>}></Route>
            </Routes>
        </div>
    )
}
