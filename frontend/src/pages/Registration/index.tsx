import {ChangeEvent, lazy, useState} from "react";
import Input from "../../common/Input";
import {Button} from '../../common/Button'
import {useNavigate} from "react-router-dom"


export default function Registration(pros: any) {
    const [login, setLogin] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate();

    const handleLogin = (e: any) => {
        setLogin(e.target.value);
    };

    const handlePassword = (e: any) => {
        setPassword(e.target.value);
    };

    const handleRegistration = () => {
        fetch('http://localhost/api/auth/register', {
            method: 'POST',
            body: JSON.stringify({
                'user_name' : login,
                'first_name': login,
                'second_name': login,
                'password': password,
                'password_again': password
            }),
            headers: {
                'Content-type': 'application/json',
                'accept': 'application/json'
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            })
            .catch((err) => {
                console.log(err.message);
            });
        navigate('/')
    };


    return (
        <div style={{position:'absolute', top: '30%', left: '45%'}}>
            <h1>Создать новый аккаунт</h1>
            <Input name={""} placeholder={"Введите логин"} onChange={handleLogin}></Input>
            <Input name={""} placeholder={"Введите пароль"} onChange={handlePassword}></Input>
            <Button onClick = {handleRegistration}>
                Регистрация
            </Button>
        </div>
    );
}