import re
from typing import Any

from .extract_base import Extract


class MultiChoiceBatchExtract(Extract):
    @staticmethod
    def extract(raw_response: str, **kwargs: Any) -> str:
        """
        Extract the batch of multi-choice answers from raw_response by regex.

        Args:
            raw_response: raw response from model
            **kwargs: other arguments
        Returns: extracted result list

        """
        batch_answers = []
        for answer in raw_response.split("\n"):
            # Skip answer prefix
            if answer.startswith("A:"):
                answer = answer[len("A: "):]
            elif answer.startswith("A["):
                answer = answer[len("A[i]: "):]
            elif answer.startswith("Answer: "):
                answer = answer[len("Answer: "):]
            elif answer.startswith("Answer["):
                answer = answer[len("Answer[i]: "):]

            if "extraction_regex" in kwargs \
                    and kwargs["extraction_regex"] is not None:
                # if extraction_words is specified, we use it to extract the answer
                extraction_regex = kwargs["extraction_regex"]
                answer = re.match(extraction_regex, answer)
                if answer is None:
                    answer = "<empty>"
                else:
                    answer = answer.group(1)
            answer = answer.lstrip('(').rstrip(')').lower()
            batch_answers.append(answer)

        return batch_answers
