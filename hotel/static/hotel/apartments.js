document.addEventListener('DOMContentLoaded', () => {


    document.querySelectorAll('.apartment-div').forEach(function(button) {
        button.onclick = function() {
            let id = this.id;
            console.log(`this id: ${id}`);
        
            if (document.getElementById(`div-${id}`).style.display == 'none'){
                console.log('here');
                document.getElementById(`div-${id}`).setAttribute("style", "display: inline-block;");
            } else {
                document.getElementById(`div-${id}`).setAttribute("style", "display: none;");
            };
        
        };
    });

});