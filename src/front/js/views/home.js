import React from "react";
import "../../styles/home.css";
import { ElectricComp } from "./electricComp";
import { AcousticComp } from "./acousticComp";
import { ClassicalComp } from "./classicalComp";


export const Home = () => {

	return (
		<div className="base container-fluid bg-dark">
			<h2 className="text-danger ms-4">Electric Guitars</h2>
			<ElectricComp />
			<h2 className="text-danger ms-4">Acoustic Guitars</h2>
			<AcousticComp/>
			<h2 className="text-danger ms-4">Classical Guitars</h2>
			<ClassicalComp/>
		</div>
	);
};
