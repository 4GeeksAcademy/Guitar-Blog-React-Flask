import React, { useContext, useEffect } from "react";
import "../../styles/home.css";
import { Context } from "../store/appContext";



export const Favorites = () => {


    const { store, actions } = useContext(Context);


    useEffect(() => {
        actions.getFavorites();
    }, []);

    const favourites = Array.isArray(store.favourites) ? store.favourites : [];

    return (
        <>
            <div className="card-people d-flex">
                {favourites.map((item, index) => {
                    console.log(item); // Aquí agregamos el console.log para ver el contenido de cada item
                    return (
                        <div className="card-group" key={index}>
                            <div className="card">
                                <img src={item.favorite.image} style={{maxWidth: "250px", maxHeight: "150px", objectFit: "cover" }} className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h5 className="card-title">{item.favorite.model}</h5>
                                </div>
                                <div className="footer">
                                    
                                        <button className="boton-learn bg-secondary" onClick={() =>
							actions.deleteFavourite(item.id)}>Delete!</button>
                                    
                                </div>
                            </div>
                        </div>
                    );
                })}

            </div>

        </>
    );
};
