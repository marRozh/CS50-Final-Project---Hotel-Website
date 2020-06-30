document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('open-calendar').onclick = function() {
        document.getElementById('calendar').setAttribute("style", "display: block;");
        document.getElementById('open-calendar').style.display = 'none';

        let bookings = document.getElementById('calendar-data').innerHTML;
        for (let i = 0; i < bookings.length; i++) {
            bookings = bookings.replace('&#x27;', '');
            bookings = bookings.replace(' ', '');
            bookings = bookings.replace('[', '');
            bookings = bookings.replace(']', '');
        };

        let bookings_array = bookings.split(',');
        console.log(`bookings: ${bookings}`);
        console.log(`bookings_array: ${bookings_array}`);

        if (bookings_array.length > 0) {
            for (let i = 0; i < bookings_array.length; i += 2) {
                let date = bookings_array[i];
                document.getElementById(bookings_array[i]).style.backgroundColor = '#F25F5C';
                let days = bookings_array[i + 1];
                for (let i = 1; i < days; i++) {
                    let date_split = date.split('-');
                    let last;
                    if (date_split[2][0] == 0) {
                        last = '0' + (parseInt(date_split[2]) + i);
                    } else {
                        last = parseInt(date_split[2]) + i;
                    };
                    date_split[2] = last;
                    let new_date = date_split.join('-');

                    document.getElementById(new_date).style.backgroundColor = '#F25F5C';
                };
            };
        };

    };

    document.getElementById('move-down').onclick = function() {
        let months = ['july2020', 'august2020', 'september2020'];
        for (let i = 1; i < months.length; i++) {
            if (document.getElementById(months[i]).style.display == 'block') {
                document.getElementById(months[i]).setAttribute("style", "display: none;");
                document.getElementById(months[i - 1]).setAttribute("style", "display: block;");
                break;
            };
        };
    };

    document.getElementById('move-up').onclick = function() {
        let months = ['july2020', 'august2020', 'september2020'];
        for (let i = 0; i < months.length - 1; i++) {
            if (document.getElementById(months[i]).style.display == 'block') {
                document.getElementById(months[i]).setAttribute("style", "display: none;");
                document.getElementById(months[i + 1]).setAttribute("style", "display: block;");
                break;
            };
        };
    };

    document.getElementById('book-form-check-in-input').onclick = () => {
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
        document.getElementById('book-form-check-in-input').setAttribute('min', today);
    };

    document.getElementById('book-form-check-out-input').onclick = () => {
        let choice = document.getElementById('book-form-check-in-input').value;
        document.getElementById('book-form-check-out-input').setAttribute('min', choice);
    };

});