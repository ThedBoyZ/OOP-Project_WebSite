import { useNavigate } from "react-router";
import axios from "axios";
import { useState } from "react";
import { selected_value } from "./show_flight";

export default function Checkout() {
  const navigate = useNavigate();
  const [airline, setAirline] = useState("");

  const test = () =>{
    console.log(selected_value['data'])
  }
  

  const checkout = (event) => {
    event.preventDefault(); // prevent form submission behavior
    
    axios.post("http://127.0.0.1:8000/add_flight", {
      
        
    
    })
    .then(res => {
      console.log(res.data);
      
    })
    
  }
  return (
    <>
      <h1>Checkout</h1>
      {test()}
        
      
        
    </>
  );
}

