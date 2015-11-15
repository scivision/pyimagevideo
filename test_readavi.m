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

function test_readavi(vidfn)
% get ready to read
vid = setupavi(fn1);
img1 = readimg(vidfn);
% display
dispvid(img1,fn1)
% threshold
mask = thresmax(img1,img2);
dispvid(mask,'mask')

filt = img1;
filt(mask) = 0;

%imwrite(filt,'test.png')

end

function thres = thresmax(I1,I2)
%keeps only pixels above a threshold
% using 246 b/c due to compression artifacts some ticks are <255
thr = 120;
thres = I1(:,:,1)>thr & I2(:,:,1)>thr; %TODO only using one channel
end

function img = readimg(vid,frm)
disp(get(vid)) % print out everything known about this file

j=1;
for i=frm
imc = read(vid,i);
im = imc(:,:,1);%mean(imc,3,'double');
img(:,:,j) = im(70:802,300:950); %first(70:802,177:1114,1);
j= j+1; 
end

if ndims(img)==3
    img = mean(img,3,'native'); 
end
end

function dispvid(img,ttxt)

f=figure(); ax=axes('parent',f);
imagesc(img)
colormap(ax,'gray')
colorbar('peer',ax)
title(ttxt,'interpreter','none','fontsize',10)



end

function vid =  setupavi(fn)
if ~exist(fn,'file')
    disp([fn,' does not exist'])
    return
end

try
    vid = VideoReader(fn);
catch exc
    disp(exc.message)
    disp(['sorry, I couldnt read ',fn,'  maybe I dont have the right codec.'])
    return
end
end
