def build_prompt(
    context,
    user_input
):

    return f"""
Welcome to another AP Calc BC tutoring session!

Current concept:

{context.target_concept.name}

Learner mastery:

{context.learner_progress.mastery}

Prerequisites:

{context.target_concept.prerequisites}

Recommended teaching mode:

{context.recommended_approach}

Student memory:

{context.student_working_memory}

Student input:

{user_input}

Respond using the recommended teaching mode.
"""
