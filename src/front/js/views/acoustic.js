import React, { useContext, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/demo.css";


export const Acoustic = () => {
	const {id} = useParams();
	const { store, actions } = useContext(Context);
	

		useEffect(() => {
		actions.getAcousticData(id);

	}, []);

	const storeAcoustic = store.acousticData; 

	return (
		<div className="container">
			<div className="card mb-3" style={{ width: "1100px" }}>
			<div className="row g-0">
					<div className="col-md-4">
						<img style={{ width: "600px", height: "250px" }} src={storeAcoustic.image} className="img-fluid rounded-start" alt="..." />
					</div>
					<div className="col-md-8">
						<div className="card-body">
							<h5 className="card-title">{storeAcoustic.model}</h5>
							<p className="card-text">{storeAcoustic.description}</p>

						</div>
						
					</div>
					<div className="red-line mt-3"></div>
					<div className="mini-container d-flex justify-content-evenly mt-3">
						<div><h3>Manufacturer</h3><p>{storeAcoustic.manufacturer}</p></div>
						<div><h3>Scale</h3><p>{storeAcoustic.scale}</p></div>
						<div><h3>Color</h3><p>{storeAcoustic.color}</p></div>
						<div><h3>Price</h3><p>{storeAcoustic.price}</p></div>
					</div>
				</div>
			</div>
			<div className="footer__card">
			<Link to="/">
				<button className="btn btn-secondary">Back home</button>
			</Link>
				<button className="btn btn-secondary me-3" onClick={() => actions.addFavouriteAcoustic(storeAcoustic.id)}>Add to Favorites</button>
				</div>
		</div>
	);
};
