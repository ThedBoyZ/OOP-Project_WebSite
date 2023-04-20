import {React, useState} from "react";
import axios from "axios";

export default function Show_flight(respond_data){
    console.log(respond_data["status"])

    return (
        <div>
            <h2>Customer</h2>
            <form>
                <select>
                    <option value="Mr">Mr</option>
                    <option value="Mrs">Mrs</option>
                    <option value="Ms">Ms</option>
                </select><br/>
                <label>name</label><br/>
                <input type="text" placeholder="Name"></input><br/>
                <label>surname</label><br/>
                <input type="text"></input><br/>
                <label>phone number</label><br/>
                <input type="text"></input><br/>
                <label>email</label><br/>
                <input type="text"></input><br/>
            </form>

            <h2>Traveller</h2>
        </div>
    )
}