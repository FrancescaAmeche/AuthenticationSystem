import React, { useState, useEffect, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

export const Navbar = () => {
	const {store, actions} = useContext(Context)
	const navigate = useNavigate()
	function handleLogout() {
		actions.logout()
		navigate("/")
	}

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					<Link to="/demo">
						<button className="btn btn-primary">Check the Context in action</button>
					</Link>
				</div>
				<Link to="/signup">
					<span className="navbar-brand mb-0 h1">Signup</span>
				</Link>
				<Link to="/login">
					<span className="navbar-brand mb-0 h1">Login</span>
				</Link>
				{store.auth === true ? <button onClick={() => handleLogout()} className="btn btn-primary">Logout</button> : null}
			</div>
		</nav>
	);
};
