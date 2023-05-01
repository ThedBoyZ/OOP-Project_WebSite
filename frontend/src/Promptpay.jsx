import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";

export default function Promptpay(){
    const [price, setPrice] = useState("")
    const [fee, setFee] = useState("")
    const [totalPrice, setTotalPrice] = useState("")

    const show_price = () =>{
        

        axios.get("http://127.0.0.1:8000/internet_banking", {
            booking_id:5001
            
        })
        .then(res => {
            console.log(res.data)
        })
    }

    return(
        <div>
            <h1>Internet Banking</h1>
            <label>Price:</label><br/>
            <label>Processing Fee:</label><br/>
            <label>Total price:</label><br/>
            {show_price()}
        </div>
    )
}