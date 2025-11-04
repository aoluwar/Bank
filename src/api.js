const API_URL = "http://localhost:8000";

export async function fetchCustomers() {
  const res = await fetch(`${API_URL}/customers`);
  return res.json();
}

export async function createCustomer(customer) {
  await fetch(`${API_URL}/customers`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(customer)
  });
}