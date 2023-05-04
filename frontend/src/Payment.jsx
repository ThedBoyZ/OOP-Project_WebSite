import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from "react";
import { airpaz_code } from "./Booking_page";

export { id }
var id

export default function Payment() {
  
  const navigate = useNavigate();
  const [data, setData] = useState(null);
  const [promocode, setPromocode] = useState("");
  const [status, setStatus] =useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/booking/${airpaz_code['airpaz_code']}`)
      .then((res) => {
        setData(res.data["booking_details"]);
        // console.log(data['airpaz_code']);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const promptpay = () => {
      id = airpaz_code['airpaz_code'];
      navigate('/payment/promptpay')
  }

  const creditcard = () => {
      id = airpaz_code['airpaz_code'];
      navigate('/payment/creditcard')
  }

  const paypal = () => {
      id = airpaz_code['airpaz_code'];
      navigate('/payment/paypal')
  }

  const verify = () => {
      axios.post("http://127.0.0.1:8000/discount", {
          airpaz_code: `${airpaz_code['airpaz_code']}`,
          promo_code: promocode,
      })
      .then(res => {
        console.log(res.data);
        setStatus(res.data["Status"])
      });
  };


  return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
      <h1 className="card text-white bg-danger mb-3" styleName="max-width: 20rem;">Payment</h1>
      <div>
        {data && (
          <div className="bg-light rounded mb-5">
            <label>Airpaz Code: {String(data["airpaz_code"])}</label><br />
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
        <h5>Voucher/Promo Code</h5>
        <input className="mt-2" type="text" placeholder="Input code here" id="promocode" onChange={(e) => setPromocode(e.target.value)}></input>
        <button className="bg-light rounded mb-2" type="button" onClick={() => verify()}>verify</button><br/>
        <label style={{ fontWeight: 'bold' , color:'red' }}>{status}</label>

        <h2>Payment Methods</h2>
        <button className="bg-light rounded mb-2" type="button" onClick={() => promptpay()}>Promptpay</button><br/>
        <button className="bg-light rounded mb-2" type="button" onClick={() => creditcard()}>Credit Card</button><br/>
        <button className="bg-light rounded mb-2" type="button" onClick={() => paypal()}>PayPal</button><br/>
      </div>
    </div>
  );
} 
