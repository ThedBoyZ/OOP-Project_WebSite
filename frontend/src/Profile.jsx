import { useNavigate } from "react-router-dom";
import { useState,React } from "react";
import axios from "axios";

export default function Profile() {
    axios.get('http://127.0.0.1:8000/see_profile')
    .then(res => {
      let respond = res.data['profile']
      console.log('email : ',respond['email'])
      console.log('name : ',respond['name'])
      console.log('surname :',respond['surname'])
    })
    return (
      <>
        <h1>Profile page</h1>
      </>
    );
  }