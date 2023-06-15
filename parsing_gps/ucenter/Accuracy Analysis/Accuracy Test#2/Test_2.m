%% Base Case
% Specify the filename of your CSV file
filename = 'Test$2$.csv';

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
start_indices = [2, 140, 249, 355, 501, 658, 823, 937, 1029, 1141];  % start indices
end_indices = [99, 208, 332, 444, 595, 743, 904, 1001, 1089, 1219];  % end indices

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
