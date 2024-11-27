import {ChangeEvent, lazy, useState} from "react";
import Input from "../../common/Input";
import {Button} from '../../common/Button'
import {useNavigate} from "react-router-dom"


export default function Authorization(pros: any) {
    const [login, setLogin] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate();

    const handleLogin = (e: any) => {
        setLogin(e.target.value);
        pros.setLogin(e.target.value);
        pros.setSubmitted(false);
    };

    const handlePassword = (e: any) => {
        setPassword(e.target.value);
        pros.setPassword(e.target.value);
        pros.setSubmitted(false);
    };

    const handleSubmit = () => {
        fetch('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify({
                'username' : login,
                'password': password,
                'remember_me': true
            }),
            headers: {
                'Content-type': 'application/json',
                'accept': 'application/json'
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                if (data.message !== "OK")
                {
                    alert("Неверный логин или пароль")
                }
                else {
                    pros.setUsername(login)
                    pros.setPoints(3041)
                    navigate('/')
                }
                // Handle data
            })
            .catch((err) => {
                console.log(err.message);
            });
        pros.setSubmitted(true);
    };

    return (
        <div style={{position:'absolute', top: '30%', left: '45%'}}>
                    <h1>Авторизация</h1>
                    <Input name={""} placeholder={"Введите логин"} onChange={handleLogin}></Input>
                    <Input name={""} placeholder={"Введите пароль"} onChange={handlePassword}></Input>
                    <Button onClick = {handleSubmit}>
                        Войти
                    </Button>
        </div>
    );
}