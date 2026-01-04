const notesList = document.getElementById('notesList');
const noteInput = document.getElementById('noteInput');

async function fetchNotes() {
    const res = await fetch('/notes');
    const data = await res.json();
    notesList.innerHTML = '';
    data.forEach(note => {
        const li = document.createElement('li');
        li.textContent = note;
        notesList.appendChild(li);
    });
}

async function addNote() {
    const note = noteInput.value.trim();
    if (!note) return;
    await fetch('/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ note })
    });
    noteInput.value = '';
    fetchNotes();
}

window.onload = fetchNotes;
