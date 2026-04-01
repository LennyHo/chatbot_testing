"""
Logic for generating responses based on NLP output.
"""
def generate_response(nlp_result):
    # For now, just return the text field
    return nlp_result.get('text', 'Sorry, I did not understand that.')
