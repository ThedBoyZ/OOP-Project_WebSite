import { useNavigate } from "react-router";
import axios from "axios";
import { useState, useEffect } from "react";
import { airpaz_code } from "./Booking_page";

export {data}

var data = [];

export default function Payment() {
  const navigate = useNavigate();
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/booking/${airpaz_code['airpaz_code']}`)
      .then((res) => {
        setData(res.data["booking_details"]);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
      <h1 className="card text-white bg-danger mb-3" styleName="max-width: 20rem;">Payment</h1>
      <div>
        {data && (
          <div className="bg-light rounded mb-5">
            <label>Airpax Code: {String(data["airpaz_code"])}</label><br />
            <label>Booking Status: {String(data["status"])}</label><br />
          </div>
        )}
        <h2>Price Details</h2>
        {data && (
          <div className="bg-light rounded mb-5">
            <label>Adult x {String(data["price_details"]["Adult"]["Number_of_Adult"])}: {String(data["price_details"]["Adult"]["Total"])} ฿</label><br />
            <label>Child x {String(data["price_details"]["Child"]["Number_of_Child"])}: {String(data["price_details"]["Child"]["Total"])} ฿</label><br />
            <label>Infant x {String(data["price_details"]["Infant"]["Number_of_Infant"])}: {String(data["price_details"]["Infant"]["Total"])} ฿</label><br />
            <label>Baggage: {String(data["price_details"]["Baggage_price"])} ฿</label><br />
            <label>Total Price: {String(data["price_details"]["Total_price"])} ฿</label><br />
          </div>
        )}

        <h2>Payment Methods</h2>
        <a href="payment/promptpay">Promptpay</a><br/>
        <a href="payment/visa">VISA</a><br/>
        <a href="payment/paypal">PayPal</a><br/>
        <a href="/">Back to home</a>
      </div>
    </div>
  );
}