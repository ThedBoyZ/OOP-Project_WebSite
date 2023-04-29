import React, { useState } from "react";

function TravelForm() {
  const [numTravelers, setNumTravelers] = useState(1);
  const [travelerInfo, setTravelerInfo] = useState([]);

  // function to handle changing the number of travelers
  function handleNumTravelersChange(event) {
    setNumTravelers(event.target.value);
  }

  // function to handle submitting the form
  function handleSubmit(event) {
    event.preventDefault();
    // send the travelerInfo data to the next page
    // ...
  }

  // generate an array of input fields based on the number of travelers
  const travelerInputs = [];
  for (let i = 0; i < numTravelers; i++) {
    travelerInputs.push(
      <div key={i}>
        <label htmlFor={`type-${i}`}>Type</label><br />
            <select className="mb-2" id={`type-${i}`} name={`type-${i}`}
            onChange={(event) =>
                setTravelerInfo((prevState) => {
                    prevState[i].type = event.target.value;
                    return [...prevState];
                })
              }>
                <option value="Adult">Adult</option>
                <option value="Child">Child</option>
                <option value="Infant">Infant</option>
            </select><br />

        <label htmlFor={`title-${i}`}>Title</label><br />
            <select className="mb-2" id={`title-${i}`} name={`title-${i}`}
            onChange={(event) =>
                setTravelerInfo((prevState) => {
                    prevState[i].title = event.target.value;
                    return [...prevState];
                })
              }>
                <option value="">None</option>
                <option value="Mr">Mr</option>
                <option value="Mrs">Mrs</option>
                <option value="Ms">Ms</option>
            </select><br />

        <label htmlFor={`gender-${i}`}>Gender</label><br />
            <select className="mb-2" id={`gender-${i}`} name={`gender-${i}`}
            onChange={(event) =>
                setTravelerInfo((prevState) => {
                    prevState[i].gender = event.target.value;
                    return [...prevState];
                })
              }>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
                <option value="">Prefer not to say</option>
            </select><br />

        <label htmlFor={`name-${i}`}>Name:</label><br />
        <input className="mb-2" type="text" id={`name-${i}`} name={`name-${i}`}
        onChange={(event) =>
            setTravelerInfo((prevState) => {
                prevState[i].name = event.target.value;
                return [...prevState];
            })
          }
        /><br />

        <label htmlFor={`surname-${i}`}>Surname:</label><br />
        <input className="mb-2" type="text" id={`surname-${i}`} name={`surname-${i}`}
        onChange={(event) =>
            setTravelerInfo((prevState) => {
                prevState[i].surname = event.target.value;
                return [...prevState];
            })
          }
        /><br />

        <label htmlFor={`dob-${i}`}>Date of Birth:</label><br />
        <input className="mb-2" type="date" id={`dob-${i}`} name={`dob-${i}`}
        onChange={(event) =>
            setTravelerInfo((prevState) => {
                prevState[i].dob = event.target.value;
                return [...prevState];
            })
          }
        /><br />

        <label htmlFor={`nationality-${i}`}>Nationality:</label><br />
            <select className="mb-2" id={`nationality-${i}`} name={`nationality-${i}`}
            onChange={(event) =>
                setTravelerInfo((prevState) => {
                    prevState[i].nationality = event.target.value;
                    return [...prevState];
                })
              }>
                <option value="Thailand">Thailand</option>
                <option value="United Kingdom">United Kingdom</option>
                <option value="United States">United States</option>
            </select><br />

        <label htmlFor={`baggage_weight-${i}`}>Add ons:</label><br />
            <select className="mb-2" placeholder="+ Add Extra Baggage" id={`baggage_weight-${i}`} name={`baggage_weight-${i}`}
            onChange={(event) =>
                setTravelerInfo((prevState) => {
                    prevState[i].baggage_weight = event.target.value;
                    return [...prevState];
                })
              }>
                <option value="0">No Baggage</option>
                <option value="15">+15kg(฿418)</option>
                <option value="20">+20kg(฿465)</option>
                <option value="25">+25kg(฿583)</option>
                <option value="30">+30kg(฿936)</option>
                <option value="35">+35kg(฿1125)</option>
                <option value="40">+40kg(฿1407)</option>
            </select><br />
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="num-travelers">Number of travelers:</label>
      <input
        type="number"
        id="num-travelers"
        name="num-travelers"
        value={numTravelers}
        onChange={handleNumTravelersChange}
      />
      {travelerInputs}
      <button type="submit">Submit</button>
    </form>
  );
}

export default TravelForm;