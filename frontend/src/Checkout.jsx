// import { useNavigate } from "react-router";
// import axios from "axios";
// import { useState } from "react";
export { selected_value }

var selected_value = {
  "airline_name": "Thai Vietjet Air",
  "arrival_airport": "CNX",
  "arrival_date": null,
  "arrival_time": "11:15",
  "cabin_baggage": 7,
  "day": "Friday",
  "departure_airport": "BKK",
  "departure_date": null,
  "departure_time": "10:00",
  "flight_id": "VZ102",
  "refund": false,
  "reschedule": true,
  "status": "One Way"
}

// export default function Checkout() {
//   const navigate = useNavigate();
//   const [jsonItems, setJsonItems] = useState([]);
  
//   const show_select = () =>{
//     console.log(selected_value['data'])
//     const data = []
//     for(let i in selected_value['data']){
//       data.push(selected_value['data'][i])
//     }
   
//     const listItems = data.map((d, index) =>
//     <ul key={index}>
//       {
//         <h5>{d}</h5>
//       }
//     </ul>);
//     return listItems
//   }

//   const checkout = () =>{
//     //navigate('./payment')
//     console.log('payment')
//   }
  

  
//   return (
//     <>
//       {show_select()}
//       <button type="button" onClick={() => checkout()}>CHECKOUT</button>
//     </>
//   );
// }