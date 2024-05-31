const getState = ({ getStore, getActions, setStore }) => {


	return {

		store: {
			electric: [],
			acoustic: [],
			classical: [],

			electricData: {},
			acousticData: {},
			classicalData: {},

			favourites: [],
			message: "",
			// counter: 0,
			auth: false
		},
		
		actions: {

			addFavouriteElectric :async (id)=>{
				let token = localStorage.getItem("token")
				try {
					const response = await fetch(process.env.BACKEND_URL + `/api/favorites/electric/${id}`, 
					
					{
						method: "POST",
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + token
						},

					})
					const data = await response.json()
					console.log(data.results)
					if (response.status == 200) {
						setStore({ message: "Successfully added as a favorite!" })
					}
					else if (response.status == 409) {
						setStore({ message: "You already have this guitar in favorites" })
					}
					
					return true;

				}	catch (error) {
					return false; 
				}
			},

			addFavouriteAcoustic :async (id)=>{
				let token = localStorage.getItem("token")
				try {
					const response = await fetch(process.env.BACKEND_URL + `/api/favorites/acoustic/${id}`, 
					
					{
						method: "POST",
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + token
						},

					})
					const data = await response.json()
					console.log(data.results)
					if (response.status == 200) {
						setStore({ message: "Successfully added as a favorite!" })
					}
					else if (response.status == 409) {
						setStore({ message: "You already have this guitar in favorites" })
					}
					
					return true;

				}	catch (error) {
					return false; 
				}
			},
	
			addFavouriteClassical :async (id)=>{
				let token = localStorage.getItem("token")
				try {
					const response = await fetch(process.env.BACKEND_URL + `/api/favorites/classical/${id}`, 
					
					{
						method: "POST",
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + token
						},

					})
					const data = await response.json()
					if (response.status == 200) {
						setStore({ message: "Successfully added as a favorite!" })
					}
					else if (response.status == 409) {
						setStore({ message: "You already have this guitar in favorites" })
					}
					
					return true;

				}	catch (error) {
					return false; 
				}
			},

			getFavorites: async () => {
				let token = localStorage.getItem("token")
				try  {
					const response = await fetch(process.env.BACKEND_URL + '/api/user/favorites', 
					{
						method: "GET",
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + token
						},

					})
					const data = await response.json()
					console.log(data.results)
					if (response.status == 200) {
						setStore({ favourites: data.results })
					}
					
					return true;
				}	catch (error) {
					return false; 
				}




			},

			deleteFavourite: async (id) => {
				let token = localStorage.getItem("token")
				try {
					const response = await fetch(process.env.BACKEND_URL + `/api/favorites/${id}`, 
					{
						method: "DELETE",
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + token
						},

					})
					const data = await response.json()
					console.log(data)
					if (response.status == 200) {
						window.location.reload();
						return true
					}

				} catch (error) {
					return false; 
				}
			},


			getAcoustic: () => {
					fetch(process.env.BACKEND_URL + '/api/acoustic-guitars')
						.then(res => res.json())
						.then(data => setStore({ acoustic: data.results }))
						.catch(err => console.error(err))
			},

			 getAcousticData: (id) => {
			 	
			 	fetch(process.env.BACKEND_URL + `/api/acoustic/${id}`)
			.then(res => res.json())
			.then(data => setStore({ acousticData: data.results }))
			// .then(data => console.log(data))
			.catch(err => console.error(err))}, 




			getElectric: () => {

				fetch(process.env.BACKEND_URL + '/api/electric-guitars')
					.then(res => res.json())
					.then(data => setStore({ electric: data.results }))
					.catch(err => console.error(err))

			},

			getElectricData: (id) => {
			 	
				fetch(process.env.BACKEND_URL + `/api/electric/${id}`)
		   .then(res => res.json())
		   .then(data => setStore({ electricData: data.results }))
		   .catch(err => console.error(err))}, 


			getClassical: () => {

				fetch(process.env.BACKEND_URL + '/api/classical-guitars')
					.then(res => res.json())
					.then(data => setStore({ classical: data.results }))
					.catch(err => console.error(err))

			},

			getClassicalData: (id) => {
			 	
				fetch(process.env.BACKEND_URL + `/api/classical/${id}`)
		   .then(res => res.json())
		   .then(data => setStore({ classicalData: data.results }))
		   .catch(err => console.error(err))}, 


			login: async (email, password) => {
				try  {
					const response = await fetch(process.env.BACKEND_URL +'/api/login', 
					{
						method: "POST",
						headers: {
							"Content-Type": "application/json"
						},
						body: JSON.stringify({
							"email": email,
							"password": password
						})

					})
					const data = await response.json()
					if (response.status == 200) {
						localStorage.setItem("token", data.access_token)
						return true;
					}
					else {
						return false;
					}
				}	catch (error) {
					return false; 
				}




			},
			
			signUp: async (firstName, lastName,email, password) => {
				try  {
					const response = await fetch(process.env.BACKEND_URL +'/api/signup', 
					{
						method: "POST",
						headers: {
							"Content-Type": "application/json"
						},
						body: JSON.stringify({
							"first_name": firstName,
							"last_name": lastName,
							"email": email,
							"password": password
						})

					})
					const data = await response.json()
					if (response.status == 200) {
						
					}
					return true;
				}	catch (error) {
					return false; 
				}




			},
 
			validToken: async () => {
				let token = localStorage.getItem("token")
				try  {
					const response = await fetch(process.env.BACKEND_URL +'/api/valid-token', 
					{
						method: "GET",
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + token
						}

					})
					let data = await response.json()
					if (response.status == 200) {
						setStore({auth: data.is_logged})
					}
					else {
						setStore({auth: false})
					}
					
				}	catch (error) {
					console.log(error); 
				}




			},
 
		


		}
	};

};

export default getState;


