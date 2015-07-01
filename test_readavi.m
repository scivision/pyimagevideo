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

fn = '~/U/eng_research_irs/Auroral_Video/X1387_032307_112005.36_short_30fps.avi'; % uncompressed AVI "works for me" with Matlab R2015a on Linux
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
f=figure(); ax=axes('parent',f);
imagesc(img)
colormap(ax,'gray')
colorbar('peer',ax)
title(fn,'interpreter','none','fontsize',10)
end