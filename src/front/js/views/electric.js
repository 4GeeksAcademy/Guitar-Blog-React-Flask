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
            <div className="card h-75 w-100">
                <div className="row h-75">
                    <div className="image-container col-md-4 d-flex align-items-center justify-content-center p-3 mt-5" style={{ height: "300px", overflow: "hidden" }}>
                        <img src={storeElectric.image} alt="guitar_image" className="img-fluid border" style={{ objectFit: "cover", width: "300px", height: "100%" }} />
                    </div>
                    <div className="col-md-8 h-75 mt-5">
                        <div className="card-body">
                            <h5 className="card-title">{storeElectric.model}</h5>
                            <p className="card-text">{storeElectric.description}</p>
                        </div>
                    </div>
                    <div className="red-line d-flex"></div>
                    <div className="mini-container d-flex justify-content-evenly mt-3">
                        <div><h2>Manufacturer</h2><p>{storeElectric.manufacturer}</p></div>
                        <div><h2>Scale</h2><p>{storeElectric.scale}</p></div>
                        <div><h2>Color</h2><p>{storeElectric.color}</p></div>
                        <div><h2>Pickups</h2><p>{storeElectric.pickups}</p></div>
                        <div><h2>Price</h2><p>{storeElectric.price}</p></div>
                    </div>
                </div>
            </div>
            <div className="footer__card mt-3">
                <Link to="/">
                    <button className="btn btn-secondary">Back home</button>
                </Link>
                <button className="btn btn-secondary" onClick={() => actions.addFavouriteElectric(storeElectric.id)}>Add to Favorites</button>
            </div>
        </div>
    );
};
