import {React, useEffect, useState} from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
export {respond_data}

var respond_data = []

export default function Homepage() {
    const navigate = useNavigate();
    const [day, setDay] = useState("monday")
    const [from, setFrom] = useState("")
    const [to, setTo] = useState("")

    const search = (event) => {
        event.preventDefault();
        
        
        axios.post("http://127.0.0.1:8000/search_flight", {
            travelday:`${day}`,
            depart:`${from}`,
            arrival:`${to}`,
        })
        .then(res => {
            //const data = res.data
            let data = res.data
            respond_data = data["respond"]
            
            
            navigate('/show_flight')
          })

    }

    return (
        <div>
            <h1>Homepage</h1>
            <a href="/">Airpaz</a>
            
            <a href="/login">Sign in</a>
            <a href="/profile">Profile</a>
            <a href="/promotion">Promotion</a>
            <a href="/order">Order</a>
            <a href="/payment">Payment</a>
            
            <form>
                <fieldset>
                    <legend>Search flight</legend>
                    <label>Day</label>
                    <select id="day" onChange={(e) => setDay(e.target.value)}>
                        <option value="Monday">Monday</option>
                        <option value="Tuesday">Tuesday</option>
                        <option value="Wednesday">Wednesday</option>
                        <option value="Thursday">Thursday</option>
                        <option value="Friday">Friday</option>
                        <option value="Saturday">Saturday</option>
                        <option value="Sunday">Sunday</option>
                    </select>

                    <input type="text" id="from" placeholder="From" onChange={(e) => setFrom(e.target.value)}/>
                    <label>To</label>
                    <input type="text" id="to" placeholder="To" onChange={(e) => setTo(e.target.value)}/>

                    <input type="submit" onClick={search}/>
                </fieldset>
            </form>
        </div>

        
    )
    

}
