import re
from typing import Any

from .extract_base import Extract


class RegExtract(Extract):
    @staticmethod
    def extract(raw_response: str, **kwargs: Any) -> str:
        """
        Extract the answer from raw_response by regex.

        Chain of Thought (CoT) is a prompt format a series of intermediate reasoning steps
        which could significantly improves the ability of large language models to perform
        complex reasoning(https://arxiv.org/abs/2201.11903).

        The response contains a chain of thought and an answer, so we need to extract the answer from the response.

        Args:
            raw_response: raw response from model
            **kwargs: other arguments
        Returns: extracted result

        """

        if "extraction_regex" in kwargs \
                and kwargs["extraction_regex"] is not None:
            # if extraction_words is specified, we use it to extract the answer
            extraction_regex = kwargs["extraction_regex"]
            answer = re.match(extraction_regex, raw_response)
            if answer is None:
                answer = "<empty>"
            else:
                answer = answer.group(1)
            return answer.strip()

        return raw_response.strip()

class RegExtract_new(Extract):
    @staticmethod
    def extract(raw_response: str, **kwargs: Any) -> str:
        """
        Extract the answer from raw_response by regex.

        Chain of Thought (CoT) is a prompt format a series of intermediate reasoning steps
        which could significantly improves the ability of large language models to perform
        complex reasoning(https://arxiv.org/abs/2201.11903).

        The response contains a chain of thought and an answer, so we need to extract the answer from the response.

        Args:
            raw_response: raw response from model
            **kwargs: other arguments
        Returns: extracted result

        """

        if "extraction_regex" in kwargs \
                and kwargs["extraction_regex"] is not None:
            # if extraction_words is specified, we use it to extract the answer
            extraction_regex = kwargs["extraction_regex"]
            
            answer = re.sub('[,\n]','',raw_response)
            answer = re.findall(extraction_regex, answer)
            answer = [i for i in answer if i != '.']
            print(answer)
            if answer == []:
                answer = "<empty>"
            else: 
                if answer[-1][-1] == '.':
                    answer[-1] = answer[-1][:-1] 
                if len(answer[-1].split('.')) > 1:
                    answer[-1] = answer[-1].split('.')[0]
                if answer is None:
                    answer = "<empty>"
                else:
                    answer = str(answer[-1])

            return answer.strip()

        return raw_response.strip()