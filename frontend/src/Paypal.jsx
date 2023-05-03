import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from "react";
import { airpaz_code } from "./Booking_page";


var respond_price = "";
var respond_fee = "";
var respond_total = "";

export default function Promptpay(){
    const navigate = useNavigate()

    const [html, setHtml] = useState("")

    const show_price = () =>{
        
        

        axios.post("http://127.0.0.1:8000/paypal", {
            id:`${airpaz_code['airpaz_code']}`
            
        })
        .then(res => {
            respond_price = res.data['Price']
            respond_fee = res.data['Processing Fee']
            respond_total = res.data['Total_Price']
            
        })
    }

    const payment_complete = () =>{
        navigate('/')
        return alert("Payment Complete")
    }

    useEffect(() => {
        setHtml(`
        Price :
        ${String(respond_price)}
        Proessing Fee :
        ${String(respond_fee)}
        Total_price : 
        ${String(respond_total)}
        
        `)
    }, [html])
    return(
        <div>
             <h1>Paypal Method</h1>
            {show_price()}
            {html}<br/>
            <button type="button" onClick={() => payment_complete()}>Pay!</button>
        </div>
    )
}