% Octave/Matlab array audio playback example

%% parameters
fs = 8000; % Hz
T = 1.; % second, arbitrary length of tone

%% 1 kHz sine wave, 1 second long, sampled at 8 kHz
t = 0:1/fs:T;
x = 0.9 * sin(2*pi*1000*t);  % 0.9 is arbitrary to avoid clipping sound card DAC

a = audioplayer(x,fs);
play(a)
