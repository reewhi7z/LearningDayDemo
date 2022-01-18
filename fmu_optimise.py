from types import FunctionType
from typing import Tuple
from functools import partial

import fmpy
from fmpy import validation


class InvalidModelError(Exception):
    pass


def empty_logger(*args):
    pass

def create_cost_function(
    filename: str,
    input_names: Tuple[str],
    output_names: Tuple[str],
    start_time: float,
    stop_time: float,
    step_size: float,
    post_simulation_function: FunctionType,
    show_output: bool = False
):
    def f(
        filename: str,
        input_names: Tuple[str],
        output_names: Tuple[str],
        start_time: float,
        stop_time: float,
        step_size: float,
        post_simulation_function: FunctionType,
        show_output: bool,
        x,
    ):
        start_values = {k: v for k, v in zip(input_names, x)}
        results = fmpy.simulate_fmu(
            filename,
            validate=False,
            start_time=start_time,
            stop_time=stop_time,
            step_size=step_size,
            start_values=start_values,
            output=output_names,
            record_events=False,
            fmi_call_logger = None,
            logger = None if show_output else empty_logger 
        )
        return post_simulation_function(results)

    # validate the model
    validation_errors = validation.validate_fmu(filename)
    if len(validation_errors) > 0:
        raise InvalidModelError(validation_errors)

    # extract the FMU
    unzipdir = fmpy.extract(filename)

    return partial(
        f,
        unzipdir,
        input_names,
        output_names,
        start_time,
        stop_time,
        step_size,
        post_simulation_function,
        show_output
    )
