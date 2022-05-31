import config from "@/config.js";

export async function loadData(id) {
  const settings = {
    methods: "GET",
    headers: {
      Authorization: localStorage.userId,
    },
  };


  let response = await fetch(`${config.API_PATH}/stores/${id}`, settings);
  let loadData = await response.json();

  return loadData;
}
export async function loadItem(id){
    const settings = {
    methods: "GET",
    headers: {
      Authorization: localStorage.userId,
    },
  };
  let response = await fetch(`${config.API_PATH}/items/${id}`, settings);
  let loadItem = await response.json();
  return loadItem
}

export async function sendData(info){
  const settings = {
    method: "POST",
    body: JSON.stringify(info),
    headers: {
      "Content-Type": "application/json",
    },
  };
  let response = await fetch(`${config.API_PATH}/buyingItems`, settings);
  if (response.status == 200){
    alert("Revise su correo, se ha enviado la informacion del vendedor");
  } else {
    alert("EL EMAIL PROPORCIONADO NO ES VALIDO, INTRODUZCA UNO VALIDO")
  }

}
