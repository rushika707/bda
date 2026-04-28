% ================================
% ThingSpeak MATLAB Full Example
% ================================

% Channel details
channelID = 3351574;   % replace with your channel ID
readAPIKey = 'YOUR_READ_API_KEY';
writeAPIKey = 'YOUR_WRITE_API_KEY';

% -------------------------------
% 1. READ DATA (last 40 minutes)
% -------------------------------
data = thingSpeakRead(channelID, ...
    'Fields', [1 2], ...
    'NumMinutes', 40, ...
    'ReadKey', readAPIKey);

% Separate fields
humidity = data(:,1);
temperature = data(:,2);

disp("Humidity values:");
disp(humidity);

disp("Temperature values:");
disp(temperature);

% -------------------------------
% 2. CLEAN DATA (remove NaN)
% -------------------------------
humidityClean = humidity(~isnan(humidity));
temperatureClean = temperature(~isnan(temperature));

% -------------------------------
% 3. CALCULATIONS
% -------------------------------
avgHumidity = mean(humidityClean);
maxHumidity = max(humidityClean);

avgTemp = mean(temperatureClean);
maxTemp = max(temperatureClean);

% Display results
fprintf("Average Humidity = %.2f\n", avgHumidity);
fprintf("Max Humidity = %.2f\n", maxHumidity);

fprintf("Average Temperature = %.2f\n", avgTemp);
fprintf("Max Temperature = %.2f\n", maxTemp);

% -------------------------------
% 4. WRITE RESULTS BACK
% -------------------------------
thingSpeakWrite(channelID, [avgHumidity avgTemp], ...
    'Fields', [1 2], ...
    'WriteKey', writeAPIKey);

% -------------------------------
% 5. PLOT DATA
% -------------------------------
figure;

subplot(2,1,1);
plot(humidity, '-o');
title("Humidity Data");
xlabel("Sample Number");
ylabel("Humidity");
grid on;

subplot(2,1,2);
plot(temperature, '-o');
title("Temperature Data");
xlabel("Sample Number");
ylabel("Temperature");
grid on;
