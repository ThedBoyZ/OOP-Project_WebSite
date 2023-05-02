import './App.css';
import { React, useEffect, useState} from "react";
import axios from "axios";
// import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'
import { selected_value } from './show_flight';

function Traveler({ travelerIndex, travelers, setTravelers }) {

    const [type_person, setType] = useState("")
    const [title, setTitle] = useState("")
    const [gender, setGender] = useState("")
    const [name, setName] = useState("")
    const [surname, setSurname] = useState("")
    const [dob, setDob] = useState("")
    const [nationality, setNationality] = useState("")
    const [baggage_weight, SetBaggage] = useState("")

    useEffect(() => {
        const updatedTravelers = [...travelers];
        updatedTravelers[travelerIndex] = { type_person, title, gender, name, surname, dob, nationality, baggage_weight };
        setTravelers(updatedTravelers);
    }, [type_person, title, gender, name, surname, dob, nationality, baggage_weight, setTravelers]);

    return (
        <div className="bg-light mb-3 rounded">
            <div className="traveler">
                <label>Type</label><br />
                <select className="mb-2" id="type_person" onChange={(e) => setType(e.target.value)}>
                    <option value="Adult">Adult</option>
                    <option value="Child">Child</option>
                    <option value="Infant">Infant</option>
                </select><br />

                <label>Title</label><br />
                <select className="mb-2" id="title" onChange={(e) => setTitle(e.target.value)}>
                    <option value="">None</option>
                    <option value="Mr">Mr</option>
                    <option value="Mrs">Mrs</option>
                    <option value="Ms">Ms</option>
                </select><br />

                <label>Gender</label><br />
                <select className="mb-2" id="gender" onChange={(e) => setGender(e.target.value)}>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                    <option value="">Prefer not to say</option>
                </select><br />

                <label>Name</label><br />
                <input className="mb-2" type="text" placeholder="Name" id="name" onChange={(e) => setName(e.target.value)}></input><br />

                <label>Surname</label><br />
                <input className="mb-2" type="text" placeholder="Surname" id="surname" onChange={(e) => setSurname(e.target.value)}></input><br />
                
                <label>Date of Birth</label><br />
                <input className="mb-2" type="date" id="dob" onChange={(e) => setDob(e.target.value)}></input><br />
                
                <label>Nationality</label><br />
                <select className="mb-2" id="nationality" onChange={(e) => setNationality(e.target.value)}>
                    <option value="Thailand">Thailand</option>
                    <option value="United Kingdom">United Kingdom</option>
                    <option value="United States">United States</option>
                </select><br />
            </div>
            <div className="addons">
                <label>Add ons</label><br />
                <select className="mb-2" id="baggage" onChange={(e) => SetBaggage(e.target.value)}>
                    <option value="0">No Baggage</option>
                    <option value="15">+15kg(฿418)</option>
                    <option value="20">+20kg(฿465)</option>
                    <option value="25">+25kg(฿583)</option>
                    <option value="30">+30kg(฿936)</option>
                    <option value="35">+35kg(฿1,125)</option>
                    <option value="40">+40kg(฿1,407)</option>
                </select><br />
            </div>
        </div>
    );
}

export default function Booking() {
    const [numTravelers, setNumTravelers] = useState(1);
    
    const [title, setTitle] = useState("")
    const [name, setName] = useState("")
    const [surname, setSurname] = useState("")
    const [email, setEmail] = useState("")
    const [mobile, setMobile] = useState("")
    const [travelers, setTravelers] = useState([])

    const book = (event) => {
        event.preventDefault();
          
        axios.post("http://127.0.0.1:8000/booking", {
            trip_detail: selected_value,
            contact_name: name,
            contact_surname: surname,
            contact_title: title,
            contact_email: email,
            contact_mobile: mobile,
            number_of_traveler: numTravelers,
            travelers: travelers
        })
        .then(res => {
            console.log(res.data);
        })
        .catch(err => {
            console.log(err);
        });
    }

    function addTraveler() {
        setNumTravelers(numTravelers + 1);
        setTravelers([...travelers, {}]);
    }

    useEffect(() => {
        const initialTravelers = Array(numTravelers).fill({});
        setTravelers(initialTravelers);
    }, [numTravelers])

    return (
        <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
            <h1 className="card text-white bg-danger mb-3" styleName="max-width: 20rem;">Booking</h1>
            <div>
                <h2>Flight Details</h2>
                <div className="bg-light rounded mb-5">
                    <label>Flight ID: {selected_value['flight_id']}</label><br />
                    <label>Airline: {selected_value['airline_name']}</label><br />
                    <label>Day: {selected_value['day']}</label><br />
                    <label>Departure Time: {selected_value['departure_time']}</label><br />
                    <label>Departure Airport: {selected_value['departure_airport']}</label><br />
                    <label>Arrival Time: {selected_value['arrival_time']}</label><br />
                    <label>Arrival Airport: {selected_value['arrival_airport']}</label><br />
                    <label>Cabin Baggage: {selected_value['cabin_baggage']} kg</label><br />
                    <label>Reschedule: {String(selected_value['reschedule'])}</label><br />
                    <label>Refund: {String(selected_value['refund'])}</label><br /> 
                </div>
                <h2>Contact Details</h2>
                <form className="bg-light rounded mb-5">
                    <label>Title</label><br />
                    <select className="mb-2" id="title" onChange={(e) => setTitle(e.target.value)}>
                        <option value="">None</option>
                        <option value="Mr">Mr</option>
                        <option value="Mrs">Mrs</option>
                        <option value="Ms">Ms</option>
                    </select><br />
                    <label>Name</label><br />
                    <input className="mb-2" type="text" placeholder="Name" id="name" onChange={(e) => setName(e.target.value)}></input><br />
                    <label>Surname</label><br />
                    <input className="mb-2" type="text" placeholder="Surname" id="surname" onChange={(e) => setSurname(e.target.value)}></input><br />
                    <label>Email</label><br />
                    <input className="mb-2" type="text" placeholder="Email" id="email" onChange={(e) => setEmail(e.target.value)}></input><br />
                    <label>Mobile</label><br />
                    <input className="mb-2" type="text" placeholder="Mobile" id="mobile" onChange={(e) => setMobile(e.target.value)}></input><br />
                </form>
                <h2>Traveler Details</h2>
                <form className="mb-5">
                    {[...Array(numTravelers)].map((_, i) => (
                        <Traveler 
                            key={i} 
                            travelerIndex={i} 
                            travelers={travelers} 
                            setTravelers={setTravelers} 
                        />
                    ))}
                </form>
                <button className="mb-2" onClick={addTraveler}>Add Traveler</button><br />
                <input type="submit" onClick={book}/>
            </div>
        </div>
    );
}