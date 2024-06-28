import gradio as gr
import spacy

# Load spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Function to determine personality traits based on pet name and type
def determine_personality_traits(pet_name, pet_type):
    # Perform NLP processing on the pet name
    doc = nlp(pet_name.lower())
    
    # Example logic based on pet type (replace with your own analysis)
    if pet_type.lower() == "bird":
        personality_traits = "Based on the name {}, you exhibit traits commonly associated with bird owners, such as being observant and detail-oriented."
    elif pet_type.lower() == "domestic animal":
        personality_traits = "Your {}'s name suggests traits like loyalty and warmth often found in owners of domestic animals."
    elif pet_type.lower() == "mammal":
        personality_traits = "The name {} indicates characteristics typically seen in owners of mammals, such as nurturing and sociability."
    elif pet_type.lower() == "wild animal":
        personality_traits = "Owners of wild animals like {} often display traits such as adventurousness and independence."
    else:
        personality_traits = "Unable to determine personality traits based on the provided information."
    
    return personality_traits.format(pet_name)

# Define the interface using Gradio
iface = gr.Interface(
    fn=determine_personality_traits,
    inputs=[
        gr.Textbox(lines=1, label="Enter your pet's name"),
        gr.Radio(["Bird", "Domestic Animal", "Mammal", "Wild Animal"], label="Select the type of pet")
    ],
    outputs=gr.Textbox(label="Personality Traits Assessment"),
    title="Pet Type and Name Personality Traits Analyzer",
    description="Enter your pet's name and select its type to discover your personality traits!"
)
