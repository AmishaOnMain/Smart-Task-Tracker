import { Link, useLocation } from "react-router-dom";

const links = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "Tasks", path: "/tasks" },
  { name: "Calendar", path: "/calendar" },
  { name: "Settings", path: "/settings" },
];

function Sidebar() {
  const location = useLocation();

  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen p-6">
      <h1 className="text-2xl font-bold mb-8">
        Productivity
      </h1>

      <nav className="space-y-2">
        {links.map((link) => (
          <Link
            key={link.path}
            to={link.path}
            className={`block rounded-lg px-4 py-2 ${
              location.pathname === link.path
                ? "bg-blue-600"
                : "hover:bg-slate-800"
            }`}
          >
            {link.name}
          </Link>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;