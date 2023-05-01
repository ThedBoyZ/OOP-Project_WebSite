import { useNavigate } from "react-router";
import axios from "axios";
import { useState } from "react";
import { Link } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();
  const [airpaz_code, setAirpazCode] = useState("");
  

  const login = (event) => {
    event.preventDefault(); // prevent form submission behavior
    
    axios.post("http://127.0.0.1:8000/***", {
      
    
    })
    .then(res => {
      
    })
    
  }
  return (
    <>
      <h1>Payment</h1>

      <h2>Payment Methods</h2>

      <a href="payment/promptpay">Promptpay</a><br/>
      <a href="payment/visa">VISA</a><br/>
      <a href="payment/paypal">PayPal</a><br/>
 
    </>
  );
}
