import { useEffect, useState } from "react";

import Layout from "../components/layout/Layout";
import { getTasks } from "../services/taskService";

function Tasks() {

    const [tasks, setTasks] = useState([]);

    useEffect(() => {

        getTasks()
            .then(setTasks)
            .catch(console.error);

    }, []);

    return (

        <Layout>

            <h1 className="text-3xl font-bold mb-6">
                Tasks
            </h1>

            <pre>

                {JSON.stringify(tasks, null, 2)}

            </pre>

        </Layout>

    );

}

export default Tasks;