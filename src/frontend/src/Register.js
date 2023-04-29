import { useNavigate } from "react-router";
import axios from "axios";
import { useState } from "react";

export default function Register() {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm_password, setConfirm_password] = useState("");
  const [country, setCountry] = useState("")

  const register = (event) => {
    event.preventDefault(); // prevent form submission behavior
    if(password===confirm_password){
      axios.post("http://127.0.0.1:8000/register", {
        
        name:`${name}`,
        surname:`${surname}`,
        email:`${email}`,
        password:`${password}`,
        confirm_password:`${confirm_password}`,
        country:`${country}`
  
      })
      .then(res => {
        console.log(res.data["register_status"]);
        if(res.data["register_status"] === "Register complete"){
          // navigate("/Login")
          return alert("Welcome!!")
        }
        else if(res.data["register_status"] === "Already registered"){
            alert("Sorry but this email was already taken")
        }
        
      })
      .catch(err => {
        console.log(err.response.data);
      })

    }
    else{
      return alert("Password doesn't match")
    }
    
  }

  const login = (event) =>{
    navigate('/login')
  }

  return (
    <>
      <h1>Register page</h1>
      <div>
        <form>
          <label>Sign Up</label><br/>
          <select name="title">
            <option value="Mr">Mr</option>
            <option value="Mrs">Mrs</option>
            <option value="Ms">Ms</option>
          </select><br/>

          <label>Name :</label><br/>
          <input type="text" id="fname" name="fname" placeholder="Firstname" onChange={(e) => setName(e.target.value)}/><br/>

          <label>Surname :</label><br/>
          <input type="text" id="sname" name="sname" placeholder="Surname" onChange={(e) => setSurname(e.target.value)}/><br/>

          <label>Enter your Email:</label><br/>
          <input type="email" id="email" name="email" placeholder="Example@gmail.com" onChange={(e) => setEmail(e.target.value)}/><br/>

          <label>Enter your Password:</label><br/>
          <input type="password" name="password1" placeholder="password" onChange={(e) => setPassword(e.target.value)}/><br/>
          <input type="password" name="password2" placeholder="confirm password" onChange={(e) => setConfirm_password(e.target.value)}/><br/>

          <label>Country</label>
          <input type="text" placeholder="country" onChange={(e) => setCountry(e.target.value)}/><br/>

          <button type="submit" onClick={register}>Proceed</button><br/>

          <label>Already have an account?</label><br/>
          <button type="submit" onClick={login}>Login</button><br/>
        </form>
      </div>
    </>
  );
}
