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
export async function loadItem(id) {
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

export async function sendData(info) {
  const settings = {
    method: "POST",
    body: JSON.stringify(info),
    headers: {
      "Content-Type": "application/json",
    },
  };
  let response = await fetch(`${config.API_PATH}/buyingItems`, settings);
  if (response.status == 200) {
    alert("Revise su correo, se ha enviado la informacion del vendedor");
  } else {
    alert("EL EMAIL PROPORCIONADO NO ES VALIDO, INTRODUZCA UNO VALIDO")
  }

}
export async function adminLogin(info) {
  const settings = {
    method: "POST",
    body: JSON.stringify(info),
    headers: {
      "Content-Type": "application/json",
    },
  };
  let response = await fetch(`${config.API_PATH}/adminLogin`, settings);


  if (response.status == 200) {
    localStorage.setItem('autorizacion', JSON.stringify(await response.json()));
    alert("Se ha logeado correctamente ya puede acceder al menu admin de su tienda ")
  } else {
    alert("NO SE A PODIDO ACCEDER CON SUS DATOS, REVISE SUS DATOS")
  }
}

export async function modifyStore(store, store_id) {
  const settings = {
    method: "PUT",
    body: JSON.stringify(store, store_id),
    headers: {
      "Content-Type": "application/json",
    },
  };
  await fetch(
    `${config.API_PATH}/storeModify/${store_id}`,
    settings
  );

}
export async function modifyItem(item, item_id) {
  const settings = {
    method: "PUT",
    body: JSON.stringify(item, item_id),
    headers: {
      "Content-Type": "application/json",
    },
  };
  await fetch(
    `${config.API_PATH}/itemModify/${item_id}`,
    settings
  );

}

export async function addItem(item, store_id) {
  const settings = {
    method: "POST",
    body: JSON.stringify(item, store_id),
    headers: {
      "Content-Type": "application/json",
    },
  };
  await fetch(
    `${config.API_PATH}/addItem/${store_id}`,
    settings
  );
}
