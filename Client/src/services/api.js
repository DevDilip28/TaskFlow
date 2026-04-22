const Base_URL = "http://127.0.0.1:8000";

const get_token = () => localStorage.getItem("token");

export const registerUser = async (data) => {
  const res = await fetch(`${Base_URL}/user/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    throw new Error("Failed to register user");
  }
  return res.json();
};

export const loginUser = async (data) => {
  const res = await fetch(`${Base_URL}/user/login`, {
    method: "POST",
    headers: {
      "content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    throw new Error("Failed to login user");
  }
  return res.json();
};

export const createTask = async (data) => {
  const res = await fetch(`${Base_URL}/task/create`, {
    method: "POST",
    headers: {
      "content-Type": "application/json",
      Authorization: `Bearer ${get_token()}`,
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    throw new Error("Failed to create task");
  }
  return res.json();
};

export const getTask = async () => {
  const res = await fetch(`${Base_URL}/task/all_tasks`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${get_token()}`,
    },
  });
  if (!res.ok) {
    throw new Error("Failed to fetch tasks");
  }
  return res.json();
};

export const deleteTask = async (id) => {
  const res = await fetch(`${Base_URL}/task/delete/id_${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${get_token()}`,
    },
  });
  if (!res.ok) {
    throw new Error("Failed to delete task");
  }
};
