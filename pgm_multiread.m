% Reads PGM image stack (multi-image) file
% Michael HIrsch, Ph.D.
function imgs = pgm_multiread(fn,verbose)
  
  if nargin<2, verbose=true, end
  if ~exist(fn,'file'), error([fn,' does not exist']), end
    
  fid = fopen(fn,'r');

  [xy, prec] = pgmheader(fid,verbose);
%% read image stack
  i = 1;
  while ~feof(fid)
    imgs(:,:,i) = fread(fid,flip(xy),prec,0,'l');
    xy = pgmheader(fid,verbose);
    i = i+1;
  end % while
%% cleanup
  fclose(fid);
end % function


function [xy,prec] = pgmheader(fid,verbose)
  % parses PGM text header (even P5 has text header)
  if nargin<2, verbose=true, end
    
  if ischar(fid), fid=fopen(fid,'r'); end
  
  %% validate magic number
  Nmag = 'P5';
  mag = fgets(fid,2);
  
  if mag==-1 % EOF
    xy=[]; prec=[];
    return
  end
  
  assert(strcmp(mag,Nmag),['Wrong Magic Number ',mag,' exprected ',Nmag])
%% find size of image
  lin = strtrim(fgetl(fid));
  while ~feof(fid) && (length(lin) == 0 || lin(1) == "#")
    lin = strtrim(fgetl(fid));
    if verbose,disp(lin), end
  end % while
  xy = cell2mat(textscan(lin,'%u %u'));
%% find maximum intensity value (typically 256 (8-bit) or 65535 (16-bit))
  lin = fgetl(fid);
  maxval = cell2mat(textscan(lin,'%u'));
  
  if maxval <= 255
    prec = 'uint8';
  else
    prec = 'uint16';
  end % if
  
end % function