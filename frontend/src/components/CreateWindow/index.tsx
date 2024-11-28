import * as React from "react";
import CustomizationPage from "../../content/CustomizationPage.json";
import {ColorPicker} from "react-color-palette";
import MiddleBlock from "../MiddleBlock";
import {Container} from "../Block/styles";
import Input from "../../common/Input";
import {Button} from "../../common/Button";
import {useState} from "react";
import {useNavigate} from "react-router-dom";

export default function CreateWindow(props: any)
{
    const [name, setName] = useState("")
    const [description, setDescription] = useState("")
    const navigate = useNavigate();

    const handleName = (e: any) => {
        setName(e.target.value);
    };

    const handleDescription = (e: any) => {
        setDescription(e.target.value);
    };

    const handleSubmit = () => {
        fetch('http://localhost/api/knowledge_base/create', {
            method: 'POST',
            body: JSON.stringify({
                'name' : name,
                'description':description
            }),
            headers: {
                'Content-type': 'application/json',
                'accept': 'application/json'
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                navigate('/')
            })
            .catch((err) => {
                console.log(err.message);
            });
    };
    return (
        <>
            <div style={{position: 'absolute', top: '30%', left: '45%'}}>
                <h1>Создание окна знаний</h1>
                <Input name={""} placeholder={"Введите название"} onChange={handleName}></Input>
                <Input name={""} placeholder={"Краткое описание"} onChange={handleDescription}></Input>
                <Button onClick={handleSubmit}>
                    Войти
                </Button>
            </div>
        </>
    );
}