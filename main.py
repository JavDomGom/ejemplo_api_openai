import openai

openai.api_key = '<PUT_HERE_YOUR_OPENAI_API_KEY>'

response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {
            'role': 'system',
            'content': 'Eres un asistente útil que responde con seriedad y ciñéndote estrictamente a la pregunta.'
        },
        {
            'role': 'user',
            'content': f'''
            Tienes la siguiente lista de cadenas de texto:
            
            aaa
            bbb
            ccc
            
            ¿Cuál dirías que viene continuación?
            '''
        }
    ],

)

print(response.get('choices')[0].get('message').get('content'))