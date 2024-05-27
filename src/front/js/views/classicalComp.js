import React, { useContext, useEffect, useState, useSyncExternalStore } from "react";
import "../../styles/home.css";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";


export const ClassicalComp = () => {


    const { store, actions } = useContext(Context);


    useEffect(() => {
        actions.getClassical();
    }, []);


    return (

        <div className="card-people d-flex">
            {store.classical.map((item, index) => (
                <div className="card-group" key={index}>
                    <div className="card">
                    <img src={item.image} style={{maxWidth: "250px", maxHeight: "150px", objectFit: "cover" }} className="card-img-top" alt="guitar picture" />
                        <div className="card-body">
                            <h5 className="card-title">{item.model}</h5>
                        </div>
                        <div className="footer">
                            <Link to={`/classical/${item.id}`}>
                                <button className="boton-learn" >Learn More!</button>
                            </Link>
                        </div>
                    </div>
                </div>
            ))}
        </div>

    );
};