import { useNavigate } from "react-router";
import axios from "axios";
import { useState } from "react";
import { selected_value } from "./show_flight";

export default function Checkout() {
  const navigate = useNavigate();
  const [jsonItems, setJsonItems] = useState([]);
  
  const show_select = () =>{
    console.log(selected_value['data'])
    const data = []
    for(let i in selected_value['data']){
      data.push(selected_value['data'][i])
    }
   
    const listItems = data.map((d, index) =>
    <ul key={index}>
      {
        <h5>{d}</h5>
      }
    </ul>);
    return listItems
  }

  const checkout = () =>{
    //navigate('./payment')
    console.log('payment')
  }
  

  
  return (
    <>
      {show_select()}
      <button type="button" onClick={() => checkout()}>CHECKOUT</button>
    </>
  );
}

