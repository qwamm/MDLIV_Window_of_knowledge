import axios from "axios";
import { Component , useState} from "react";
import * as React from "react";
import './styles.css'

export default function AdminPanel() {
    const [file, setFile] = useState("");

    const handleFileChange = (e) => {
        if (e.target.files) {
            setFile(e.target.files[0]);
            console.log(e.target.files[0].arrayBuffer())
        }
    };

    const handleUpload = async () => {
        if (file) {
            console.log('Uploading file...');

            const formData = new FormData();
            formData.append('file', file);

            fetch('http://localhost/api/file/addFile', {
                method: 'POST',
                body: '',
                kb_id: 1,
                re: file,
                headers: {
                    'Content-type': 'application/json',
                    'accept': 'application/json'
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data)
                })
                .catch((err) => {
                    console.log(err.message);
                });
        };
    };

    return (
        <>
        <div style = {{position: 'absolute', left: '50%', top: '50%'}}>
            <input id="file" type="file" onChange={handleFileChange} />
        </div>
    {file && (
        <section>
            File details:
            <ul>
                <li>Name: {file.name}</li>
                <li>Type: {file.type}</li>
                <li>Size: {file.size} bytes</li>
            </ul>
        </section>
    )}

    {file && (
        <button
            onClick={handleUpload}
            className="submit"
        >Upload a file</button>
    )}
            </>
    );
}