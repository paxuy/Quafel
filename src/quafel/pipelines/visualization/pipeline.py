"""
This is a boilerplate pipeline 'visualization'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from quafel.pipelines.visualization.nodes import (
    shots_depths_viz,
    shots_qubits_viz,
)


def create_pipeline(figures, **kwargs) -> dict:
    pl_visualize_evaluations = pipeline(
        [
            node(
                func=shots_depths_viz,
                inputs={
                    "evaluations_combined": "evaluations_combined",
                },
                outputs={
                    **{f: f for f in filter(lambda s: "depth" in s, figures)},
                },
                name=f"shots_depths_viz",
            ),
            node(
                func=shots_qubits_viz,
                inputs={
                    "evaluations_combined": "evaluations_combined",
                },
                outputs={
                    **{f: f for f in filter(lambda s: "qubits" in s, figures)},
                },
                name=f"shots_depth_viz",
            ),
        ],
        inputs={
            "evaluations_combined": "evaluations_combined",
        },
        outputs={
            **{f: f for f in figures},
        },
    )

    return {
        "pl_visualize_evaluations": pl_visualize_evaluations,
    }
