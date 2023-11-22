x_str = "698310488572646777019184";
y_str = "144585992498882884065634";

x_str = convertStringsToChars(reverse(x_str));
y_str = convertStringsToChars(reverse(y_str));

max_len = max(length(x_str), length(y_str));
binary_power = ceil(log2(max_len));
two_D = binary_power * 2;

x = zeros(1,2^(binary_power + 1));
y = zeros(1,2^(binary_power + 1));

for ix = 1:length(x_str)
    x(ix) = str2num(x_str(ix));
    y(ix) = str2num(y_str(ix));
end

X = fft(x);
Y = fft(y);

fprintf("\nX\n");
for ix = 1:length(X)
    fprintf("%1.6f, i %1.6f\n", real(X(ix)), imag(X(ix)));
end

fprintf("\nY\n");
for ix = 1:length(Y)
    fprintf("%1.6f, i %1.6f\n", real(Y(ix)), imag(Y(ix)));
end

Z = X .* Y;

fprintf("\nZ\n");
for ix = 1:length(Z)
    fprintf("%1.6f, i %1.6f\n", real(Z(ix)), imag(Z(ix)));
end

format long
z = ifft(Z);
z = round(z);

fprintf("\nz\n");
for ix = 1:length(z)
    fprintf("%1.6f, i %1.6f\n", real(z(ix)), imag(z(ix)));
end

for ix = 2:length(z)
    c = floor(z(ix-1)/10);
    z(ix) = z(ix) + c;
    z(ix-1) = z(ix-1) - c*10;
end

return_str = "";
for ix = 1:length(z)
    return_str = strcat(return_str, num2str(z(ix)));
end

return_str = reverse(return_str);
return_str = convertStringsToChars(return_str);

filtered_str = "";
all_zeroes = 1;
for ix = 1:length(return_str)
    if (all_zeros == 0)
        if return_str(ix) ~= '0'
            all_zeroes = 0;
        end
    end
    if (all_zeroes == 0)
        filtered_str = strcat(filtered_str, return_str(ix));
    end
end

filtered_str