import {React, useState} from "react";
import axios from "axios";

export default function Show_flight(respond_data){
    console.log(respond_data["matching_flights"])
    
    return (
        <div>
            <p>Show flight page</p>
        </div>
    )
}