import {React, useState} from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Order(){
    const [airpaz_code, setAirpazCode] = useState("");

    const confirmed = () =>{

    }

    const complete = () =>{

    }

    const waiting = () =>{

    }

    const cancled = () =>{

    }

    return(
        <div>
            <h1>Order</h1>
            <form>
                <input type="text" placeholder="Airpaz Code"></input>
                <button type="submit">Search</button>
            </form>
            <button type="button" value="confirmed">Confirmed</button>
            <button type="button" value='complete'>Complete</button>
            <button type="button">Waiting</button>
            <button type="button">Cancled</button>
        </div>
    )
}