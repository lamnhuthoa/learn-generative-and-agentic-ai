document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('todo-form');
    const input = document.getElementById('todo-input');
    const list = document.getElementById('todo-list');

    form.addEventListener('submit', e => {
        e.preventDefault();
        const text = input.value.trim();
        if (!text) return;
        addTodo(text);
        input.value = '';
    });

    function addTodo(text) {
        const li = document.createElement('li');
        li.textContent = text;
        li.addEventListener('click', () => {
            li.classList.toggle('done');
        });
        const delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.className = 'delete-btn';
        delBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            li.remove();
        });
        li.appendChild(delBtn);
        list.appendChild(li);
    }
});
