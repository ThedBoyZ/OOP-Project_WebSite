import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from "react";
import { id } from "./Payment";


export default function Paypal(){
    const navigate = useNavigate();
    const [data, setData] = useState(null);

    useEffect(() => {
    axios
        .get(`http://127.0.0.1:8000/paypal/${id}`)
        .then((res) => {
            setData(res.data);
        })
        .catch((error) => {
            console.log(error);
        });
    }, []);

    const payment_complete = () =>{
        axios
        .get(`http://127.0.0.1:8000/payment_complete/${id}`)
        .then(() => {
            navigate('/')
            return alert("Payment Complete")
        });
    }

    return(
        <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
            <h1 className="mb-3">Paypal Method</h1>
            {data && (
            <div className="bg-light rounded mb-3">
                <label>Price: {String(data["Price"])}</label><br />
                <label>Processing Fee: {String(data["Processing Fee"])}</label><br />
                <span style={{ fontWeight: 'bold' }}>Total Price: {String(data["Total_Price"])}</span><br />
            </div>
            )}
            <button className="bg-light rounded mb-2" type="button" onClick={() => payment_complete()}>Pay!</button><br />
        </div>
    )
}