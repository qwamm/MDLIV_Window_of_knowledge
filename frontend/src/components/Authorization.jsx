import '../App.css'
import {useState} from "react";
import {useNavigate} from "react-router-dom";
export default function Authorization(pros)
{
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [submitted, setSubmitted] = useState(false);
    const navigate = useNavigate()
    // Handling the email change
    const handleLogin = (e) => {
        setLogin(e.target.value);
        setSubmitted(false);
    };

    // Handling the password change
    const handlePassword = (e) => {
        setPassword(e.target.value);
        setSubmitted(false);
    };

    const handleRegistration = (e) => {
        e.preventDefault();
        setSubmitted(true);
        fetch('http://localhost/api/auth/registration', {
            method: 'POST',
            body: JSON.stringify({
                'username' : login,
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
                // Handle data
            })
            .catch((err) => {
                console.log(err.message);
            });
        pros.setUsername(login)
        pros.setPoints(3041)
        navigate('/')
    };

    // Handling the form submission
    const handleSubmit = (e) => {
        e.preventDefault();
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
        setSubmitted(true);
    };
    return (
        <div className="auth">
            <h2 style = {{position : "absolute", left: "25px", bottom : "160px"}}>Авторизация</h2>
            <form className="form">
                <input className="form" type="text" placeholder="Логин" onChange={handleLogin} id="login"/>
                <input className="form" type="text" placeholder="Пароль" onChange={handlePassword} id="password"/>
                <button type="submit" className="submit" onClick={handleSubmit}>
                    Submit
                </button>
                <button type="submit" className="submit" onClick={handleRegistration}>
                    Registration
                </button>
            </form>
        </div>
    )
}