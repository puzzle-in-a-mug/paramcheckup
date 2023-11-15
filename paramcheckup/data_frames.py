"""

##### List of functions (alphabetical order) #####

## Functions WITH TESTS ###

- column_name_in_dataframe(column_name, data_frame, param_name, func_name)
- is_empty_data_frame(data_frame, param_name, func_name)



## Functions WITH some TESTS (needs improvements) ###


## Functions WITHOUT tests ###



##### List of CLASS (alphabetical order) #####







Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: October 27, 2023.

Last update: October 27, 2023



"""

##### IMPORTS #####

### Standard ###
import sys

### Third part ###

### home made ###
from .utils import user_warning
from . import documentation as docs

##### CONSTANTS #####


##### CLASSES #####


##### FUNCTIONS #####
@docs.docstring_parameter(
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def column_name(
    column_name, data_frame, param_name, kind, kind_name, stacklevel=4, error=True
):
    """This function checks whether the *str* *column_name* is a valid column name for the :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` *dataframe*.

    Parameters
    ----------
    column_name : str
        The name of the column to be checked;
    data_frame : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
        The :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` that should contain the column named *column_name*;
    {param_name}
        {param_name_desc}
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}

    Returns
    -------
    True
        If `column_name` **IS** a valid column name for the `data_frame`;
    ValueError
        If `column_name` is **NOT** a valid column name for the `data_frame`;

    Examples
    --------
    >>> import pandas as pd
    >>> from paramcheckup import data_frames
    >>> data = [["Anderson", 33], ["Juliana", 31], ["Marcos", 26], ["Mariana", 30]]
    >>> columns = ["Name", "Age"]
    >>> df = pd.DataFrame(
        data=data,
        columns=columns,
    )
    >>> output = data_frames.column_name(
        column_name="Name",
        data_frame=df,
        param_name="data_frame",
        kind="function",
        kind_name="database",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> import pandas as pd
    >>> from paramcheckup import data_frames
    >>> data = [["Anderson", 33], ["Juliana", 31], ["Marcos", 26], ["Mariana", 30]]
    >>> columns = ["Name", "Age"]
    >>> df = pd.DataFrame(
        data=data,
        columns=columns,
    )
    >>> output = data_frames.column_name(
        column_name="Gender",
        data_frame=df,
        param_name="data_frame",
        kind="function",
        kind_name="database",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 10: The `data_frame` in function `database` does not contain a column with the name `Gender`.


    """

    if column_name not in data_frame.columns:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` does not contain a column with the name `{column_name}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("ColumnNameError")
            except ValueError:
                raise
    return True


def is_empty(data_frame, param_name, func_name):
    """This function checks whether the *data_frame* is an empty :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`

    Parameters
    ----------
    data_frame : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
        The :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` to be checked for emptiness;
    param_name : str
        The name of the parameter that received the variable *value*';
    func_name : str
        The name of the function that utilizes the parameter *param_name*;

    Returns
    -------
    True
        If variable *data_frame* is **NOT** an empty :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`;
    ValueError
        If variable *data_frame* is an **EMPTY** :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`;

    Examples
    --------
    >>> from paramcheckup import data_frames
    >>> import pandas as pd
    >>> df = pd.DataFrame({
        "Dataset": [1, 2, 3, 4, 5]
    })
    >>> print(data_frames.is_empty(df, "data", "ttest"))
    True


    >>> from paramcheckup import data_frames
    >>> import pandas as pd
    >>> df = pd.DataFrame({})
    >>> data_frames.is_empty(df, "data", "ttest")
    The DataFrame 'data' in function 'ttest' is an EMPTY DataFrame.

    """

    if data_frame.empty:
        try:
            raise ValueError("EmptyDataFrameError")
        except ValueError:
            print(
                f"The DataFrame '{param_name}' in function '{func_name}' is an EMPTY DataFrame.\n"
            )
            raise
    return True
