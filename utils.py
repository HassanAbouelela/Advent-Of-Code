# -------------------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2019 Scaleios
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -------------------------------------------------------------------------------


class PerformanceUtils:
    def __init__(self):
        pass

    @staticmethod
    def time_checker(func, runs: int = 10000, *args, **kwargs) -> [int, int]:
        """
        Returns the time needed to run a function 'runs' times.

        Parameters:
            func (function): The function to be tested
            runs (int): (Optional) The amount of times the function should be run
            args (args): (Optional) Arguments that should be passed into the function.
                         Passed in as is.
            kwargs (kwargs): (Optional) Named arguments that should be passed into the function.
                             Passed in as is.

        Returns:
            average (int): The average time to run the function once
            total (int): Time taken to run function 'runs' times
        """
        import datetime
        if args and kwargs:
            start = datetime.datetime.now()
            for i in range(runs):
                func(*args, **kwargs)
            end = datetime.datetime.now()
        elif args:
            start = datetime.datetime.now()
            for i in range(runs):
                func(*args)
            end = datetime.datetime.now()
        elif kwargs:
            start = datetime.datetime.now()
            for i in range(runs):
                func(**kwargs)
            end = datetime.datetime.now()
        else:
            start = datetime.datetime.now()
            for i in range(runs):
                func()
            end = datetime.datetime.now()
        total = end - start
        average = (end - start) / runs
        return average.total_seconds(), total.total_seconds()
    # def


class UnitTestUtils:
    def __init__(self):
        pass


class DataMethods:
    def __init__(self):
        pass

    class StringMethods:
        def __init__(self):
            pass

        @staticmethod
        def multi_term_split(string: str, *args: any, cleanup: bool = True) -> list:
            """
            Separates a string into a list based on the given args.

            Parameters:
                string (str): The string to be separated
                args (any): Terms to split the string
                cleanup (bool): (Optional) If results should be automatically cleaned
                               Defaults to True

            Returns:
                separated (list): A list of the string separated at the args
            """

            separated = string
            try:
                separated = separated.split(args[0])
            except ValueError:
                return separated
            except IndexError:
                return ["Index Error: No arguments given"]
            if len(args) <= 1:
                return separated

            for term in args:
                temp = []
                for item in separated:
                    try:
                        temp.extend(item.split(term))
                    except ValueError:
                        pass
                separated = temp.copy()

            if cleanup:
                new_separated = []
                for term in separated:
                    if term.isspace() or not term or term.strip() in new_separated or term == string:
                        pass
                    else:
                        new_separated.append(term.strip())
                separated = new_separated
            return separated

    class DictionaryMethods:
        def __init__(self):
            pass

        @staticmethod
        def update_dict(dictionary: dict, key: any, value: any) -> None:
            """
            Non-destructive dict.update. dictionary[key] is updated to a list
            containing former value and new value.

            Parameters:
                dictionary (dict): Dictionary to be modified
                key: The key to be modified
                value: The value to add to the key

            Returns:
                None
            """
            try:
                if type(dictionary[key]) is list:
                    x = dictionary[key]
                    x.append(value)
                    dictionary[key] = x
                else:
                    dictionary[key] = [dictionary[key], value]

            except KeyError:
                dictionary[key] = value

        @staticmethod
        def tracker_dict(dictionary: dict, key: any, add: int = 1) -> None:
            """
            Iterates a value for a given key.

            Parameters:
                dictionary (dict): The dictionary to work on
                key (any): The key to be iterated
                add (int): (Optional) The amount by which to iterate key

            Returns:
                None
            """
            try:
                dictionary[key] = dictionary[key] + add
            except KeyError:
                dictionary[key] = add
