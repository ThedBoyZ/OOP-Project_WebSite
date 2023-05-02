import {React, useState, useEffect} from "react";
import axios from "axios";

var data = [];
export default function Order(){
    const [airpaz_code, setAirpazCode] = useState("");
    const [data, setData] = useState(null);

    const search = () =>{
        axios.get(`http://127.0.0.1:8000/orders/${airpaz_code}`)
        .then(res => {
            console.log(res.data)
            setData(res.data["booking_details"]);
        })
    }

    return(
        <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
            <h1 className="card text-white bg-danger mb-3" styleName="max-width: 20rem;">Order</h1>
            <div>
                <form>
                    <input type="text" placeholder="Airpaz Code" onChange={(e)=>setAirpazCode(e.target.value)}></input>
                    <button type="button" onClick={() => search()}>Search</button>
                </form><br />
            </div>
            
            <div>
                {data && (
                <div className="bg-light rounded mb-5">
                    <label>Booking Status: {data["status"]}</label><br />
                    <h2>Flight Details</h2>
                    <div className="bg-light rounded mb-5">
                        <label>Flight ID: {data["trip_detail"]['flight_id']}</label><br />
                        <label>Airline: {data["trip_detail"]['airline_name']}</label><br />
                        <label>Day: {data["trip_detail"]['day']}</label><br />
                        <label>Departure Time: {data["trip_detail"]['departure_time']}</label><br />
                        <label>Departure Airport: {data["trip_detail"]['departure_airport']}</label><br />
                        <label>Arrival Time: {data["trip_detail"]['arrival_time']}</label><br />
                        <label>Arrival Airport: {data["trip_detail"]['arrival_airport']}</label><br />
                        <label>Cabin Baggage: {data["trip_detail"]['cabin_baggage']} kg</label><br />
                        <label>Reschedule: {String(data["trip_detail"]['reschedule'])}</label><br />
                        <label>Refund: {String(data["trip_detail"]['refund'])}</label><br /> 
                    </div>
                    <h2>Contact Details</h2>
                    <div className="bg-light rounded mb-5">
                        <label>Name: {data["contact_info"]['name']}</label><br />
                        <label>Surname: {data["contact_info"]['surname']}</label><br />
                        <label>Email: {data["contact_info"]['email']}</label><br />
                    </div>
                </div>
                )}
            </div>
        </div>
    )
}