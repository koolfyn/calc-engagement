from uuid import uuid4
import asyncio

from adapters.teaching_adapter import (
    CalculusTeachingAdapter
)

from prompts.prompt_builder import (
    build_prompt
)

from routing.model_router import (
    choose_model
)

from llm.openrouter_client import (
    generate_response
)


learner_id=uuid4()


async def main():

    teaching=CalculusTeachingAdapter()

    context=await teaching.build_context(
        learner_id,
        "chain_rule"
    )


    prompt=build_prompt(

        context,

        "I'm confused about trig sub"
    )


    model=choose_model(
        context
    )


    print("\nMODEL:")
    print(model)

    print("\nPROMPT:")
    print(prompt)


    response=await generate_response(
        prompt,
        model
    )

    print("\nAI RESPONSE:")
    print(response)



if __name__=="__main__":
    asyncio.run(main())
