// メッセージ送信
document.getElementById("send").onclick = async () => {
  const input = document.getElementById("input").value;
  const res = await fetch(`/api/echo?message=${encodeURIComponent(input)}`);
  const data = await res.json();
  document.getElementById("response").textContent = `Response: ${data.message}`;
};

// 画像アップロード & OCR
document.getElementById("upload").onclick = async () => {
  const fileInput = document.getElementById("imageInput");
  if (fileInput.files.length === 0) {
    alert("画像を選択してください");
    return;
  }
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch("/api/upload", {
    method: "POST",
    body: formData
  });
  const data = await res.json();

  // テキスト表示
  document.getElementById("ocrResult").textContent = data.text;
  // CSVダウンロードリンク
  const link = document.createElement("a");
  link.href = `/${data.csv_path}`;
  link.textContent = "CSVをダウンロード";
  document.getElementById("csvLink").innerHTML = "";
  document.getElementById("csvLink").appendChild(link);
};