% compare with demo_findpeaks.py

try
pkg load signal %for GNU Octave
end

minpeakheight=2;
mindist=1; %arbitrary, try see what it does
minpeakwidth=0;

noisy = [1,3,5,2,1,5,5.01,0,2,4,6,0,7,1,0];
[~,pkind]=findpeaks(noisy,'MinPeakHeight',minpeakheight,'MinPeakDistance',mindist,...
                   'MinPeakWidth',minpeakwidth);
               
figure(1),clf(1),hold('on')
plot(noisy,'k')
plot(pkind,noisy(pkind),'*r')
xlabel('index (one-based)')
ylabel('value')

disp(['peaks at indices ',num2str(pkind)])