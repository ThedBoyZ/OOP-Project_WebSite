import './App.css'
import React from 'react'

import { Routes, Route } from "react-router-dom";
import Login from "./Login";
import Profile from './Profile';
import Register from './Register';
import Homepage from './Homepage';
import Promotion from './Promotion';
import Show_flight from './show_flight';

function App(){
  return (
    <div className ="App">
    <Routes>
      <Route path="/" element = {<Homepage/>}/>
      <Route path="/login" element = {<Login/>}/>
      <Route path="/profile" element = {<Profile/>}/>
      <Route path="/register" element = {<Register/>}/>
      <Route path="/promotion" element = {<Promotion/>}/>
      <Route path='/show_flight' element = {<Show_flight/>} />
    </Routes>
    </div>
  )
}

export default App