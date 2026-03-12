const taskForm = document.getElementById("task-form");
const taskList = document.getElementById("task-list");
const titleInput = document.getElementById("title");
const descriptionInput = document.getElementById("description");

async function fetchTasks() {
  const response = await fetch(`${window.API_BASE_URL}/tasks`);
  const tasks = await response.json();
  taskList.innerHTML = "";

  tasks.forEach((task) => {
    const li = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done;
    checkbox.addEventListener("change", async () => {
      await fetch(`${window.API_BASE_URL}/tasks/${task.id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ done: checkbox.checked }),
      });
      fetchTasks();
    });

    const title = document.createElement("span");
    title.textContent = task.description
      ? `${task.title} — ${task.description}`
      : task.title;
    if (task.done) {
      title.classList.add("done");
    }

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", async () => {
      await fetch(`${window.API_BASE_URL}/tasks/${task.id}`, {
        method: "DELETE",
      });
      fetchTasks();
    });

    li.appendChild(checkbox);
    li.appendChild(title);
    li.appendChild(deleteButton);
    taskList.appendChild(li);
  });
}

taskForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  await fetch(`${window.API_BASE_URL}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: titleInput.value,
      description: descriptionInput.value || null,
      done: false,
    }),
  });

  taskForm.reset();
  fetchTasks();
});

fetchTasks();
