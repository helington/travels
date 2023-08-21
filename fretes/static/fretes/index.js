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
    
    const all_freights = document.querySelector('#freights')
    all_freights.innerHTML = ''

    fetch('/freights/all')
    .then(respose => respose.json())
    .then(freights_per_month => {
        freights_per_month.forEach(freight_per_month => {

            const month = document.createElement('h2')
            month.innerHTML = freight_per_month.month

            all_freights.append(month)
            console.log(freight_per_month.month)
            const freights = document.createElement('ul')
            freight_per_month.freights.forEach(freight => {
                const row = document.createElement('li')
                row.innerHTML = `<strong>${freight.date}:</strong> ${freight.title}`

                const edit_button = document.createElement('button')
                edit_button.className = 'btn btn-link'
                edit_button.innerHTML = 'edit'
                edit_button.addEventListener('click', () => {
                    compose_freight(freight.id)
                })

                row.append(edit_button)

                freights.append(row)
            })
            all_freights.append(freights)
        })
    })
}

function compose_freight(freight_id=null) {
    document.querySelector('#freights-view').style.display = 'none';
    document.querySelector('#compose-freight-view').style.display = 'block';

    const title = document.querySelector('#title')
    const date = document.querySelector('#date')

    title.value = ''
    date.value = ''
    const remove_button = document.querySelector('#remove-freight-button')
    if (remove_button) {
        remove_button.remove()
    }

    if (freight_id !== null) {
        fetch(`/freights/${freight_id}`)
        .then(response => response.json())
        .then(freight => {
            title.value = freight.title
            date.value = freight.date_for_html_input

            const remove_freight_button = document.createElement('button')
            remove_freight_button.type = 'button'
            remove_freight_button.id = 'remove-freight-button'
            remove_freight_button.innerHTML = 'Remove'
            remove_freight_button.className = 'btn btn-danger'
            remove_freight_button.addEventListener('click', () => {
                remove_freight(freight_id)
                location.reload()
            } )
            
            document.querySelector('.formButtons').append(remove_freight_button)
        })
    }

    document.querySelector('#compose-freight-form').onsubmit = () => {
        if (freight_id === null) {
            fetch('/freights', {
                method: 'POST',
                body: JSON.stringify({
                    title: title.value,
                    date: date.value
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log(result)
            })
        }
        else {
            fetch(`/freights/${freight_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    title: title.value,
                    date: date.value
                })
            })
        }
    }
}

function remove_freight(freight_id) {
    fetch(`/freights/${freight_id}`, {
        method: "DELETE"
    })
}