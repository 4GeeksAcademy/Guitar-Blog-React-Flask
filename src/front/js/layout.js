import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";


import { Home } from "./views/home";
import { Signup } from "./views/signup";
import { Login } from "./views/login";
import { Favorites } from "./views/favorites";
import { People } from "./views/people";
import { Planets } from "./views/planets";
import { Starships } from "./views/starships";
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";

//create your first component
const Layout = () => {
	//the basename is used when your project is published in a subdirectory and not in the root of the domain
	// you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
	const basename = process.env.BASENAME || "";

	return (
		<div className="bg-dark">
			<BrowserRouter basename={basename}>
				<ScrollToTop>	
					<Navbar />
					<Routes>
						<Route path="/" element={<Home />} />
						<Route path="/signup" element={<Signup />} />
						<Route path="/people/:id" element={<People />} />
						<Route path="/planets/:id" element={<Planets />} />
						<Route path="/starships/:id" element={<Starships />} />
						<Route path="/login" element={<Login />} />
						<Route path="/favorites" element={<Favorites />} />
						<Route path="*" element={<h1>Not found!</h1>} />
					</Routes>
					<Footer />
				</ScrollToTop>
			</BrowserRouter>
		</div>
	);
};

export default injectContext(Layout);
