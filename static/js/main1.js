//console.log("hello")
const resultDiv = document.getElementById('result');
//console.log(resultDiv)
    const element = document.querySelector('#formValue').addEventListener("submit",function(event){
      event.preventDefault();
      const value = generateValue();
      const elementValue = document.createElement('p')
      elementValue.textContent = value;
      //console.log(elementValue)
      resultDiv.appendChild(elementValue)

      
    })
    
   
    
    
    // Add event listener to the button
   // addButton.addEventListener('click', function(){
    
      // Generate the dynamically added value
      //const value = generateValue();
      //console.log(value)
    
      // Create a new element to hold the value
      //const valueElement = document.createElement('p');
      //valueElement.textContent = value;
     
    
      // Append the value element to the result div
      //resultDiv.appendChild(valueElement);
    //});
    
    // Function to generate the value dynamically
    function generateValue() {
      // Generate the value based on your requirements
      // For example, generate a random number
      const randomValue = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo ut laudantium, ea voluptates cum porro dignissimos dolore aperiam quas perspiciatis!"
      return randomValue;
    }