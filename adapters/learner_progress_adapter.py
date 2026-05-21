from capillary_actions_sdk.ports.learner_interaction import (
     LearnerProgressPort
)


class LearnerAdapter(
     LearnerProgressPort
):

    def __init__(self):

         self.mastery={

              "limits":0.8,
              "derivatives":0.4,
              "integrals": 0.5
         }


    async def get_progress(
          self,
          learner_id,
          graph_id
    ):

          ...


    async def update_mastery(
         self,
         learner_id,
         concept_id,
         score
    ):

         self.mastery[concept_id]=score


    async def get_next_concept(
         self,
         learner_id,
         graph_id
    ):

         ...
