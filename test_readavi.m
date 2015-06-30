%% test_readavi
% demo of loading an AVI and displaying the first frame of video
% helps determine if Matlab has a particular codec available
% Michael Hirsch

function test_readavi()

% uncompressed file can be 20 times size of original (ouch says the hard drive)
% converted CinePak avi to uncompressed avi with command:
% ffmpeg -i ~/U/eng_research_irs/Auroral_Video/sCMOS_PFRR_Mar2012/CMOS_110302_0819.avi -vcodec rawvideo ~/CMOS_110302_0819.avi
fn = '~/CMOS_110302_0819.avi'; % "works for me" with Matlab R2015a on Linux
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