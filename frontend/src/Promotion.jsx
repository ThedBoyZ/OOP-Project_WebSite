import { useState, React, useEffect } from "react";
import axios from "axios";

const show_coupon = () => {
  return axios.get("http://127.0.0.1:8000/coupon_home")
    .then(res => res.data['Data']['_coupon_detail'])
    .catch(err => {
      console.error(err);
      return [];
    });
}

export default function Promotion() {

  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const couponData = await show_coupon();
      setData(couponData);
    };
    fetchData();
  }, []);

  if (!data || data.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
      <h1 className="card text-white bg-danger mb-3" styleName="max-width: 20rem;">Promotion page</h1>
      <div>
  
        {data.map((item, index) => (
          <div key={index}>
            <h5 style={{ fontWeight: 'bold'}}>---- Coupon {index+1} ----</h5>
            <p>Code : {item.code}</p>
            <p>Discount : {item.discount}</p>
            <p>Description : {item.description}</p>
            
          </div>
        ))}
      </div>
    </div>
  );
}