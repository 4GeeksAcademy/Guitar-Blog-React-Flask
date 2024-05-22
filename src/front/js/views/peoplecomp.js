import React, { useContext, useEffect, useState, useSyncExternalStore } from "react";
import "../../styles/home.css";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";



export const PeopleComp = () => {


	const { store, actions } = useContext(Context);


	useEffect(() => {
		actions.getPeople();
	}, []);
	console.log(store.people);


	return (
		<>
			<div className="card-people d-flex">
			{store.people.map((item, index) => {
    console.log(item); // Aquí agregamos el console.log para ver el contenido de cada item
    return (
        <div className="card-group" key={index}>
            <div className="card">
                <img src={item.image} style={{ objectFit: "cover" }} className="card-img-top" alt="guitar picture" />
                <div className="card-body">
                    <h5 className="card-title">{item.model}</h5>
                    <h5 className="card-title">{item.color}</h5>
                </div>
                <div className="footer">
                    <Link to={`/people/${item.id}`}>
                        <button className="boton-learn">Learn More!</button>
                    </Link>
                </div>
            </div>
        </div>
    );
})}

			</div>
		
        </>
	);
};
