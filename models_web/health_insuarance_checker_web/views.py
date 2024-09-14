from django.shortcuts import render
from joblib import load
from django.http import HttpResponseBadRequest

# Load the model once when the module is loaded
model = load('./savedmodels/model.joblib')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        try:
            # Retrieve data from POST request
            name = request.POST.get('name')
            age = request.POST.get('age')
            height = request.POST.get('height')
            weight = request.POST.get('weight')

            # Validate inputs
            if not (age and height and weight):
                return HttpResponseBadRequest("Missing input values.")

            # Convert to appropriate types
            age = float(age)
            height = float(height)
            weight = float(weight)

            # Predict using the model
            predict = model.predict([[age, height, weight]])

            # Prepare context
            context = {
                'name': name,
                'result': int(predict)  # Assuming `predict` returns an array-like object
            }

            return render(request, 'index.html', context)

        except ValueError:
            return HttpResponseBadRequest("Invalid input values. Please provide numeric values for age, height, and weight.")
        except Exception as e:
            return HttpResponseBadRequest(f"An error occurred: {str(e)}")
