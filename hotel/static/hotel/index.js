document.addEventListener('DOMContentLoaded', () => {



    document.getElementById('search-check-in-input').onclick = () => {
        let today = new Date();
        let dd = today.getDate();
        let mm = today.getMonth()+1;
        let yyyy = today.getFullYear();

        if (dd < 10) {
            dd = '0' + dd;
        };
        if (mm < 10) {
            mm = '0' + mm;
        };
        today = yyyy + '-' + mm + '-' + dd;
        document.getElementById('search-check-in-input').setAttribute('min', today);
    };

    document.getElementById('search-check-out-input').onclick = () => {
        let choice = document.getElementById('search-check-in-input').value;
        document.getElementById('search-check-out-input').setAttribute('min', choice);
    };




});