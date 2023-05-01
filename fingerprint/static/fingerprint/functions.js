// for heading selection

const search = document.querySelector('.input-group input'),
    table_rows= document.querySelectorAll('tbody tr');

    search.addEventListener('input', searchTable);


    function searchTable(){
      table_rows.forEach((row, i)=>{
        let table_data= row.textContent,
            search_data = search.value.toLowerCase;

        row.classList.toggle('hide',table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay' , i/5 + 's');
      })
    }









const table = document.getElementById('myTable');

// Get the table header row
const th = table.querySelectorAll('th');
for (let c=0; c<th.length;c++){
    th[c].addEventListener('click', item(c))
}

function item(c){
    return function(){
        console.log(c)
        sortTable(c)
    }
}


// this below code is copied from w3school if you've 
// any confusion check it on the site
function sortTable(c) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("myTable");
    switching = true;
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
      // Start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /* Loop through all table rows (except the
      first, which contains table headers): */
      for (i = 1; i < (rows.length - 1); i++) {
        // Start by saying there should be no switching:
        shouldSwitch = false;
        /* Get the two elements you want to compare,
        one from current row and one from the next: */
        x = rows[i].getElementsByTagName("TD")[c];
        y = rows[i + 1].getElementsByTagName("TD")[c];
        // Check if the two rows should switch place:
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark that a switch has been done: */
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }
  }