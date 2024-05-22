import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useContext } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";
import "../../styles/demo.css"


export const Login = () => {

	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();

	async function handleSubmit(e) {
		e.preventDefault()
		let logged_in = await actions.login(email, password);
		console.log(logged_in);
			if (logged_in){
				navigate("/")
			}
			else {
				navigate("/signup")
			}
	}

	return (
		<div className="container" style={{height: "408px"}}>
			<div>
				<h1 className="text-center mt-5">Add a new contact</h1>
				<form>
					<div className="form-group">
						<label>Email</label>
						<input
							type="email"
							className="form-control"
							placeholder="Enter email"
							onChange={e => setEmail(e.target.value)}
							value={email}
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
						/>
					</div>
					<button type="button" className="btn btn-primary form-control mt-4" onClick={handleSubmit}>
						Submit
					</button>
					<Link to={"/signup"}>
					<button type="button" className="btn btn-primary form-control mt-4">
						Sign Up if you don't have an account!!
					</button>
					</Link>
				</form>
			</div>
		</div>
	);
};
