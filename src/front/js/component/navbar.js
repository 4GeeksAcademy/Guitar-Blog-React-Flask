import React, { useContext } from "react";
import { Link } from "react-router-dom";
import "../../styles/demo.css";
import { Context } from "../store/appContext"
import starwarsyellow from '../../img/guitarra_mujer.jpg'
import { useNavigate } from "react-router-dom";


export const Navbar = () => {

	const { store, actions } = useContext(Context);
	const navigate = useNavigate();


	const handleLogout = async () => {
		localStorage.removeItem("token");
		await actions.validToken();  // Si `validToken` es una función asincrónica, usa `await`.
		navigate("/login");
	}
	

	return (
		<nav className="navbar bg-dark" data-bs-theme="dark">
			<div className="container d-flex justify-content-between">
				<div className="d-flex col-4 justify-content-start">
					<Link to={"/"} style={{ textDecoration: 'none', color: "white" }}>
						<span className="navbar-brand">Home</span>
					</Link>
					{store.auth && (
						<Link to={"/favorites"} style={{ textDecoration: 'none', color: "white" }}>
							<span className="navbar-brand ms-3">Your Favorites</span>
						</Link>
					)}
				</div>
				<div className="d-flex col-4 justify-content-center">
					<h1 className="sevillana-regular text-white">Osian's Guitars</h1>
				</div>
				<div className="d-flex col-4 justify-content-end">
					<Link to={"/login"} style={{ textDecoration: 'none', color: "white", marginRight: '10px' }}>
						<span className="login-link">Log In</span>
					</Link>
					<span className="login-link" style={{ color: "white", cursor: "pointer" }} onClick={handleLogout}>Log Out</span>
				</div>
			</div>
		</nav>
	);
	
};