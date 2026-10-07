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



part 3 task 4

def generate_scr_narrative(findings:dict) -> dict:
  """
  Offline fallback path that deterministaclly formats the narrative
  using an f-string template directly from findings with no API or network dependancy.
  """
  # Extarct values directly from findings dictionary with default fallbacks
  total_revenue = findings.get("total_revenye","97,359.30")
  cod_return_rate = findings.get("cod_return_rate","44.4")
  highest_risk_rate = findings.get("highest_risk_rate","54.5")
  reconciliation_delta = findings.get("reconciliation_delta","2501.90")
  peak_month = findings.get("peak_month","March")
  peak_month_value = findings.get("peak_month_value","20318.90")

  ## format into 3 labeled sections (Situation, Complication, Resolution)
  narrative_text = (
      f"Situation:\n"
      f"The cleaned total revenue stood at {total_revenue}, with performance peaking in "
      f" {peak_month} together with {peak_month_value}. \n\n"
      f"Complication:\n"
      f"the operational reviews shows a COD return rate of {cod_return_rate}%, while the COD + Tier-2"
      f"highest-risk segment return rate reached {highest_risk_rate}%. Additionally, a duplicate-driven "
      f"reconciliation delta of {reconciliation_delta} was recorded.\n\n"
      f"Resolution:\n"
      f"Implement targeted process improvements to mitigate COD returns and elemenate duplicate "
      f"entries driving the reconciliation delta."
  )

  # Return structured dict shape matching the online version
  return{
      "sataus":"success",
      "narrative": narrative_text,
      "tokens":0
  }     

part 3 task 5

def check_numeric_accuracy(narrative_text:str) -> bool: 
  """
  Checker function that verifies if all 5 figures are present 
  in the narrative text (after normalizing commas).
  """
  # Normalize commas from the narrative text for easy matching
  normalized_text = narrative_text.replace(',','')

  # List of required targets (values without commas)
  required_figures ={
      "Cleaned Total Revenue": ["97358.30", "97358.3"],
      "COD Return rate":["44.4"],
      "COD + Tier-2 Risk Return Rate":["54.5"],
      "Reconciliation Delta":["2501.90","2501.9"],
      "Peak Month":["March"],
      "Peak Month Value":["20318.90","20318.9"]
  } 

  all_passed =True
  print("---- Numeric Accuracy Verification ---")

  # Assert presence of each figure and print pass/fail line
  for label, options in required_figures.items():
      found = any(option in normalized_text for option in options)
      if found:
        print(f"[PASS] {label}")
      else:
        print(f"[FAIL] {label}")
        all_passed = False

  return all_passed

 Save narrative text to narrator/sample_output.txt as mentioned in task 
import os 
os.makedirs ("narrator", exist_ok=True)
with open("narrator/sample_output.txt","w") as f:
    f.write(result["narrative"])






  




  


