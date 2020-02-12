export function buildImageData(value) {
  const urlParts = window.location.pathname.split("/");
  let data = new FormData();
  data.append("uploaded_file", value);
  data.append("object_id", urlParts[4]);
  data.append("model_name", `${urlParts[2]}.${urlParts[3]}`);
  return data;
}
