start_crop_x = 6900;
start_crop_y = 4200;

cr = {[6900,7100],[4200,4400]};
% Red
B4 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B4.TIF', 'PixelRegion', cr);
% Green
B3 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B3.TIF', 'PixelRegion', cr);
% Blue
B2 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B2.TIF', 'PixelRegion', cr);

rgbImage = cat(3, B4, B3, B2);
imshow(rgbImage);

%NIR
B5 = imread('f:\edu\Research\dataset\Test_Misuri\landsat\LC80230342014186LGN01_B5.TIF', 'PixelRegion', cr);


% Compute NDVI
NDVI = double(B5 - B4) ./ double(B5 + B4);
imshow(NDVI, 'DisplayRange', [-1 1]);


GT = imread('f:\edu\Research\dataset\Test_Misuri\ground_truth_v1_16colors.png');

size(GT)
yellow = 0;
blue = 0;
red = 0;
green = 0;
dataset = [0.1 0.2 0.3 0.4 0];
for row=1:size(GT,1) 
    for col=1:size(GT,2)
        class = 0;
        if (GT(row,col,1) == 255 && GT(row,col,2) == 255 && GT(row,col,3) == 0) 
            yellow = yellow + 1;
            class = 1; 
        end
        if (GT(row,col,1) == 0 && GT(row,col,2) == 255 && GT(row,col,3) == 255) 
            blue = blue + 1;
            class = 2;
        end
        if (GT(row,col,1) == 255 && GT(row,col,2) == 0 && GT(row,col,3) == 0) 
            red = red + 1;
            class = 3;
        end
        if (GT(row,col,1) == 0 && GT(row,col,2) == 128 && GT(row,col,3) == 128) 
            green = green + 1;
            class = 4;
        end
        
        if (class > 0)
            % we have a new data set entry
            double(NDVI(row, col));
            entry = [double(B2(row, col)) double(B3(row, col)) double(B4(row, col)) double(NDVI(row, col)) double(class)];
            size(dataset)
            size(entry)
            dataset = [dataset; entry];
        end
    end
end
size(dataset)
csvwrite('f:\edu\Research\dataset\Test_Misuri\dataset_v1.csv', dataset);
%yellow 
%blue
%red
%green
%dataset

