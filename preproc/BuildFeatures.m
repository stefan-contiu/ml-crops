start_crop_x = 6900;
start_crop_y = 7100;

cr = {[6900,7100],[4200,4400]};
% Red
B4 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B4.TIF', 'PixelRegion', cr);
% Green
B3 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B3.TIF', 'PixelRegion', cr);
% Blue
B2 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B2.TIF', 'PixelRegion', cr);

%R = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B4.TIF');
%G = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B3.TIF');
%B = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B2.TIF');

rgbImage = cat(3, B4, B3, B2);
imshow(rgbImage);

%NIR
B5 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B5.TIF', 'PixelRegion', cr);


% Compute NDVI
NDVI = double(B5 - B4) ./ double(B5 + B4);
imshow(NDVI, 'DisplayRange', [-1 1]);


GT = imread('f:\edu\Research\dataset\Test_Misuri\ground_truth_v1.png');
size(GT)
yellow = 0;
for row=1:size(GT,1) 
    for col=1:size(GT,2)
        class = '';
        if (GT(row,col,1) == 255 && GT(row,col,2) == 244 && GT(row,col,3) == 0) 
            yellow = yellow + 1;
            class = 'yellow';
        end
        
        if (class <> '')
            % we have a new feature
        end
    end
end
size(B4)
yellow
