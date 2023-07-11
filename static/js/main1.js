
const resultDiv = document.getElementById('result');
const form = document.getElementById('formValue');

form.addEventListener("submit", function(event) {
  event.preventDefault();

  const quantitySelect = document.querySelector('select[name="quantity"]');
  const mealQuantity = parseInt(quantitySelect.value);

  const calorieInput = document.querySelector('input[name="quantity"]');
  const calorieCount = calorieInput.value;

  resultDiv.innerHTML = ""; // Clear previous results
  
  const title = document.createElement('h3');
  title.textContent = `Today's Meal Plan: (${calorieCount} Kcal)`;
  //or title.textContent = "Today's Meal Plan (" + calorieCount + " Calories)";
  resultDiv.appendChild(title);
  title.style.marginBottom='15px';

  for (let i = 0; i < mealQuantity; i++) {
    const div = document.createElement('div');
div.style.backgroundColor = 'lightblue'; // Set the background color
div.style.padding = '10px'; // Set padding
div.style.marginBottom = '10px'; // Set margin bottom
div.style.display = 'flex'; // Use flexbox to align items
div.style.flexDirection = 'column'; // Stack elements vertically

const mealTitle = document.createElement('h2');
mealTitle.textContent = "Title";
mealTitle.style.marginBottom = '10px';
mealTitle.style.fontSize = '18px';
mealTitle.style.color = 'red';

const imgTextContainer = document.createElement('div');
imgTextContainer.style.display = 'flex';
imgTextContainer.style.alignItems = 'flex-start';

const img = document.createElement('img');
img.src = '{% static "images/almonds.jpg" %}'; // Replace with the actual path to your image
img.style.height = '90%';
img.style.width = '20%';
img.style.borderRadius = '14px';

const text = document.createElement('p');
text.textContent = 'Lorem ipsum dolor';
text.style.marginLeft = '10px';
text.style.cursor = 'pointer'; // Set cursor to pointer on hover

const popup = document.createElement('div');
popup.style.display = 'none'; // Hide the popup initially
popup.style.position = 'absolute';
popup.style.backgroundColor = 'rgba(0, 0, 0, 0.92)'; // Set the background color with transparency
popup.style.color = 'white';
popup.style.padding = '10px';
popup.style.zIndex = '1';
popup.style.height = '140px'; // Set the height of the popup box
//popup.style.width = '90px';

const titleSection = document.createElement('div');
titleSection.style.display = 'flex';
titleSection.style.flexDirection = 'column';

const title = document.createElement('h3');
title.textContent = 'Title';
title.style.marginBottom = '5px';

const description = document.createElement('div');
description.style.display = 'flex';
description.style.flexDirection = 'row';
description.style.marginTop = '10px';

const labelsColumn = document.createElement('div');
labelsColumn.style.display = 'flex';
labelsColumn.style.flexDirection = 'column';
labelsColumn.style.marginRight = '10px';

const valuesColumn = document.createElement('div');
valuesColumn.style.display = 'flex';
valuesColumn.style.flexDirection = 'column';

const caloriesLabel = document.createElement('span');
caloriesLabel.textContent = 'Calories:';

const carbohydratesLabel = document.createElement('span');
carbohydratesLabel.textContent = 'Carbohydrates:';

const proteinLabel = document.createElement('span');
proteinLabel.textContent = 'Protein:';

const fatLabel = document.createElement('span');
fatLabel.textContent = 'Fat:';

const kcalValue = document.createElement('span');
kcalValue.textContent = 'kcal';

const gmValue1 = document.createElement('span');
gmValue1.textContent = 'gm';

const gmValue2 = document.createElement('span');
gmValue2.textContent = 'gm';

const gmValue3 = document.createElement('span');
gmValue3.textContent = 'gm';

labelsColumn.appendChild(caloriesLabel);
labelsColumn.appendChild(carbohydratesLabel);
labelsColumn.appendChild(proteinLabel);
labelsColumn.appendChild(fatLabel);

valuesColumn.appendChild(kcalValue);
valuesColumn.appendChild(gmValue1);
valuesColumn.appendChild(gmValue2);
valuesColumn.appendChild(gmValue3);

description.appendChild(labelsColumn);
description.appendChild(valuesColumn);

titleSection.appendChild(title);
titleSection.appendChild(description);
popup.appendChild(titleSection);

text.addEventListener('mouseenter', () => {
  popup.style.display = 'block'; // Show the popup on mouse enter
});

text.addEventListener('mouseleave', () => {
  popup.style.display = 'none'; // Hide the popup on mouse leave
});

imgTextContainer.appendChild(img);
imgTextContainer.appendChild(text);
div.appendChild(mealTitle);
div.appendChild(imgTextContainer);
div.appendChild(popup);




    resultDiv.appendChild(div);
  }
});
