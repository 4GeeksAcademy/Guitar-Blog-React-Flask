import React, { useContext, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/demo.css";

export const Electric = () => {
	const { id } = useParams();
	const { store, actions } = useContext(Context);

	useEffect(() => {
		actions.getElectricData(id);

	}, []);

	const storeElectric = store.electricData;



	return (
		<div className="container h-100">
			<div className="card h-75" style={{ width: "100%" }}>
				<div className="row">
					<div className="col-md-4">
						<img src={storeElectric.image} className="img-fluid h-100 w-100 object-cover"  alt="guitar_image" />
					</div>
					<div className="col-md-8 h-100">
						<div className="card-body">
							<h5 className="card-title">{storeElectric.model}</h5>
							<p className="card-text">{storeElectric.description}</p>

						</div>
						
					</div>
					<div className="red-line d-flex mt-3"></div>
					<div className="mini-container d-flex justify-content-evenly mt-3 align-self-center">
						<div><h3>Manufacturer</h3><p>{storeElectric.manufacturer}</p></div>
						<div><h3>Scale</h3><p>{storeElectric.scale}</p></div>
						<div><h3>Color</h3><p>{storeElectric.color}</p></div>
						<div><h3>Pickups</h3><p>{storeElectric.pickups}</p></div>
						<div><h3>Price</h3><p>{storeElectric.price}</p></div>
					</div>
				</div>
			</div>
			<div className="footer__card">
			<Link to="/">
				<button className="btn btn-secondary">Back home</button>
			</Link>
				<button className="btn btn-secondary" onClick={() => actions.addFavouriteElectric(storeElectric.id)}>Add to Favorites</button>
				</div>
		</div>
	);
};
