function [] = karatsuba(x, y, n)
    a = floor(x/10^n);
    b = mod(x,10^n);
    c = floor(y/10^n);
    d = mod(y,10^n);
    
    A = a*c;
    B = b*d;
    C = (a+b)*(c+d);
    D = A+B;
    E = C - D;
    result = A*10^(2*n) + E*10^n + B;
    fprintf("A=%d\n", A);
    fprintf("B=%d\n", B);
    fprintf("C=%d\n", C);
    fprintf("D=%d\n", D);
    fprintf("E=%d\n", E);
    fprintf("%d+%d+%d\n", A*10^(2*n), E*10^n, B);
    fprintf("=%d\n\n", result);
end