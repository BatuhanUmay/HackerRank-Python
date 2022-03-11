# #include <iostream>
# #include <vector>
# #include <string>
#
# template<typename T>void printArray(vector<T> a){for(T i:a)cout<<i<<endl;}
#
# using namespace std;
#
# int main() {
#     int n;
#
#     cin >> n;
#     vector < int > int_vector(n);
#     for (int i = 0; i < n; i++) {
#         int value;
#         cin >> value;
#         int_vector[i] = value;
#     }
#
#     cin >> n;
#     vector < string > string_vector(n);
#     for (int i = 0; i < n; i++) {
#     string value;
#     cin >> value;
#     string_vector[i] = value;
#     }
#
#     printArray < int > (int_vector);
#     printArray < string > (string_vector);
#
#     return 0;
# }

from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

