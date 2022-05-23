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
