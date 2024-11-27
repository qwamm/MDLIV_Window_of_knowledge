import {lazy, Suspense, useState} from "react";
import { Route, BrowserRouter, Routes } from "react-router-dom";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Home from "../pages/Home";
import Authorization from "../pages/Authorization";
import { Styles } from "../styles/styles";
import Registration from "../pages/Registration";
import Chats from "../pages/Chats";

export default function Router() {
    const [login, setLogin] = useState("")
    const [submit, setSubmitted] = useState("")
    const [password, setPassword] = useState("")

  return (
      <Routes>
            <Route path ="/" element = {
                <Suspense fallback={null}>
                <Styles />
                <Header />
                <Home/>
                <Footer />
                </Suspense>
            }
            ></Route>
          <Route path = '/login' element = {<Authorization setLogin = {setLogin} setSubmitted = {setSubmitted} setPassword = {setPassword}/>}></Route>
          <Route path = '/register' element = {<Registration setLogin = {setLogin} setSubmitted = {setSubmitted} setPassword = {setPassword}/>}></Route>
          <Route path = "/chats" element = {<Chats/>}> </Route>
      </Routes>
  );
};

