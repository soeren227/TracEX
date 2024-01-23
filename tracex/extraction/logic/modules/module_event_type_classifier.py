import pandas as pd

from ..module import Module
from .. import utils as u
from .. import prompts as p


from pandas import DataFrame


class EventTypeClassifier(Module):
    """
    This module classifies the event types of the activities. The given event types are 'Symptom Onset',
    'Symptom Offset', 'Diagnosis', 'Doctor visit', 'Treatment', 'Hospital admission', 'Hospital discharge',
    'Medication', 'Lifestyle Change' and 'Feelings'. This is done so that we can extract a standardized set of event
    types from the patient journey. This is necessary for the application of process mining algorithms.
    """

    def __init__(self):
        super().__init__()
        self.name = "Event Type Classifier"
        self.description = "Classifies the event types for the corresponding activity labels from a patient journey."

    def execute(self, df, patient_journey=None):
        super().execute(df, patient_journey)
        self.result = self.__add_event_types(df)

    def __add_event_types(self, df):
        """Adds event types to the activity labels."""
        name = "event_type"
        df[name] = df["event_information"].apply(self.__classify_event_type)
        # document_intermediates(output)

        return df

    @staticmethod
    def __classify_event_type(activity_label):
        messages = [
            {"role": "system", "content": p.EVENT_TYPE_CONTEXT},
            {
                "role": "user",
                "content": f"{p.EVENT_TYPE_PROMPT}\n The bulletpoint: {activity_label}",
            },
            {"role": "assistant", "content": p.EVENT_TYPE_ANSWER},
        ]
        output = u.query_gpt(messages)
        fc_message = [
            {"role": "system", "content": p.FC_EVENT_TYPE_CONTEXT},
            {
                "role": "user",
                "content": f"{p.FC_EVENT_TYPE_PROMPT} The text: {output}",
            },
        ]
        event_type = u.query_gpt(
            messages=fc_message,
            tool_choice={
                "type": "function",
                "function": {"name": "add_event_type"},
            },
        )

        return event_type
