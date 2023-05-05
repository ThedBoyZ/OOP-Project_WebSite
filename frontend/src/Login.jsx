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
      console.log(res.data['login_status']);
      if(res.data["login_status"]=="complete")
      {
        navigate("/")
      }
      else if(res.data['login_status']=='root')
      {
        navigate('/admin_page')
        alert("ADMIN")
      }
      else
      {
        return alert("wrong username or password")
      }
    })
    
  }

  const toRegister = () => {
    navigate('/Register')
  }

  return (
    <>
      <h1>login page</h1>
      <div>
        <form>
          <label>Email</label><br/>
          <input type="text" onChange={(e) => setEmail(e.target.value)} /><br/>
          <label>Password</label><br/>
          <input type="password" onChange={(e) => setPassword(e.target.value)} /><br/>
          <button type="submit" onClick={login}>Login</button>
          <p>Didn't have account yet?</p>
          <button type="button" onClick={toRegister}>Register</button>
        </form>
      </div>
    </>
  );
}
