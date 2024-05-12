from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from g4f.client import Client
import markdown

@csrf_exempt
def chat_with_bot_api(request):
    if request.method == 'POST':
        user_query = request.POST.get('user_query', '')
        
        datas = """
        {
            "userAddress": "0x123456789abcdeffedcba9876543210abcd1234",
            "ipfsHash": "QmR7Gi8hjM6A9smJH5ueRbSGRi4T3Aoe3aXjTeZZawPY47",
            "loanAmount": 15000,
            "loanDate": "2024-05-12",
            "reason": "Purchase of new tractor",
            "farmerName": "John Doe",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "fileDocument": "QmP7Vth67jxhSGRj5GT4JnEwo3976jsRkSVxrHPG6979ks",
            "previousLoanHistory": 90,  // Percentage of previous loans repaid on time
            "existingDebt": 3000,
            "annualIncome": 50000,
            "landOwnership": "Owned",
            "farmSize": 120,  // in acres
            "typeOfAgriculture": "Crop",
            "cropInsurance": true
        }"""

        client = Client()

        # Create a chat completion with the user's query
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "System", "content": "you are a useful ai to analyze the risk, possibility of managements and loan based on given json data if it good Approve or decline."},
                {"role": "user", "content": user_query + "give me the output in the json format like {'LoneStatus':Approve or not based on given data, 'generated report':'give me the report why the approve approved or declined. what the advantages or disadvantages''}.Note: dont give any other instructions and ack i just need the json structure output."}
                ]
        )
        ai_response = chat_completion.choices[0].message.content or ""
        print(ai_response)

        # Return the AI's response as JSON
        return JsonResponse({"ai_response": markdown.markdown(ai_response)})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
