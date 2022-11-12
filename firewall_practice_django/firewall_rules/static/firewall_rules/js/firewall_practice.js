function new_row(interface, direction, source_address, destination_address, port_number, action, description) {
    var table = document.getElementById("myTable");
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
    var cell7 = row.insertCell(6);
    
    cell1.innerHTML = interface;
    cell2.innerHTML = direction;
    cell3.innerHTML = source_address;
    cell4.innerHTML = destination_address;
    cell5.innerHTML = port_number;
    cell6.innerHTML = action;
    cell7.innerHTML = description;
  }

      
  $('#firewall_rules_submit').click(function(){
    //e.preventDefault();
    $("#result").load("output/firewall_rules");
    //$.ajax({
    //  method: "GET",
    //  url: "output/firewall_rules",
    //}); 
  })