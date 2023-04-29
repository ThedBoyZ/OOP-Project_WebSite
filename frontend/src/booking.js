import './App.css';
import { React, useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'


function Booking() {
  const [hasError, setErrors] = useState(false);
  const [airpazcode, setAirpazcode] = useState({});
  const [booking, setBooking] = useState({});

  async function fetchData() {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/booking/get_booking/${airpazcode}`);
      setBooking(res.data);
    } catch (error) {
      setErrors(true);
    }
  }

  useEffect(() => {
    fetchData();
  }, [airpazcode]);

  const handleInputChange = (event) => {
    setAirpazcode(event.target.value);
  };

  return (
    <div>
      <h1>Booking</h1>
      <div>
        <label htmlFor="airpazcode">Airpaz Code:</label>
        <input
          type="text"
          id="airpazcode"
          name="airpazcode"
          value={airpazcode}
          onChange={handleInputChange}
        />
        <button onClick={fetchData}>Search</button>
      </div>
      {hasError && <p>Error fetching booking data</p>}
      {!hasError && booking && (
        <div>
          <p>Airpaz Code: {booking.airpaz_code}</p>
          <p>Flight Details: {booking.trip_detail}</p>
          <p>Contact Details: {booking.contact_info}</p>
          <p>Traveler Details: {booking.travelers}</p>
          <p>Price Details: {booking.total_price}</p>
        </div>
      )}
    </div>
  );
}

export default Booking;
