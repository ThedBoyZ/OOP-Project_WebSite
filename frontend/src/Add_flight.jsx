import { useNavigate } from "react-router";
import axios from "axios";
import { useState } from "react";

export default function Add_flight() {
  const navigate = useNavigate();
  const [airline, setAirline] = useState("");
  const [day, setDay] = useState("");
  const [departure_airport, setDA] = useState("");
  const [departure_day, setDD] = useState("");
  const [departure_time, setDT] = useState("");
  const [arrival_airport, setAA] = useState("");
  const [arrival_day, setAD] = useState("");
  const [arrival_time, setAT] = useState("");
  const [baggage, setBaggage] = useState("");
  const [refund, setRefund] = useState("");
  const [reschedule, setReschedule] = useState("");
  const [id, setId] = useState("");
  const [status, setStatus] = useState("");

  const add = (event) => {
    event.preventDefault(); // prevent form submission behavior
    
    axios.post("http://127.0.0.1:8000/add_flight", {
      
        airline:`${airline}`,
        day:`${day}`,
        departure_airport:`${departure_airport}`,
        departure_day:`${departure_day}`,
        departure_time:`${departure_time}`,
        arrival_airport:`${arrival_airport}`,
        arrival_day:`${arrival_day}`,
        arrival_time:`${arrival_time}`,
        baggage:`${baggage}`,
        refund:`${refund}`,
        reschedule:`${reschedule}`,
        id:`${id}`,
        status:`${status}`
    
    })
    .then(res => {
      console.log(res.data);
      
    })
    
  }
  return (
    <>
      <h1>Add flight</h1>

      <form>


        <label>Airline Name</label>
        <input onChange={(e) => setAirline(e.target.value)}></input><br/>

        <label>Day</label>
        <input onChange={(e) => setDay(e.target.value)}></input><br/>

        <label>departure_airport</label>
        <input onChange={(e) => setDA(e.target.value)}></input><br/>

        <label>departure_day</label>
        <input onChange={(e) => setDD(e.target.value)}></input><br/>

        <label>departure_time</label>
        <input onChange={(e) => setDT(e.target.value)}></input><br/>

        <label>arrival_airport</label>
        <input onChange={(e) => setAA(e.target.value)}></input><br/>

        <label>arrival_day</label>
        <input onChange={(e) => setAD(e.target.value)}></input><br/>

        <label>arrival_time</label>
        <input onChange={(e) => setAT(e.target.value)}></input><br/>

        <label>baggage</label>
        <input onChange={(e) => setBaggage(e.target.value)}></input><br/>

        <label>refund</label>
        <input onChange={(e) => setRefund(e.target.value)}></input><br/>

        <label>reschedule</label>
        <input onChange={(e) => setReschedule(e.target.value)}></input><br/>

        <label>id</label>
        <input onChange={(e) => setId(e.target.value)}></input><br/>
        
        <label>status</label>
        <input onChange={(e) => setStatus(e.target.value)}></input><br/>

        <button type="button" onClick={add}>Proceed</button>

      </form>
    
        
    </>
  );
}


//     ="2023-05-01",
//     ="12:00 PM",
//     ="Airport B",
//     ="2023-05-01",
//     ="2:00 PM",
//     ="Yes",
//     ="Yes",
//     ="Yes",
//     ="FL001",
//     ="On Time"
