from uuid import uuid4

from capillary_actions_sdk.ports.learner_interaction import (
    TeachingPort
)

from capillary_actions_sdk.models.learner_interaction import (
    TeachingContext,
    LearnerProgress,
    KnowledgeConcept
)


class CalculusTeachingAdapter(TeachingPort):

    async def build_context(
        self,
        learner_id,
        concept_id
    ):

        concept = KnowledgeConcept(
            id = "integrals",
            name = "Integrals",
            description = "Definite and indefinite integration",
            difficulty = 3,
            tags = ["ap_calc"],
            prerequisites = ["derivatives"]
        )


        progress = LearnerProgress(

            learner_id=learner_id,

            knowledge_graph_id=uuid4(),

            mastery={

                "limits":0.9,
                "derivatives":0.7,
                "integrals":0.8

            },

            current_concept="integrals",

            completed_concepts=[
                "limits",
                "derivatives"
            ]
        )


        return TeachingContext(

            learner_progress=progress,

            target_concept=concept,

            student_working_memory={

                "last_confusion":
                "student struggled with power rule"

            },

            recommended_approach=
            "conceptual"
        )


    async def record_outcome(
        self,
        learner_id,
        concept_id,
        outcome
    ):

        print(
            f"Outcome recorded: {outcome}"
        )
