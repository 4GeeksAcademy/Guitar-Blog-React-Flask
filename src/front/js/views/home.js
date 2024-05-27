import React from "react";
import "../../styles/home.css";
import { ElectricComp } from "./electricComp";
import { AcousticComp } from "./acousticComp";
import { ClassicalComp } from "./classicalComp";


export const Home = () => {

	return (
		<div className="base container-fluid bg-dark">
			<div className="border"></div>
			<h1 className="text-danger ms-4 mt-3">Electric Guitars</h1>
			<ElectricComp />
			<div className="border"></div>
			<h1 className="text-danger ms-4 mt-3">Acoustic Guitars</h1>
			<AcousticComp/>
			<div className="border"></div>
			<h1 className="text-danger ms-4 mt-3">Classical Guitars</h1>
			<ClassicalComp/>
		</div>
	);
};
