import './App.css'
import React from 'react'

import { Routes, Route } from "react-router-dom";
import Login from "./Login";
import Profile from './Profile';
import Register from './Register';
import Homepage from './Homepage';
import Promotion from './Promotion';
import Show_flight from './show_flight';
import Order from './Order';
import Payment from './Payment'
import Add_flight from './Add_flight';
import Checkout from './Checkout';

import Paypal from './Paypal';
import Promptpay from './Promptpay';
import Visa from './Visa';

import Booking from './Booking_page';

function App(){
  return (
    <div className ="App">
      <Routes>
        <Route path="/" element = {<Homepage/>}/>
        <Route path="/login" element = {<Login/>}/>
        <Route path="/profile" element = {<Profile/>} />
        <Route path="/register" element = {<Register/>} />
        <Route path="/promotion" element = {<Promotion/>} />
        <Route path='/show_flight' element = {<Show_flight/>} />
        <Route path='/order' element = {<Order/>} />
        <Route path='/payment' element = {<Payment/>} />
        <Route path='/Add_flight' element = {<Add_flight/>}/>
        <Route path='/checkout' element = {<Checkout/>}/>
        <Route path='/order' element = {<Order/>}/>

        <Route path='/payment/promptpay' element = {<Promptpay/>}/>
        <Route path='/payment/paypal' element = {<Paypal/>}/>
        <Route path='/payment/visa' element = {<Visa/>}/>

        <Route path='/booking' element = {<Booking/>}/>
      </Routes>
    </div>
  )
}

export default App