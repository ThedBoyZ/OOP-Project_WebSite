import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from "react";
<<<<<<< HEAD
import { id } from "./Payment";


export default function Promptpay(){
    const navigate = useNavigate();
    const [data, setData] = useState(null);

    useEffect(() => {
        axios
        .get(`http://127.0.0.1:8000/promptpay/${id}`)
        .then(res => {
            setData(res.data);
=======
import { airpaz_code } from "./Booking_page";


var respond_price = "";
var respond_fee = "";
var respond_total = "";

export default function Promptpay(){
    const navigate = useNavigate()

    const [html, setHtml] = useState("")

    const show_price = () =>{
        

        axios.post("http://127.0.0.1:8000/promptpay", {
            id:`${airpaz_code['airpaz_code']}`
            
        })
        .then(res => {
            respond_price = res.data['Price']
            respond_fee = res.data['Processing Fee']
            respond_total = res.data['Total_Price']
>>>>>>> 8498a5a911db5c7ea3dc3dc89a42f1abb09f7bc1
        })
        .catch((error) => {
        console.log(error); 
        });
    }, []);

    const payment_complete = () =>{
        navigate('/')
        return alert("Payment Complete")
    }

    return(
        <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
            <h1 className="mb-3">Promptpay Method</h1>
            <div className="bg-light rounded mb-3">
                <label>Price: {String(data["Price"])}</label><br />
                <label>Processing Fee: {String(data["Processing Fee"])}</label><br />
                <span style={{ fontWeight: 'bold' }}>Total Price: {String(data["Total_Price"])}</span><br />
            </div>
            <button className="bg-light rounded mb-2" type="button" onClick={() => payment_complete()}>Pay!</button><br />
        </div>
    )
}