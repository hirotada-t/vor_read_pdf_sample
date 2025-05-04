document.getElementById("send").onclick = async () => {
  const input = document.getElementById("input").value;
  console.log(input)
  const res = await fetch(`/api/echo?message=${encodeURIComponent(input)}`);
  const data = await res.json();
  console.log(data)
  document.getElementById("response").textContent = `Response: ${data.message}`;
};
