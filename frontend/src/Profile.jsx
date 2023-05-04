import { useState, useEffect } from "react";
import axios from "axios";

const Profile = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/see_profile")
      .then(response => 
        {
          setData(response.data)
          console.log(response.data)
        })
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Profile</h1>
      <ul>
        {Object.values(data).length > 0 ? (
          Object.values(data).map((item,index) => (
            <li key={index}>
              <p>Name : {item.name}</p>
              <p>Surname : {item.surname}</p>
              <p>Email : {item.email}</p>
              <p>Country : {item.country}</p>
            </li>
          ))
        ) : (
          <p>Loading...</p>
        )}
      </ul>
    </div>
  );
};

export default Profile;