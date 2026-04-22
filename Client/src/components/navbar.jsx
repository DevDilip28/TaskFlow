import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div className="bg-white border-b">
      <div className="max-w-4xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1
          onClick={() => navigate("/")}
          className="text-lg font-semibold text-blue-600 cursor-pointer"
        >
          TaskFlow
        </h1>

        <button
          onClick={logout}
          className="text-sm bg-slate-100 hover:bg-slate-200 px-4 py-2 rounded-lg"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
