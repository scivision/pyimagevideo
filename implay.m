% for Octave that didn't yet have native implay()

function implay(imgs,fps)
  
  N = ndims(imgs);
  assert(N==3 || N==4,'need 3D or 4D (color) image stack')
  
  figure
  if N==3
    h = imagesc(imgs(:,:,1));
    K = size(imgs,3);
  else
    h = imagesc(imgs(:,:,:,1));
    K = size(imgs,4);
  end %if
  
  colormap('gray')
  colorbar
  axis('image')
  
  for i = 1:K
    
    if N==3
      set(h,'cdata',imgs(:,:,i))
    else
      set(h,'cdata',imgs(:,:,:,i))
    end % if
    
    title(int2str(i))
    
  drawnow; pause(0.1)  
  end % for

end %function