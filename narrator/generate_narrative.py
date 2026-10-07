import json              
from google import genai
from google.genai import types

def generate_scr_narrative(findings:dict) -> dict:
  """
  Generates an SCR(Situation,Complication,Resolution) narrative using Google GenAI SDK.
  """
  # Initialize the GenAI client (Ensure GOOGLE_API_KEY environment variable is set)
  client = genai.Client()

  ## Build a System instruction whic is required
  system_instruction = (
      " you are a senior data analyst  writing for mamaearth's regional ops and finance heads."
      "Structure your response strictly into three labeled sections:Situation .Complication,Resolution."
      "Explicit constraint: every number in the output must come from the supplied findings and"
      "appear with the exact same value . Do not invent any statistics."
  )
## Buiild the user prompt dynamically (no hardcoding )
## We convert the findings dict into a JSON string to interpolate it dynamically.
  user_prompt = f"Here are the findings to base the narrative on :\n{json.dumps(findings,indent=2)}"

##Model call parameter locking
  config = types.GenerateContentConfig(
     system_instruction = system_instruction,
     temperature = 0.0,        ##deterministic (factual business report ,not creative)
     max_output_tokens=500     ##Explicit value (at least 300, enough for ~ 250 words)
)

## Call client.models.generate_content(......)
  response =  client.models.generate_content(
     model = "gemini-3.5-flash",
     contents = user_prompt,
     config = config
)

## Extract and return the narrative
  narrative_text = response.text
  return {"narrative": narrative_text}

part 3 task 3..

import json
from google import genai
from google.genai import types

def generate_scr_narrative(findings:dict) -> dict:
  """ Generates an SCR(Situation,Complication,Resolution) narrative using Google Gemini .
  """
  # Initialize the GenAI client
  client = genai.Client()

  # System instruction definition
  system_instruction = (
      "you are a senior data analyst writing for mamaearth's regional ops and leadership team ."
      " Provide a structured narrative with labeled sections: Situation, Complication, Resolution."
  )

  # build user prompt dynamically from findings dictionary
  prompt = f" Based on the following analytical findings, write the SCR narrative: {json.dumps(findings)}"

  try:
      response = client.models.generate_content(
          model = "gemini-3.5-flash",
          contents = prompt,
          config = types.GenerateContentConfig(
              system_instruction = system_instruction,
              #temperature = 0.0 (deterministic - this is a factual business report, not a creative writing)
              temperature = 0.0,
              #max_output_tokens sett to an explicit value at least 300
              max_output_tokens = 350,
              #timeout set (>= 10 seconds)
              http_options=types.HttpOptions(timeout=15000)  # 15000 ms = 15 seconds
          )
      )

      #Success response structure required by task
      return{
          "status":"success",
          "narrative":response.text,
          "tokens":response.usage_metadata.totals_token_count 
      }                     
  except Exception as err:
    # Failure response structure required bt task
    return {
        "status":"error",
        "narrative": None,
        "message":str(err)
    }


