%% Load & Plot Data
clc, clear all, close all, format compact

data = load("LWW_Song.mat");

Fs = data.Fs; % 800 samples/sec
data = data.Data; data = data';

t = (0:length(data)-1)/Fs;  % Samples / (Samples/Sec) = Secs

%%
clc, close all
% Butterworth Filter
n = 4; beginF = 20; endF = 80;
[b,a] = butter(n, [beginF/ (Fs/2) , endF / (Fs/2)]);
data_bs = filtfilt(b,a,data);

% Median Filtering
data_bs = sgolayfilt(data_bs, 3, Fs + 1);
%data_bs = medfilt1(data_bs, 1);

% Butterworth Filter
% n = 4; beginF = 45; endF = 55;
% [b,a] = butter(n, [beginF/ (Fs/2) , endF / (Fs/2)]);
% data_bs = filtfilt(b,a,data);

% Spectrogram
NFFT = Fs;
NOVERLAP = round(.8*NFFT);
spectrogram(data_bs, NFFT, NOVERLAP, [0:0.2:110], Fs, 'yaxis')
title('Spectrogram Post-Butterworth')
