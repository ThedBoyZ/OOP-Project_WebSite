import './App.css';
import {React, useEffect, useState} from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'

function Traveler() {
  return (
    <div className="traveler">
      <label>Type</label><br/>
      <select className="mb-2" name="type_person">
        <option value="Adult">Adult</option>
        <option value="Child">Child</option>
        <option value="Infant">Infant</option>
      </select><br/>
      <label>Title</label><br/>
      <select className="mb-2" name="title">
        <option value="Mr">Mr</option>
        <option value="Mrs">Mrs</option>
        <option value="Ms">Ms</option>
      </select><br/>
      <label>Gender</label><br/>
      <input className="mx-2" type="radio" name="gender" value="Male" />
      <label>Male</label>
      <input className="mx-2" type="radio" name="gender" value="Female" />
      <label>Female</label>
      <input className="mx-2" type="radio" name="gender" value="Other" />
      <label>Other</label>
      <input className="mx-2" type="radio" name="gender" value="" />
      <label>Prefer not to say</label><br/>
      <label>Name</label><br/>
      <input className="mb-2" type="text" name="name" placeholder="Name"></input><br/>
      <label>Surname</label><br/>
      <input className="mb-2" type="text" name="surname" placeholder="Surname"></input><br/>
      <label>Date of Birth</label><br/>
      <input className="mb-2" type="date" name="dob" pattern="\d{2}/\d{2}/\d{4}"></input><br/>
      <label>Nationality</label><br/>
      <select className="mb-2" name="nationality">
        <option value="Thailand">Thailand</option>
        <option value="United Kingdom">United Kingdom</option>
        <option value="United States">United States</option>
      </select><br/>
      <label>Add ons</label><br/>
      <select className="mb-2" name="add_ons_baggage" placeholder="+ Add Extra Baggage">
        <option value="0">No Baggage</option>
        <option value="15">+15kg(฿418)</option>
        <option value="20">+20kg(฿465)</option>
        <option value="25">+25kg(฿583)</option>
        <option value="30">+30kg(฿936)</option>
        <option value="35">+35kg(฿1125)</option>
        <option value="40">+40kg(฿1407)</option>
      </select><br/>
    </div>
  );
}

function Booking() {
  const [numTravelers, setNumTravelers] = useState(1);

  function addTraveler() {
    setNumTravelers(numTravelers + 1);
  }

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}}>
      <h1 className="card text-white bg-primary mb-3" styleName="max-width: 20rem;">Booking</h1>
        <div>
            <h2>Contact Details</h2>
            <form className="mb-5">
                <label>Title</label><br/>
                <select className="mb-2">
                    <option value="Mr">Mr</option>
                    <option value="Mrs">Mrs</option>
                    <option value="Ms">Ms</option>
                </select><br/>
                <label>Name</label><br/>
                <input className="mb-2" type="text" placeholder="Name"></input><br/>
                <label>Surname</label><br/>
                <input className="mb-2" type="text" placeholder="Surname"></input><br/>
                <label>Email</label><br/>
                <input className="mb-2" type="text" placeholder="Email"></input><br/>
                <label>Mobile</label><br/>
                <input className="mb-2" type="text" placeholder="Mobile"></input><br/>
            </form>
            <h2>Traveler Details</h2>
            <form className="mb-5">
              {[...Array(numTravelers)].map((_, i) => (
                <Traveler key={i} />
              ))}
            </form>
            <button onClick={addTraveler}>Add Traveler</button>
        </div>
    </div>
  );
}

export default Booking;