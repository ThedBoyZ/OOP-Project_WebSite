import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";

export default function Internet_banking(){
    const [price, setPrice] = useState("")
    const [fee, setFee] = useState("")
    const [totalPrice, setTotalPrice] = useState("")

    const show_price = (event) =>{
        event.preventDefault();

        axios.post("http://127.0.0.1:8000/internet_banking", {
            // booking_id:`${booking_id}`,
            // bank_name:`${bank_name}`,
            // account_number:`${account_number}`
        })
        axios.post("http://127.0.0.1:8000/credit_card", {
            // booking_id:`${booking_id}`,
            // card_number:`${card_number}`,
            // card_holder_name:`${card_holder_name}`
            // expiry_date:`${expiry_date}`
            // cvv:`${cvv}`
        })
        axios.post("http://127.0.0.1:8000/paypal", {
            // booking_id:`${booking_id}`,
            // email:`${email}`,
            // password:`${password}`
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

        </div>
    )
}