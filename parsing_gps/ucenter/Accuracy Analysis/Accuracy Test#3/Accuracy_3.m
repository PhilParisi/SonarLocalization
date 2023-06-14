% Specify the filename of your CSV file
filename = 'Lat_Lon_Conversion_Test.csv';

% Read the data from the CSV file
data = readtable(filename);

% Extract latitude and longitude columns
longitude = data(:, 2).Variables;
latitude = data(:, 3).Variables;

% Convert latitude and longitude to radians
lat1 = deg2rad(latitude);
lon1 = deg2rad(longitude);
lat2 = 0;  % Latitude reference point (e.g., 0 or any other desired point)
lon2 = 0;  % Longitude reference point (e.g., 0 or any other desired point)

% Earth's radius in kilometers
R = 6371;

% Define the start and end row indices for the base case
base_start_indices = [2, 144, 259, 381, 562, 703, 924, 1050, 1163, 1284];  % start indices
base_end_indices = [83, 195, 328, 461, 636, 778, 994, 1119, 1230, 1354];  % Example end indices

% Preallocate table to store base case distances
num_points = numel(base_start_indices);
base_resultTable = table((1:num_points)', zeros(num_points, 1), zeros(num_points, 1), 'VariableNames', {'Point', 'Avg_Distance', 'Std_Deviation'});

% Calculate distances for each start and end point in the base case
for i = 1:num_points
    % Extract latitude and longitude for the current range
    lat_range = lat1(base_start_indices(i):base_end_indices(i));
    lon_range = lon1(base_start_indices(i):base_end_indices(i));
    
    % Calculate distances using the Haversine formula
    dlat = lat2 - lat_range;
    dlon = lon2 - lon_range;
    a = sin(dlat/2).^2 + cos(lat_range) .* cos(lat2) .* sin(dlon/2).^2;
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    distances = R * c;
    
    % Calculate average distance
    avg_distance = mean(distances);
    
    % Calculate standard deviation
    std_deviation = std(distances);
    
    % Assign values to the base result table
    base_resultTable.Avg_Distance(i) = avg_distance;
    base_resultTable.Std_Deviation(i) = std_deviation;
end

% Format the Avg_Distance column with significant figures and units
avg_distance_formatted = compose('%.4f km', base_resultTable.Avg_Distance);
base_resultTable.Avg_Distance = avg_distance_formatted;

% Display the base result table
disp("Base Case Result:");
disp(base_resultTable);


%% Test 3
% Specify the filename of your CSV file
filename = 'Test$3$.csv';

% Read the data from the CSV file
data = readtable(filename);

% Extract latitude and longitude columns
longitude = data(:, 2).Variables;
latitude = data(:, 3).Variables;

% Convert latitude and longitude to radians
lat1 = deg2rad(latitude);
lon1 = deg2rad(longitude);
lat2 = 0;  % Latitude reference point (e.g., 0 or any other desired point)
lon2 = 0;  % Longitude reference point (e.g., 0 or any other desired point)

% Earth's radius in kilometers
R = 6371;

% Define the start and end row indices
start_indices = [2, 127, 237, 353, 471, 604, 767, 870, 960, 1059];  % start indices
end_indices = [90, 198, 319, 417, 542, 686, 844, 929, 1020, 1139];  % end indices

% Preallocate table to store distances
num_points = numel(start_indices);
resultTable = table((1:num_points)', zeros(num_points, 1), zeros(num_points, 1), 'VariableNames', {'Point', 'Avg_Distance', 'Std_Deviation'});

% Calculate distances for each start and end point
for i = 1:num_points
    % Extract latitude and longitude for the current range
    lat_range = lat1(start_indices(i):end_indices(i));
    lon_range = lon1(start_indices(i):end_indices(i));
    
    % Calculate distances using the Haversine formula
    dlat = lat2 - lat_range;
    dlon = lon2 - lon_range;
    a = sin(dlat/2).^2 + cos(lat_range) .* cos(lat2) .* sin(dlon/2).^2;
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    distances = R * c;
    
    % Calculate average distance
    avg_distance = mean(distances);
    
    % Calculate standard deviation
    std_deviation = std(distances);
    
    % Assign values to the result table
    resultTable.Avg_Distance(i) = avg_distance;
    resultTable.Std_Deviation(i) = std_deviation;
end

% Format the Avg_Distance column with significant figures and units
avg_distance_formatted = compose('%.4f km', resultTable.Avg_Distance);
resultTable.Avg_Distance = avg_distance_formatted;

% Display the result table
disp(resultTable);


%% Difference between base case and Test 3
% Convert Avg_Distance columns to numeric values
base_resultTable.Avg_Distance = str2double(strrep(base_resultTable.Avg_Distance, ' km', ''));
resultTable.Avg_Distance = str2double(strrep(resultTable.Avg_Distance, ' km', ''));

% Calculate the difference between average distances in meters
difference = abs(resultTable.Avg_Distance - base_resultTable.Avg_Distance) * 1000;

% Add the difference column to the base result table
base_resultTable.Difference = difference;

% Display the updated base result table with difference in meters
disp("Base Case Result with Difference (in meters):");
disp(base_resultTable(:, [1, end]));







