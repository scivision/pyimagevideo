% demo of lossless MPEG 2000 encoding with matlab for plots
v = VideoWriter('test.mj2','Motion JPEG 2000');
v.LosslessCompression = true; v.FrameRate=5;
open(v)
f=figure; title('line'), ylabel('amplitude'),xlabel('index')
pause(0.2) %let plot wake up
for i=1:.05:3; 
    line(0:.01:1,(0:.01:1).^i)
    im = getframe(f);
    writeVideo(v,im)
end
close(v)
