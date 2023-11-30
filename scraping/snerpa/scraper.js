const fs = require("fs/promises");

const read_local = async (file) => {
  const data = await fs.readFile(file, { encoding: "utf8" });
  return data;
};

const scrape = async (url) => {
  const res = await fetch(url);
  const body = await res.text();
  return body;
};

const main = async () => {
  const urls = await JSON.parse(await read_local("./snerpa_links.json"));
	const parser = new DOMParser();
  const data = parser.parseFromString(
    await scrape(urls[0]),
    "text/html"
  );
  console.log(data.querySelector(".article").innerText);
};

main();
