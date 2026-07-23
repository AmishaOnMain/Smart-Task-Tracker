import { GoogleLogin } from "@react-oauth/google";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import type { CredentialResponse } from "@react-oauth/google";

function Login() {
  const navigate = useNavigate();

  const handleSuccess = async (
    credentialResponse: CredentialResponse
) => {
    if (!credentialResponse.credential) {
        alert("Google login failed.");
        return;
    }

    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/auth/google",
            {
                id_token: credentialResponse.credential,
            }
        );

        localStorage.setItem(
            "token",
            response.data.access_token
        );

        navigate("/dashboard");
    } catch (error) {
        console.error(error);
        alert("Login failed");
    }
};

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <div className="bg-white rounded-xl shadow-lg p-10 w-[400px]">
        <h1 className="text-3xl font-bold mb-2">AI Productivity Dashboard</h1>

        <p className="text-gray-500 mb-8">Sign in to continue</p>

        <GoogleLogin
          onSuccess={handleSuccess}
          onError={() => alert("Login Failed")}
        />
      </div>
    </div>
  );
}

export default Login;
