import pandas as pd
from ..module import Module
from .. import utils as u
from .. import prompts as p


class ActivityLabeler(Module):
    """
    This is the module that extracts the activity labels from the patient journey.
    """

    # Remove this, only for test purposes
    def __init__(self):
        super().__init__()
        self.name = "Activity Labeler"
        self.description = "Extracts the activity labels from a patient journey."

    def execute(self, _input, patient_journey=None):
        super().execute(_input, patient_journey)
        self.result = self.__extract_activities()

    def __extract_activities(self):
        """Converts the input text to activity_labels."""
        name = "event_information"
        messages = [
            {"role": "system", "content": p.TXT_TO_BULLETPOINTS_CONTEXT},
            {
                "role": "user",
                "content": f"{p.TXT_TO_BULLETPOINTS_PROMPT} {self.patient_journey}",
            },
            {"role": "assistant", "content": p.TXT_TO_BULLETPOINTS_ANSWER},
        ]
        activity_labels = u.query_gpt(messages)
        # TODO: adjust prompt to remove "-" instead of replace()
        activity_labels = activity_labels.replace("- ", "").split("\n")
        df = pd.DataFrame(activity_labels, columns=[name])
        # document_intermediates("\n", True)
        return df
