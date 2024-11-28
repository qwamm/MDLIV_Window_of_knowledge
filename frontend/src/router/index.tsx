import { Suspense, useState} from "react";
import { Route, Routes } from "react-router-dom";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Home from "../pages/Home";
import Authorization from "../pages/Authorization";
import { Styles } from "../styles/styles";
import Registration from "../pages/Registration";
import ChatWindow from "../components/ChatWindow";
import Chats from "../pages/Chats"
import { ColorPicker, useColor } from "react-color-palette";
import Customization from "../pages/Customization";
import AdminPanel from '../pages/AdminPanel'
import CreateWindow from '../components/CreateWindow'

export default function Router() {
    const [login, setLogin] = useState("")
    const [submit, setSubmitted] = useState(false)
    const [password, setPassword] = useState("")
    const [color, setColor] = useColor("#123123");

  return (
      <Routes>
            <Route path ="/" element = {
                <Suspense fallback={null}>
                <Styles />
                <Header submitted = {submit} setSubmitted={setSubmitted} />
                <Home/>
                <Footer />
                    <ChatWindow color={color} setColor={setColor} />
                </Suspense>
            }
            ></Route>
          <Route path = '/login' element = {<Authorization setLogin = {setLogin} setSubmitted = {setSubmitted} setPassword = {setPassword}/>}></Route>
          <Route path = '/register' element = {<Registration setLogin = {setLogin} setSubmitted = {setSubmitted} setPassword = {setPassword}/>}></Route>
          <Route path = "/chats" element = {<Chats/>}></Route>
          <Route path="/customization" element = {
              <Suspense fallback={null}>
              <Styles />
              <Header submitted = {submit} setSubmitted = {setSubmitted} />
                  <Customization color = {color} setColor={setColor}/>
              </Suspense>
          }></Route>
          <Route path = "/panel" element = {<AdminPanel/>}></Route>
          <Route path = "/create_window" element = {<CreateWindow/>}></Route>
      </Routes>
  );
};

