const dropdown_extension = document.getElementById("extension_list");
const dropdown_format = document.getElementById("format_list");
updateGraph();

dropdown_extension.addEventListener("change", updateGraph);
dropdown_format.addEventListener("change", updateGraph);

function updateGraph() {

    const format = dropdown_format.value;
    const extension = dropdown_extension.value;

    $.ajax({
      type: "POST",
      url: "/update_graph",
      data: {
        format: format,
        extension: extension
            },
      success: function(response) {
        updateGraphWithData(response);
    }
      
    });
  }

function toggleElementById (toggle, id) {
    element = document.getElementById(id)
    if (toggle) {
        element.classList.remove('d-none');
        element.classList.add('d-block');
      } else {
        element.classList.remove('d-block');
        element.classList.add('d-none');
      }
}
  
function updateGraphWithData(graphJSON) {
    console.log(graphJSON)

    if (graphJSON === "df is empty") {
        toggleElementById(true, 'no_data_message');
        toggleElementById(false, 'chart');
        
    } else {
        toggleElementById(false, 'no_data_message');
        toggleElementById(true, 'chart');
        let graphs = JSON.parse(graphJSON);
        plot = Plotly.newPlot('chart', graphs, {}); 
    }
    

  }
