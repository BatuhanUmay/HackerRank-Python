from random import randint

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


class TestDataUniqueValues(object):
    data = set()
    while len(data) < 10:
        data.add(randint(0, 100))

    @staticmethod
    def get_array():
        data = TestDataUniqueValues.data
        return list(data)

    @staticmethod
    def get_expected_result():
        data = TestDataUniqueValues.get_array()
        return data.index(min(data))

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


class TestDataExactlyTwoDifferentMinimums(object):
    data = set()
    while len(data) < 9:
        data.add(randint(0, 100))
    newData = list(data)
    newData.append(min(newData))

    @staticmethod
    def get_array():
        data = TestDataExactlyTwoDifferentMinimums.newData
        return data

    @staticmethod
    def get_expected_result():
        data = TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")


####################################################################################

# import random;
#
#
# class TestDataEmptyArray(object):
#
#     @staticmethod
#     def get_array():
#         # complete this function
#         return []
#
#
# class TestDataUniqueValues(object):
#
#     @staticmethod
#     def get_array():
#         # complete this function
#         TestDataUniqueValues.l1 = random.sample(range(0, 200), random.randint(2, 100))
#         return TestDataUniqueValues.l1
#
#     @staticmethod
#     def get_expected_result():
#         # complete this function
#         index = 0
#         for i in TestDataUniqueValues.l1:
#             if i == min(TestDataUniqueValues.l1):
#                 return index
#             index += 1
#
#
# class TestDataExactlyTwoDifferentMinimums(object):
#
#     @staticmethod
#     def get_array():
#         # complete this function
#         TestDataExactlyTwoDifferentMinimums.l2 = random.sample(range(0, 200), random.randint(2, 100))
#         TestDataExactlyTwoDifferentMinimums.l2.insert(random.randint(0, len(TestDataExactlyTwoDifferentMinimums.l2)),
#                                                       min(TestDataExactlyTwoDifferentMinimums.l2))
#         return TestDataExactlyTwoDifferentMinimums.l2
#
#     @staticmethod
#     def get_expected_result():
#         # complete this function
#         index = 0
#         for i in TestDataExactlyTwoDifferentMinimums.l2:
#             if i == min(TestDataExactlyTwoDifferentMinimums.l2):
#                 return index
#             index += 1
####################################################################################

# class TestDataEmptyArray(object):
#
#     @staticmethod
#     def get_array():
#         return list()
#
#
# class TestDataUniqueValues(object):
#
#     @staticmethod
#     def get_array():
#         return [2, 3]
#
#     @staticmethod
#     def get_expected_result():
#         return 0
#
#
# class TestDataExactlyTwoDifferentMinimums(object):
#
#     @staticmethod
#     def get_array():
#         return [2, 2]
#
#     @staticmethod
#     def get_expected_result():
#         return 0
