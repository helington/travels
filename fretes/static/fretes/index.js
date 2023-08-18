document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#all').addEventListener('click', () => {
        load_freights()
    });
    document.querySelector('#add').addEventListener('click', () => {
        compose_freight()
    });

    load_freights();
})

function load_freights() {
    document.querySelector('#freights-view').style.display = 'block';
    document.querySelector('#compose-freight-view').style.display = 'none';

    fetch('/freights/all')
    .then(respose => respose.json())
    .then(freights => {
        console.log(freights)
    })
}

function compose_freight() {
    document.querySelector('#freights-view').style.display = 'none';
    document.querySelector('#compose-freight-view').style.display = 'block';
}