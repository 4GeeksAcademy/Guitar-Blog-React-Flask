import React, { useContext, useEffect, useState, useSyncExternalStore } from "react";
import "../../styles/home.css";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";


export const StarshipsComp = () => {


    const { store, actions } = useContext(Context);


    useEffect(() => {
        actions.getStarships();
    }, []);
    console.log(store.starships);


    return (

        <div className="card-people d-flex">
            {store.starships.map((item, index) => (
                <div className="card-group" key={index}>
                    <div className="card">
                        <img src={item.image} style={{ objectFit: "cover" }} className="card-img-top" alt="..." />
                        <div className="card-body">
                            <h5 className="card-title">{item.model}</h5>
                            <h5 className="card-title">{item.color}</h5>
                        </div>
                        <div className="footer">
                            <Link to={`/starships/${item.id}`}>
                                <button className="boton-learn" >Learn More!</button>
                            </Link>
                        </div>
                    </div>
                </div>
            ))}
        </div>

    );
};