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
lat2 = 0;  % Latitude reference point
lon2 = 0;  % Longitude reference point

% Earth's radius in kilometers
R = 6371;

% Defining the start and end row indices
start_indices = [2, 144, 259, 381, 562, 703, 924, 1050, 1163, 1284];  % start indices
end_indices = [83, 195, 328, 461, 636, 778, 994, 1119, 1230, 1354];  % Example end indices

% Initialize cell array to store distances
distances = cell(size(start_indices));

% Calculating distances for each start and end point
for i = 1:numel(start_indices)
    start_idx = start_indices(i);
    end_idx = end_indices(i);
    
    % Extracting latitude and longitude for the current range
    lat_range = lat1(start_idx:end_idx);
    lon_range = lon1(start_idx:end_idx);
    
    % Calculating distances using the Haversine formula
    dlat = lat2 - lat_range;
    dlon = lon2 - lon_range;
    a = sin(dlat/2).^2 + cos(lat_range) .* cos(lat2) .* sin(dlon/2).^2;
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    distances{i} = R * c;
end

% Calculating the average distance
average_distances = cellfun(@mean, distances);

% Calculating the standard deviation of the distances
standard_deviations = cellfun(@std, distances);

% Displaying the average distances
disp('Average Distances:');
disp(average_distances);

% Displaying the standard deviations
disp('Standard Deviations:');
disp(standard_deviations);
