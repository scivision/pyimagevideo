%% test_readavi
% demo of loading an AVI and displaying the first frame of video
% helps determine if Matlab has a particular codec available
% 
%
% Michael Hirsch
%% Example: Matlab R2015a cannot read Cinepak encoded video.
% (1) I converted Cinepak AVI to uncompressed AVI with Linux Terminal command:
% ffmpeg -i ~/U/eng_research_irs/Auroral_Video/sCMOS_PFRR_Mar2012/CMOS_110302_0819.avi -vcodec rawvideo ~/CMOS_110302_0819.avi
% (2) I ran this Matlab program and it displayed the first frame of video successfully
%
% Note: uncompressed AVI file can be 20 times filesize of Cinepak AVI

function test_readavi()

fn = '~/CMOS_110302_0819.avi'; % uncompressed AVI "works for me" with Matlab R2015a on Linux
showFirstFrame(fn)
end

function showFirstFrame(fn)
if ~exist(fn,'file')
    disp([fn,' does not exist'])
    return
end
vid = VideoReader(fn);
disp(get(vid)) % print out everything known about this file
img = readFrame(vid);
figure()
imagesc(img)
title(fn,'interpreter','none')
end