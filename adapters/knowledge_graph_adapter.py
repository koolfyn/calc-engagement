from uuid import UUID, uuid4

from capillary_actions_sdk.ports.learner_interaction import (
    KnowledgeGraphPort
)

from capillary_actions_sdk.models.learner_interaction import (
    KnowledgeConcept,
    KnowledgeGraph
)


class CalculusGraphAdapter(KnowledgeGraphPort):

    def __init__(self):

        self.concepts = {

            "limits":
                KnowledgeConcept(
                    id="limits",
                    name="Limits",
                    description="Introduction to limits and continuity",
                    difficulty=1,
                    tags=["ap_calc"],
                    prerequisites=[]
                ),

            "derivatives":
                KnowledgeConcept(
                    id="derivatives",
                    name="Derivatives",
                    description="Rate of change and derivative rules",
                    difficulty=2,
                    tags=["ap_calc"],
                    prerequisites=["limits"]
                ),

            "integrals":
                KnowledgeConcept(
                    id="integrals",
                    name="Integrals",
                    description="Definite and indefinite integration techniques",
                    difficulty=3,
                    tags=["ap_calc"],
                    prerequisites=["derivatives"]
                )

        }


    async def get_graph(
        self,
        graph_id: UUID
    ) -> KnowledgeGraph:

        return KnowledgeGraph(
            id=graph_id,
            name="AP Calculus BC Graph",
            concepts=list(self.concepts.values())
        )


    async def get_concept(
        self,
        concept_id:str
    ):

        return self.concepts[concept_id]


    async def get_prerequisites(
        self,
        concept_id:str
    ):
        concept = self.concepts[concept_id]
        prereq_ids = getattr(concept, "prerequisites", []) or []
        return [self.concepts[p] for p in prereq_ids]


    async def search_concepts(
        self,
        query:str,
        graph_id=None
    ):

        return [
            c for c in self.concepts.values()
            if query.lower()
            in c.name.lower()
        ]
