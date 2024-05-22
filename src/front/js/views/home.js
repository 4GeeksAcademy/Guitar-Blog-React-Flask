import React, { useEffect, useState, useSyncExternalStore } from "react";
import "../../styles/home.css";
import { PeopleComp } from "./peoplecomp";
import { PlanetsComp } from "./planetscomp";
import { StarshipsComp } from "./starshipscomp";


export const Home = () => {

	return (
		<div className="base container-fluid bg-dark">
			<h2 className="text-danger ms-4">Electric Guitars</h2>
			<PeopleComp />
			<h2 className="text-danger ms-4">Acoustic Guitars</h2>
			<PlanetsComp/>
			<h2 className="text-danger ms-4">Classical Guitars</h2>
			<StarshipsComp/>
		</div>
	);
};
