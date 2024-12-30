import streamlit as st
import openai
from openai import OpenAI
import json
from geopy.geocoders import Nominatim
from geopy.distance import distance
import uuid
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # Load API key from environment variable

###############################################################################
# Location Processing Function
###############################################################################
def locate_and_offset(
    photo_filename: Optional[str] = None,
    location_text: Optional[str] = None,
    offset_miles: Optional[float] = None,
    offset_direction: Optional[str] = None
) -> dict:
    """Process location from photo/text and compute optional offset."""
    geolocator = Nominatim(user_agent="streamlit-location-app")
    
    result = {
        "photo_filename": photo_filename,
        "found_location": None,
        "found_latitude": None,
        "found_longitude": None,
        "offset_applied": False,
        "offset_bearing_degrees": None,
        "offset_miles": None,
        "offset_latitude": None,
        "offset_longitude": None,
        "error": None
    }

    # Try to determine location
    if location_text:
        loc = geolocator.geocode(location_text)
        if loc:
            result.update({
                "found_location": loc.address,
                "found_latitude": loc.latitude,
                "found_longitude": loc.longitude
            })
        else:
            result["error"] = f"Could not geocode: {location_text}"
            return result
    elif photo_filename:
        # For demo, we'll use a fixed location when photo is provided
        loc = geolocator.geocode("Statue of Liberty")
        if loc:
            result.update({
                "found_location": f"Demo location from photo {photo_filename}",
                "found_latitude": loc.latitude,
                "found_longitude": loc.longitude
            })
        else:
            result["error"] = "Could not process photo location"
            return result
    else:
        result["error"] = "No location input provided"
        return result

    # Process offset if requested
    if offset_miles and offset_direction:
        direction_map = {
            "north": 0.0, "east": 90.0,
            "south": 180.0, "west": 270.0,
            # Add more directions as needed
        }
        bearing = direction_map.get(offset_direction.lower())
        if bearing is None:
            result["error"] = f"Invalid direction: {offset_direction}"
            return result

        # Calculate new point
        origin = (result["found_latitude"], result["found_longitude"])
        dist_obj = distance(miles=offset_miles)
        new_point = dist_obj.destination(point=origin, bearing=bearing)
        
        result.update({
            "offset_applied": True,
            "offset_bearing_degrees": bearing,
            "offset_miles": offset_miles,
            "offset_latitude": new_point.latitude,
            "offset_longitude": new_point.longitude
        })

    return result

###############################################################################
# Function Schema for GPT
###############################################################################
LOCATION_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "locate_and_offset",
        "description": "Process a location from photo/text and compute optional offset",
        "parameters": {
            "type": "object",
            "properties": {
                "photo_filename": {
                    "type": "string",
                    "description": "Name of uploaded photo file (if any)"
                },
                "location_text": {
                    "type": "string",
                    "description": "Text description of location"
                },
                "offset_miles": {
                    "type": "number",
                    "description": "Distance in miles to offset from location"
                },
                "offset_direction": {
                    "type": "string",
                    "description": "Cardinal direction (north, south, east, west)"
                }
            },
            "required": []
        }
    }
}

###############################################################################
# Streamlit App
###############################################################################
def main():
    st.title("Location Assistant")
    st.write("Upload a photo and/or describe a location. You can also ask about offsets!")

    # File upload and text input
    uploaded_file = st.file_uploader("Upload an image (optional)", type=["jpg", "png", "jpeg"])
    user_input = st.text_input("Describe a location or ask about an offset:")

    if st.button("Process"):
        with st.spinner("Processing..."):
            # Save uploaded file if present
            photo_filename = None
            if uploaded_file:
                unique_id = str(uuid.uuid4())[:8]
                photo_filename = f"uploaded_{unique_id}_{uploaded_file.name}"
                with open(photo_filename, "wb") as f:
                    f.write(uploaded_file.read())

            # Prepare conversation for LLM
            messages = [
                {"role": "system", "content": """You are a helpful location assistant. 
                When users provide a location (via text or photo) and optionally request
                an offset, use the locate_and_offset function to process their request.
                Parse their input carefully for location names and any mention of 
                distances/directions."""},
                {"role": "user", "content": user_input}
            ]

            try:
                # Get LLM's interpretation of the request
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    tools=[LOCATION_TOOL_SCHEMA],
                    tool_choice="auto"
                )

                # Process LLM's response
                message = response.choices[0].message
                
                if message.tool_calls:
                    # LLM wants to call our function
                    tool_call = message.tool_calls[0]
                    function_args = json.loads(tool_call.function.arguments)
                    
                    # Add the photo filename if we have one
                    if photo_filename:
                        function_args['photo_filename'] = photo_filename
                    
                    # Call our function with the interpreted arguments
                    result = locate_and_offset(**function_args)
                    
                    # Display results
                    if result.get("error"):
                        st.error(result["error"])
                    else:
                        st.success("Location processed successfully!")
                        st.json(result)
                        
                        # Show on a map if we have coordinates
                        if result["found_latitude"] and result["found_longitude"]:
                            st.map({
                                "lat": [result["found_latitude"]],
                                "lon": [result["found_longitude"]]
                            })
                            
                            # Show offset point if applicable
                            if result["offset_applied"]:
                                st.map({
                                    "lat": [result["offset_latitude"]],
                                    "lon": [result["offset_longitude"]]
                                })
                else:
                    st.write("LLM Response:", message.content)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            
            finally:
                # Cleanup
                if photo_filename and os.path.exists(photo_filename):
                    os.remove(photo_filename)

if __name__ == "__main__":
    main()
    