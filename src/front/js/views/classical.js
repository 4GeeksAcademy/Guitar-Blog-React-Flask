import React, { useContext, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import { Modal, Button } from "react-bootstrap";
import "../../styles/demo.css";

export const Classical = () => {
    const { id } = useParams();
    const { store, actions } = useContext(Context);
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        actions.getClassicalData(id);
    }, []);


    const handleClose = () => setShowModal(false);

	const storeClassical = store.classicalData;

     // Función para manejar el clic en el botón "Añadir a favoritos"
     const handleAddToFavorites = () => {
        actions.addFavouriteClassical(storeClassical.id);
        // Mostrar el modal solo cuando se añade a favoritos
        setShowModal(true);
    };

	return (
        <>
        <div className="container h-100 d-flex flex-column align-items-center">
            <div className="card h-75 w-100">
                <div className="row h-75">
                    <div className="image-container col-md-4 d-flex align-items-center justify-content-center p-3" style={{ height: "300px", overflow: "hidden" }}>
                        <img src={storeClassical.image} alt="guitar_image" className="img-fluid border" style={{ objectFit: "cover", width: "300px", height: "100%" }} />
                    </div>
                    <div className="col-md-8 h-75 mt-5">
                        <div className="card-body">
                            <h5 className="card-title">{storeClassical.model}</h5>
                            <p className="card-text">{storeClassical.description}</p>
                        </div>
                    </div>
                    <div className="red-line d-flex"></div>
                    <div className="mini-container d-flex justify-content-evenly mt-4">
                        <div><h2>Manufacturer</h2><p>{storeClassical.manufacturer}</p></div>
                        <div><h2>Scale</h2><p>{storeClassical.scale}</p></div>
                        <div><h2>Color</h2><p>{storeClassical.color}</p></div>
                        <div><h2>Price</h2><p>{storeClassical.price}</p></div>
                    </div>
                </div>
            </div>
            <div className="footer__card mt-3">
                <div>
                <Link to="/">
                    <button className="btn buton__favorites">Back home</button>
                </Link>
                </div>
                <div>
                <button className="btn buton__favorites" onClick={handleAddToFavorites}>Add to Favorites</button>
                </div>        
            </div>
        </div>
        <Modal show={showModal} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Message</Modal.Title>
                </Modal.Header>
                <Modal.Body>{store.message}</Modal.Body>
                <Modal.Footer>
                    <Button variant="primary" onClick={handleClose}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
            </>
    );
};
