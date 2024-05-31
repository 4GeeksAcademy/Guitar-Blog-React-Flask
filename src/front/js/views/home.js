import React from "react";
import "../../styles/home.css";
import { ElectricComp } from "./electricComp";
import { AcousticComp } from "./acousticComp";
import { ClassicalComp } from "./classicalComp";


export const Home = () => {

	return (
		<>
			{/* <div className="row d-flex justify-content-around text-white">
				<div className="col-1">Electric Guitars</div>
				<div className="col-1">Acoustic Guitars</div>
				<div className="col-1">Classical Guitars</div>
			</div> */}
		<div className="base container-fluid bg-dark">
			<div className="row d-flex justify-content-center">
			<div className="col-4 border mx-5"></div>
			<ElectricComp />
			<div className="col-4 border mx-5"></div>
			<AcousticComp/>
			<div className="col-4 border mx-5"></div>
			<ClassicalComp/>
			</div>
		</div>
		</>
	);
};
