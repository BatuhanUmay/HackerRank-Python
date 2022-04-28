# import java.util. *;
#
# public class Solution {
#
#     public static void main(String[] args) {
#         long n = in.nextLong();
#         int a = in.nextInt();
#         int b = in.nextInt();
#         int increment = 4;
#
#         for (long i=1;i < n;i++)
#             {
#                 if (a == 3)
#                 {
#                     if (isTriangularNumber(i))
#                         System.out.println(i);
#                     if (i == 1) i += 3;
#                     else if (i > 4)
#                     {
#                         i += increment+2;
#                         increment += 3;
#                     }
#                     }
#                 else
#                 {
#                     if (isHexagonalNumber(i))
#                         System.out.println(i);
#                     if (i == 1) i += 3;
#                     else if (i > 4)
#                     {
#                         i += increment+2;
#                         increment += 3;
#                     }
#                 }
#             }
#     }
#
#     public static boolean isTriangularNumber(long n)
#     {
#         double tTest = Math.sqrt(1 + 8*n);
#         return tTest == ((long)tTest);
#     }
#
#     private static boolean isHexagonalNumber(long number
#     {
#         double hexTest = (Math.sqrt(1 + 8 * number) + 1.0) / 4.0;
#         return hexTest == ((long)hexTest);
#
#     }
# }

