import { useEffect, useState } from "react";
import { getTask, createTask, deleteTask } from "../services/api";
import Navbar from "../components/navbar";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [form, setForm] = useState({
    title: "",
    description: "",
    is_completed: false,
  });

  const loadTasks = async () => {
    const data = await getTask();
    setTasks(data);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const handleCreate = async () => {
    if (!form.title) return;
    await createTask(form);
    setForm({ title: "", description: "" });
    loadTasks();
  };

  const handleDelete = async (id) => {
    await deleteTask(id);
    loadTasks();
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />

      <div className="max-w-2xl mx-auto px-4 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-semibold text-slate-800">Your Tasks</h1>
          <p className="text-sm text-slate-500">
            Stay organized and productive
          </p>
        </div>

        <div className="bg-white border rounded-2xl p-5 shadow-sm mb-6 space-y-3">
          <input
            className="w-full p-3 border rounded-xl focus:ring-2 focus:ring-blue-500"
            placeholder="Task title"
            value={form.title}
            onChange={(e) => setForm({ ...form, title: e.target.value })}
          />

          <input
            className="w-full p-3 border rounded-xl focus:ring-2 focus:ring-blue-500"
            placeholder="Description"
            value={form.description}
            onChange={(e) => setForm({ ...form, description: e.target.value })}
          />

          <button
            onClick={handleCreate}
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-xl"
          >
            Add Task
          </button>
        </div>

        <div className="space-y-3">
          {tasks.map((task) => (
            <div
              key={task.id}
              className="bg-white border rounded-2xl p-4 shadow-sm flex justify-between items-center"
            >
              <div>
                <h3 className="font-medium text-slate-800">{task.title}</h3>
                <p className="text-sm text-slate-500">{task.description}</p>
              </div>

              <button
                onClick={() => handleDelete(task.id)}
                className="text-sm bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-lg"
              >
                Delete
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
