
function matched() {
let input, filter, table, tr, td, i, txtValue;
input = document.getElementById("tbSearch");
filter = input.value.toUpperCase();
table = document.querySelector(".table");
tr = table.getElementsByTagName("tr");

// Loop through all table rows and hide those that don't match the search query
for (i = 0; i < tr.length; i++) {
  td = tr[i].getElementsByTagName("td")[1]; // Change the index to match the column you want to search (e.g., 1 for firstname, 4 for username, etc.)
  if (td) {
    txtValue = td.textContent || td.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      tr[i].style.display = "";
    } else {
      tr[i].style.display = "none";
    }
  }
}
}

// Add an event listener to call the matched() function whenever the input text changes
document.getElementById("tbSearch").addEventListener("input", matched);
