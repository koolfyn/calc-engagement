def choose_model(
     context
):

     mode=context.recommended_approach


     if mode=="procedural":

          return "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"

     if mode=="conceptual":

          return "openai/gpt-4o-mini"


     return "openrouter/owl-alpha"

