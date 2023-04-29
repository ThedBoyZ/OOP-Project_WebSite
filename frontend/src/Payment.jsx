import { useNavigate } from "react-router";
import axios from "axios";
import { useState } from "react";

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = (event) => {
    event.preventDefault(); // prevent form submission behavior
    
    axios.post("http://127.0.0.1:8000/login", {
      
        email:`${email}`,
        password:`${password}`
    
    })
    .then(res => {
      console.log(res.data);
      if(res.data["login_status"]==="complete")
      {
        navigate("./Profile")
      }
      else
      {
        return alert("wrong username or password")
      }
    })
    
  }
  return (
    <>
      <h1>Payment</h1>

      <h2>Payment Methods</h2>
    </>
  );
}
