SCENARIO_PROMPT = """
                You are an expert executive coach and corporate mentor specializing in difficult professional conversations, conflict resolution, and leadership roleplay simulations.
                Generate a complete branching professional roleplay scenario with multiple paths, choices, and outcomes in the JSON format I'll specify.

                The scenario should have:
                1. A compelling professional title based on the theme provided
                2. A starting workplace situation (root node) with 2-3 strategic communication options
                3. Each option should lead to a realistic counter-response or next stage in the conversation with its own follow-up options
                4. Some communication paths should lead to poor outcomes (losing endings, e.g., escalation, misunderstanding, or damaged relationships)
                5. At least one path should lead to a successful professional outcome (winning ending, e.g., constructive resolution, alignment, or successful negotiation)

                Scenario structure requirements:
                - Each node should have 2-3 strategic choices except for ending nodes
                - The scenario should be 3-4 levels deep (including root node)
                - Add variety in the conversation paths (some resolve earlier, some require deeper negotiation)
                - Make sure there's at least one successful resolution path

                Output your scenario in this exact JSON structure:
                {format_instructions}

                Don't simplify or omit any part of the scenario structure. 
                Don't add any text outside of the JSON structure.
                """

SCENARIO_JSON_STRUCTURE = """
        {
            "title": "Scenario Title",
            "rootNode": {
                "content": "The starting workplace situation",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Option 1 communication text",
                        "nextNode": {
                            "content": "What happens after option 1",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    // More options for root node
                ]
            }
        }
        """