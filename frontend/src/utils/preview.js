import { getBlockTypes } from "@/utils/blockTypes";

const maxLength = 50;

export function getPreview(block) {
  const blockModel = getBlockTypes().find(
    b => block.block_type == b.block_type
  );
  if (blockModel.block_type == "text") {
    return getTextBlockPreview(block);
  } else if (blockModel.block_type == "image") {
    return getImageBlockPreview(block);
  }
  return `${blockModel.label} Block`;
}

function getTextBlockPreview(block) {
  if (!block.value || !block.value.text || block.value.text.length < 1) {
    return "Text Block";
  }
  let value = stripHTML(block.value.text);
  const continued = value.length > maxLength ? "..." : "";
  return `Text Block: ${value.slice(0, maxLength)}${continued}`;
}

function getImageBlockPreview(block) {
  if (!block.value || !block.value.image || !block.value.image.filename)
    return "Image Block";
  const preview = block.value.image.filename;
  return `Image Block: ${preview}`;
}

function stripHTML(text) {
  const regex = /(<([^>]+)>)/gi;
  return text.replace(regex, "");
}
