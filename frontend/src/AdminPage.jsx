import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";



const Admin_page = () => {
    const [authenticated, setAuthenticated] = useState(false);
    const navigate = useNavigate()

    const [airline, setAirline] = useState('')
    const [day, setDay] = useState('')
    const [departure_airport, setDepartureAirport] = useState('')
    const [departure_day, setDepartureDay] = useState('')
    const [departure_time, setDepartureTime] = useState('')
    const [arrival_airport, setArrivalAirport] = useState('')
    const [arrival_day, setArrivalDay] = useState('')
    const [arrival_time, setArrivalTime] = useState('')
    const [baggage, setBaggage] = useState('')
    const [refund, setRefund] = useState('')
    const [reschedule, setReschedule] = useState('')
    const [id, setId] = useState('')
    const [status, setStatus] = useState('')


    const add_flight = () => {
        axios.post("http://127.0.0.1:8000/add_flight", {
            
            "airline": airline,
            "day": day,
            "departure_airport": departure_airport,
            "departure_day": departure_day,
            "departure_time": departure_time,
            "arrival_airport": arrival_airport,
            "arrival_day": arrival_day,
            "arrival_time": arrival_time,
            "baggage": baggage,
            "refund": refund,
            "reschedule": reschedule,
            "id": id,
            "status": status
            
        })
        .then(res=>{
            console.log(res.data)
        })
    }


    useEffect(() => {
      axios.get("http://127.0.0.1:8000/current_status")
        .then(res => {
            console.log(res.data)
            if(res.data['status'] === 'root'){
                alert('Welcome ADMIN')
            }
            else{
                navigate('/')
                alert("You don't have permission on this site")
            }
        })
        .catch(err => console.error(err));
    }, []);

    return (
        <div>
            <h1>Admin Page</h1>
            <form>
                <label>Add flight</label>
                <input type="text" onChange={(e)=>setAirline(e.target.value)} placeholder="Airline"/>
                <input type="text" onChange={(e)=>setDay(e.target.value)}  placeholder="Day"/>
                <input type="text" onChange={(e)=>setDepartureAirport(e.target.value)}  placeholder="DepartureAirport"/>
                <input type="text" onChange={(e)=>setDepartureDay(e.target.value)}  placeholder="DepartureDay"/>
                <input type="text" onChange={(e)=>setDepartureTime(e.target.value)} placeholder="DepartureTime"/>
                <input type="text" onChange={(e)=>setArrivalAirport(e.target.value)} placeholder="ArrivalAirport"/>
                <input type="text" onChange={(e)=>setArrivalDay(e.target.value)} placeholder="ArrivalDay"/>
                <input type="text" onChange={(e)=>setArrivalTime(e.target.value)} placeholder="ArrivalTime"/>
                <input type="text" onChange={(e)=>setBaggage(e.target.value)} placeholder="Baggage"/>
                <input type="text" onChange={(e)=>setRefund(e.target.value)} placeholder="Refund"/>
                <input type="text" onChange={(e)=>setReschedule(e.target.value)} placeholder="Reschedule"/>
                <input type="text" onChange={(e)=>setId(e.target.value)} placeholder="Id"/>
                <input type="text" onChange={(e)=>setStatus(e.target.value)} placeholder="Status"/>

                <button type="button" onClick={()=>add_flight()}>Submit</button>
            </form>
        </div>
    );
}

export default Admin_page;
