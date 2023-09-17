import java.lang.*;

public class BigInt {
    protected int signum = 0;                       // neg = -1, 0 = 0, pos = 1
    protected int[] mag;                            // Magnitude in little-endian
    public final static int MAXN = 134217728;       // Maximum value for n
    public final static int ENTRYSIZE = 10;         // Bits per entry in mag
    protected final static long P = 2013265921;     // The prime 15*2^{27}+1
    protected final static int OMEGA = 440564289;   // Root of unity 31^{15} mod P
    protected final static int TWOINV = 1006632961; // 2^{-1} mod P

    // Constructor
    public BigInt(int signum, int[] mag) {
        this.signum = signum;
        this.mag = mag;
    }

    // Multiply two BigInt numbers using the FFT method
    public BigInt multiply(BigInt val) {
        int n = makePowerOfTwo(Math.max(mag.length, val.mag.length)) * 2;
        int signResult = signum * val.signum;
        int[] A = padWithZeros(mag, n);             // copies mag into A padded w/ 0's
        int[] B = padWithZeros(val.mag, n);         // copies val.mag into B padded with 0's
        int[] root = rootsOfUnity(n);               // creates all n roots of unity
        int[] C = new int[n];                       // result array for A*B
        int[] AF = new int[n];                      // result array for FFT of A
        int[] BF = new int[n];                      // result array for FFT of B
        FFT(A, root, n, 0, AF);
        FFT(B, root, n, 0, BF);
        for (int i = 0; i < n; i++) {
            AF[i] = (int)(((long)AF[i] * (long)BF[i]) % P);    // Component multiply
        }
        reverseRoots(root);                         // Reverse roots to create inverse roots
        inverseFFT(AF, root, n, 0, C);         // Leaves inverse FFT result in C
        propagateCarries(C);                        // Convert C to the right number of bits per entry
        return new BigInt(signResult, C);
    }

    // Recursive FFT
    public void FFT(int[] A, int[] root, int n, int base, int[] Y) {
        int prod;
        if (n == 1) {
            Y[base] = A[base];
            return;
        }
        inverseShuffle(A, n, base);           // inverse shuffle to separate evens and odds
        FFT(A, root, n / 2, base, Y);          // results in Y[base] to Y[base+n/2-1]
        FFT(A, root, n / 2, base + n / 2, Y); // results in Y[base+n/2] to Y[base+n-1]
        int j = A.length / n;
        for (int i = 0; i < n / 2; i++) {
            prod = (int)(((long)root[i * j] * Y[base + n / 2 + i]) % P);
            Y[base + n / 2 + i] = (int)(((long)Y[base + i] + P - prod) % P);
            Y[base + i] = (int)(((long)Y[base + i] + prod) % P);
        }
    }

    // Recursive inverse FFT
    public void inverseFFT(int[] A, int[] root, int n, int base, int[] Y) {
        int inverseN = modInverse(n);       // n^{-1}
        FFT(A, root, n, base, Y);
        for (int i = 0; i < n; i++) {
            Y[i] = (int)(((long)Y[i] * inverseN) % P);
        }
    }

    // Compute reverse roots
    protected void reverseRoots(int[] roots) {
        int n = roots.length;
        int j = n / 2 - 1;

        for (int i = 1; i < n - 1; i++) {
            if (i < j) {
                int temp = roots[i];
                roots[i] = roots[j];
                roots[j] = temp;
            }

            int k = n / 2;
            while (j < k) {
                k /= 2;
                j += k;
            }
            j -= k;
        }
    }

    // Calculate the modular inverse
    protected int modInverse(int n) { // assumes n is a power of 2
        int result = 1;
        for (long twoPower = 1; twoPower < n; twoPower *= 2) {
            result = (int)(((long)result * TWOINV) % P);
        }
        return result;
    }

    // Inverse shuffle
    protected void inverseShuffle(int[] A, int n, int base) {
        int shift;
        int[] sp = new int[n];
        for (int i = 0; i < n / 2; i++) { // Unshuffle A into the scratch space
            shift = base + 2 * i;
            sp[i] = A[shift];           // an even index
            sp[i + n / 2] = A[shift + 1];     // an odd index
        }
        for (int i = 0; i < n; i++) {
            A[base + i] = sp[i];          // copy back to A
        }
    }

    // Create an array of roots of unity
    protected int[] rootsOfUnity(int n) { // assumes n is a power of 2
        int t = MAXN;
        int nthroot = OMEGA;
        for (int i = 0; i < t / n; i++) {
            nthroot = (int)(((long)nthroot * nthroot) % P);
        }
        int[] roots = new int[n];
        int r = 1;          // r will run through all nth roots of unity
        for (int i = 0; i < n; i++) {
            roots[i] = r;
            r = (int)(((long)r * nthroot) % P);
        }
        return roots;
    }

    // Pad the array with zeros to make it a power of two in size
    protected int[] padWithZeros(int[] arr, int n) {
        int[] paddedArr = new int[n];
        System.arraycopy(arr, 0, paddedArr, 0, arr.length);
        return paddedArr;
    }

    // Make an integer power of two
    protected int makePowerOfTwo(int num) {
        int result = 1;
        while (result < num) {
            result *= 2;
        }
        return result;
    }

    // Helper function to propagate carries in an array
    protected void propagateCarries(int[] A) {
        int i, carry;
        carry = 0;
        for (i = 0; i < A.length; i++) {
            A[i] = A[i] + carry;
            carry = A[i] >>> ENTRYSIZE;
            A[i] = A[i] - (carry << ENTRYSIZE);
        }
    }
}
