import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BigIntTest {

    @Test
    public void testMultiplyPositiveNumbers() {
        int[] mag1 = {1, 2, 3}; // Represents the number 321 in little-endian
        int[] mag2 = {4, 5, 6}; // Represents the number 654 in little-endian

        BigInt num1 = new BigInt(1, mag1);
        BigInt num2 = new BigInt(1, mag2);
        BigInt result = num1.multiply(num2);

        int[] expectedResult = {4, 13, 28, 27, 18}; // Represents the number 210534 in little-endian
        BigInt expected = new BigInt(1, expectedResult);

        assertEquals(expected, result);
    }

    @Test
    public void testMultiplyNegativeNumbers() {
        int[] mag1 = {1, 2, 3}; // Represents the number -321 in little-endian
        int[] mag2 = {4, 5, 6}; // Represents the number -654 in little-endian

        BigInt num1 = new BigInt(-1, mag1);
        BigInt num2 = new BigInt(-1, mag2);
        BigInt result = num1.multiply(num2);

        int[] expectedResult = {4, 13, 28, 27, 18}; // Represents the number 210534 in little-endian
        BigInt expected = new BigInt(1, expectedResult);

        assertEquals(expected, result);
    }

    @Test
    public void testMultiplyMixedSignNumbers() {
        int[] mag1 = {1, 2, 3}; // Represents the number -321 in little-endian
        int[] mag2 = {4, 5, 6}; // Represents the number 654 in little-endian

        BigInt num1 = new BigInt(-1, mag1);
        BigInt num2 = new BigInt(1, mag2);
        BigInt result = num1.multiply(num2);

        int[] expectedResult = {-4, -13, -28, -27, -18}; // Represents the number -210534 in little-endian
        BigInt expected = new BigInt(-1, expectedResult);

        assertEquals(expected, result);
    }

    @Test
    public void testMultiplyZero() {
        int[] mag1 = {0};
        int[] mag2 = {1, 2, 3}; // Represents the number 321 in little-endian

        BigInt num1 = new BigInt(0, mag1);
        BigInt num2 = new BigInt(1, mag2);
        BigInt result = num1.multiply(num2);

        int[] expectedResult = {0};
        BigInt expected = new BigInt(0, expectedResult);

        assertEquals(expected, result);
    }

    @Test
    public void testMultiplyWithLargeNumbers() {
        int[] mag1 = {1, 2, 3, 4, 5, 6, 7}; // Represents the number 7654321 in little-endian
        int[] mag2 = {8, 9, 1, 2, 3, 4, 5}; // Represents the number 54321089 in little-endian

        BigInt num1 = new BigInt(1, mag1);
        BigInt num2 = new BigInt(1, mag2);
        BigInt result = num1.multiply(num2);

        int[] expectedResult = {8, 23, 51, 83, 120, 161, 214, 290, 356, 365, 382, 351, 177};
        BigInt expected = new BigInt(1, expectedResult);

        assertEquals(expected, result);
    }
}

//    @Test
//    public void testMultiplyLargeNumbers() {
//        int[] mag1 = {9, 8, 7, 6, 5, 4, 3, 2, 1}; // Represents the number 123456789 in little-endian
//        int[] mag2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Represents the number 987654321 in little-endian
//
//        BigInt num1 = new BigInt(1, mag1);
//        BigInt num2 = new BigInt(1, mag2);
//        BigInt result = num1.multiply(num2);
//
//        int[] expectedResult = {9, 7, 6, 5, 4, 3, 2, 1, 0, 7, 5, 3, 1, 0, 8, 6, 4, 2, 0, 9};
//        BigInt expected = new BigInt(1, expectedResult);
//
//        assertEquals(expected, result);
//    }
//
//    @Test
//    public void testMultiplyWithLargeNegativeNumbers() {
//        int[] mag1 = {9, 8, 7, 6, 5, 4, 3, 2, 1}; // Represents the number -123456789 in little-endian
//        int[] mag2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Represents the number -987654321 in little-endian
//
//        BigInt num1 = new BigInt(-1, mag1);
//        BigInt num2 = new BigInt(-1, mag2);
//        BigInt result = num1.multiply(num2);
//
//        int[] expectedResult = {9, 7, 6, 5, 4, 3, 2, 1, 0, 7, 5, 3, 1, 0, 8, 6, 4, 2, 0, 9};
//        BigInt expected = new BigInt(1, expectedResult);
//
//        assertEquals(expected, result);
//    }

//    @Test
//    public void testMultiplyLargeBigIntegers() {
//        String num1Str = "123456789123456789"; // 18 digits
//        String num2Str = "987654321987654321"; // 18 digits
//
//        BigInteger num1 = new BigInteger(num1Str);
//        BigInteger num2 = new BigInteger(num2Str);
//        BigInteger result = num1.multiply(num2);
//
//        String expectedResultStr = "121932631137021795136337638235156289"; // 36 digits
//        BigInteger expected = new BigInteger(expectedResultStr);
//
//        assertEquals(expected, result);
//    }
//
//    @Test
//    public void testMultiplyLargeNegativeBigIntegers() {
//        String num1Str = "-123456789123456789"; // 18 digits
//        String num2Str = "-987654321987654321"; // 18 digits
//
//        BigInteger num1 = new BigInteger(num1Str);
//        BigInteger num2 = new BigInteger(num2Str);
//        BigInteger result = num1.multiply(num2);
//
//        String expectedResultStr = "121932631137021795136337638235156289"; // 36 digits
//        BigInteger expected = new BigInteger(expectedResultStr);
//
//        assertEquals(expected, result);
//    }


//    @Test
//    public void testMultiplyVeryLargeBigIntegers() {
//        String num1Str = "123456789098765432109876543210"; // 30 digits
//        String num2Str = "987654321012345678909876543210"; // 30 digits
//
//        BigInteger num1 = new BigInteger(num1Str);
//        BigInteger num2 = new BigInteger(num2Str);
//        BigInteger result = num1.multiply(num2);
//
//        String expectedResultStr = "1219326321033379020955123850164234190742118864860980548100"; // 60 digits
//        BigInteger expected = new BigInteger(expectedResultStr);
//
//        assertEquals(expected, result);
//    }
//
//    @Test
//    public void testMultiplyVeryLargeNegativeBigIntegers() {
//        String num1Str = "-123456789098765432109876543210"; // 30 digits
//        String num2Str = "-987654321012345678909876543210"; // 30 digits
//
//        BigInteger num1 = new BigInteger(num1Str);
//        BigInteger num2 = new BigInteger(num2Str);
//        BigInteger result = num1.multiply(num2);
//
//        String expectedResultStr = "1219326321033379020955123850164234190742118864860980548100"; // 60 digits
//        BigInteger expected = new BigInteger(expectedResultStr);
//
//        assertEquals(expected, result);
//    }
