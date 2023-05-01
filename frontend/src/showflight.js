import {React, useState} from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { respond_data as respond } from "./Homepage";
export {selected_value}

//console.log(respond_data["status"])
var selected_value = {}

export default function Show_flight(){
    const navigate = useNavigate()

    const select = (data, index) =>{
        selected_value = {
            data :data[index]
            
        }
        navigate('/checkout')
        //console.log(selected_value['data'])
    }

    const show_flight = () => {

        //console.log(respond[0])
        
        const data = []
        for(let i=0; i<respond.length; i++){

            //data.push(respond[i]['flight_id'])
            data.push(respond[i])
            
        }
        //console.log(data)
        const listItems = data.map((d, index) => 
        <ul key={index}>
            
            {
                <form>

                    <h5>
                        flight_id : {d['flight_id']}&emsp;
                        airline_name : {d['airline_name']}&emsp;
                        departure_time : {d['departure_time']}&emsp;
                        arrival_time : {d['arrival_time']}&emsp;
                    
                        <button id="data_index" type="button" onClick={() => select(data, index)} value={index}>Select</button>
                    </h5>
                </form>
            }
        </ul>);
        
        return listItems
    }
    
    return (
        <div id="content">
            
            <a href="/">Airpaz&emsp;</a>
            <a href="/">Home&emsp;</a>
            <a href="/booking">Booking&emsp;</a>
            <a href="/login">Sign in&emsp;</a>
            <a href="/profile">Profile&emsp;</a>
            <a href="/promotion">Promotion&emsp;</a>
            <a href="/order">Order&emsp;</a>
            {show_flight()}
            
        </div>
    )

    
}