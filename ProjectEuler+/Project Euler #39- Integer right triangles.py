# Java kodu

# public class Solution {
#
#     static int[] getIntegerRightTriangles() {
#         int[] freq = new int[5_000_001];
#
#         for (int m = 2; m <= 1200; m++) {
#             for (int n = 1; n < m; n++) {
#                 if ((m + n) % 2 == 0 || gcd(m, n) != 1)
#                     continue;
#
#                 int p = 2 * m * (m + n);
#                 int k = 1;
#
#                 while (k * p <= 5_000_000) {
#                     freq[k * p]++;
#                     k++;
#                 }
#             }
#         }
#
#         int[] res = new int[freq.length];
#
#         for (int i = 1; i < freq.length; i++)
#             res[i] = freq[i] > freq[res[i - 1]] ? i : res[i - 1];
#
#         return res;
#     }
#
#     private static int gcd(int m, int n) {
#         while (true) {
#             if (n == 0)
#                 return m;
#
#             int tmp = m;
#             m = n;
#             n = tmp % n;
#         }
#     }
#
#     public static void main(String[] args) {
#         int[] res = getIntegerRightTriangles();
#
#         Scanner scan = new Scanner(System.in);
#         int T = scan.nextInt();
#
#         for (int i = 0; i < T; i++) {
#             int N = scan.nextInt();
#             System.out.println(res[N]);
#         }
#     }
# }