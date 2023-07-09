document.getElementById("calculatorForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Retrieve user inputs
    var age = parseInt(document.getElementById("age").value);
    var gender = document.getElementById("gender").value;
    var height = parseInt(document.getElementById("height").value);
    var weight = parseInt(document.getElementById("weight").value);
    var activityLevel = parseFloat(document.getElementById("activity").value);
    var goal = document.getElementById("goal").value;
  
    // Calculate BMR (Basal Metabolic Rate)
    var bmr;
    if (gender === "male") {
      bmr = 10 * weight + 6.25 * height - 5 * age + 5;
    } else {
      bmr = 10 * weight + 6.25 * height - 5 * age - 161;
    }
    bmr = bmr.toFixed(0);
  
    // Calculate daily calorie intake
    var calorieIntake = calculateCalorieIntake(bmr, activityLevel);
  
    // Adjust calorie intake based on goal
    var goalCalorieAdjustment = 0;
    if (goal === "muscle_gain") {
      goalCalorieAdjustment = 250; // Add 250 calories for muscle gain
    } else if (goal === "fat_loss") {
      goalCalorieAdjustment = -250; // Subtract 250 calories for fat loss
    }
    var adjustedCalorieIntake = calorieIntake + goalCalorieAdjustment;
    
  
    // Calculate macronutrient intake based on adjusted calorie intake
    var carbsMin, carbsMax, proteinMin, proteinMax, fatMin, fatMax;
  
    if (goal === "muscle_gain") {
      carbsMin = Math.round(0.40 * adjustedCalorieIntake / 4);
      carbsMax = Math.round(0.50 * adjustedCalorieIntake / 4);
      proteinMin = Math.round(0.25 * adjustedCalorieIntake / 4);
      proteinMax = Math.round(0.35 * adjustedCalorieIntake / 4);
      fatMin = Math.round(0.20 * adjustedCalorieIntake / 9);
      fatMax = Math.round(0.30 * adjustedCalorieIntake / 9);
    } else if (goal === "fat_loss") {
      carbsMin = Math.round(0.30 * adjustedCalorieIntake / 4);
      carbsMax = Math.round(0.40 * adjustedCalorieIntake / 4);
      proteinMin = Math.round(0.30 * adjustedCalorieIntake / 4);
      proteinMax = Math.round(0.40 * adjustedCalorieIntake / 4);
      fatMin = Math.round(0.20 * adjustedCalorieIntake / 9);
      fatMax = Math.round(0.30 * adjustedCalorieIntake / 9);
    } else {
      // General maintenance
      carbsMin = Math.round(0.45 * adjustedCalorieIntake / 4);
      carbsMax = Math.round(0.65 * adjustedCalorieIntake / 4);
      proteinMin = Math.round(0.10 * adjustedCalorieIntake / 4);
      proteinMax = Math.round(0.35 * adjustedCalorieIntake / 4);
      fatMin = Math.round(0.20 * adjustedCalorieIntake / 9);
      fatMax = Math.round(0.35 * adjustedCalorieIntake / 9);
    }
  
    // Display the results
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML =
      "<strong>BMR:</strong> " +
      bmr +
      " calories" +
      "<br><strong>Daily Maintain calorie:</strong> " +
      calorieIntake +
      " calories" +
      (goalCalorieAdjustment !== 0
        ? "<br><strong>Daily " +
          (goalCalorieAdjustment > 0 ? "Added" : "Reduced") +
          " Calories:</strong> " +
          Math.abs(goalCalorieAdjustment) +
          " calories"
        : "") +
      "<br><strong>Net Calorie intake:</strong>" +
       adjustedCalorieIntake +
  
  
      "<br><strong>Goal:</strong> " +
      goal +
      "<br><strong>Carbohydrates:</strong> " +
      carbsMin +
      "-" +
      carbsMax +
      " grams" +
      "<br><strong>Protein:</strong> " +
      proteinMin +
      "-" +
      proteinMax +
      " grams" +
      "<br><strong>Fat:</strong> " +
      fatMin +
      "-" +
      fatMax +
      " grams";
  });
  
  function calculateCalorieIntake(bmr, activityLevel) {
    return Math.round(bmr * activityLevel);
  }
  