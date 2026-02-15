async function loadProfile() {
  const token = localStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:8000/users/me", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    alert("Not authorized");
    window.location.href = "login.html";
    return;
  }

  const user = await res.json();

  document.getElementById("info").innerText =
    `Welcome ${user.username} (${user.email})`;
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

loadProfile();
