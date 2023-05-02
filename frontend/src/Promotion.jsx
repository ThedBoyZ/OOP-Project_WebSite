import { useNavigate } from "react-router-dom";
import { useState,React } from "react";
import axios from "axios";

var respond = []

export default function Promotion() {

    const show_coupon = () => {
        axios.get("http://127.0.0.1:8000/coupon_home")
        .then(res =>{
          respond = res.data['Data']['_coupon_detail']
          console.log(respond.length)
        })
    }

    const list_coupon = () =>{
      for(let i=0; i < respond.length; i++){
        console.log(respond[i])
        console.log('p')
      }
      const data = []
      for(let i in respond){
        data.push(respond[i])
      }
    
      const listItems = data.map((d, index) =>
      <ul key={index}>
        {
          <h5>{d}</h5>
        }
      </ul>);
      return listItems
    }

    return (
      <>
        <h1>Promotion page</h1>
        {show_coupon()}
        {list_coupon()}
      </>
    );
  }