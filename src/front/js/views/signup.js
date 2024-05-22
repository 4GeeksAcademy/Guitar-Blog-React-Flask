import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useContext } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";
import "../../styles/demo.css"


export const Signup = () => {

	const [firstName, setFirstName] = useState("");
	const [lastName, setLastName] = useState("");
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();

	async function handleSignup(e) {
		e.preventDefault()
		let logged_in = await actions.signUp(firstName, lastName, email, password);
		console.log(logged_in);
			if (logged_in){
				navigate("/login")
			}
	}

	return (
		<div className="container" style={{height: "450px"}}>
			<div>
				<h1 className="text-center mt-4 text-primary">Sign Up!</h1>
				<form>
                <div className="form-group">
						<label>First Name</label>
						<input
							type="text"
							className="form-control"
							placeholder="First Name"
							onChange={e => setFirstName(e.target.value)}
							value={firstName}
                            required
						/>
					</div>
                    <div className="form-group">
						<label>Last Name</label>
						<input
							type="text"
							className="form-control"
							placeholder="Last Name"
							onChange={e => setLastName(e.target.value)}
							value={lastName}
                            required
						/>
					</div>
					<div className="form-group">
						<label>Email</label>
						<input
							type="email"
							className="form-control"
							placeholder="Enter email"
							onChange={e => setEmail(e.target.value)}
							value={email}
                            required
						/>
					</div>
					<div className="form-group">
						<label>Password</label>
						<input
							type="password"
							className="form-control"
							placeholder="Enter password"
							onChange={e => setPassword(e.target.value)}
							value={password}
                            required
						/>
					</div>
					<button type="button" className="btn btn-primary form-control mt-4" onClick={handleSignup}>
						Submit
					</button>
				</form>
			</div>
		</div>
	);
};
