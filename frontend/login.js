async function login() {
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  if (!email || !password) {
    alert("Please enter email and password");
    return;
  }

  const formData = new URLSearchParams();
  formData.append("username", email);   // IMPORTANT: must be "username"
  formData.append("password", password);

  try {
    const res = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: formData.toString()
    });

    const data = await res.json();

    if (!res.ok) {
      console.log("LOGIN ERROR:", data);
      alert(data.detail || "Login failed");
      return;
    }

    localStorage.setItem("token", data.access_token);
    window.location.href = "dashboard.html";

  } catch (err) {
    console.error(err);
    alert("Server not reachable");
  }
}
