import React, {useEffect, useState} from "react";
import {fetchCustomers} from "../api";

export default function CustomerList() {
  const [customers, setCustomers] = useState([]);
  useEffect(() => {
    fetchCustomers().then(setCustomers);
  }, []);
  return (
    <div>
      <h2>Nigerian Customers</h2>
      <ul>
        {customers.map(c => (
          <li key={c.id}>{c.name} ({c.email}, {c.phone})</li>
        ))}
      </ul>
    </div>
  );
}