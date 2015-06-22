<Query Kind="Program" />

/*
NW Corner Lat dec 	38.52862
NW Corner Long dec 	-90.46066
NE Corner Lat dec 	38.12853
NE Corner Long dec 	-88.33649
SE Corner Lat dec 	36.40548
SE Corner Long dec 	-88.87608
SW Corner Lat dec 	36.80427
SW Corner Long dec 	-90.95199
*/

double shift_y = 100;

// landsat scene corners north west, south east
double lc_x_0 = -90.95199;
double lc_y_0 = 38.52862;
double lc_x_1 = -88.33649;
double lc_y_1 = 36.40548;

// number of pixels in landsat scene
double p_x = 7991;
double p_y = 7861;

// coordinates of the area of interest

double aoi_x_0 = -89.5366;
double aoi_y_0 = 36.6702;
double aoi_x_1 = -89.4802;
double aoi_y_1 = 36.6186;


void Main()
{
	double crop_pixel_x0 = p_x * ((aoi_x_0 - lc_x_0)/(lc_x_1 - lc_x_0));	
	double crop_pixel_y0 = p_y * ((aoi_y_0 - lc_y_0)/(lc_y_1 - lc_y_0));
	double crop_pixel_x1 = p_x * ((aoi_x_1 - lc_x_0)/(lc_x_1 - lc_x_0));	
	double crop_pixel_y1 = p_y * ((aoi_y_1 - lc_y_0)/(lc_y_1 - lc_y_0));
	
	Console.WriteLine("Crop landsat TIF image from (start_row, end_row), (start_col, end_col) :"
	 	+ " (" + (int)crop_pixel_x0 + "," + (int)crop_pixel_x1 + ")"
	 	+ " (" + (int)crop_pixel_y0 + "," + (int)crop_pixel_y1 + ")");
	
	Console.WriteLine("\nResulting rectangle dimensions : " 
		+ ((int)crop_pixel_x1 - (int)crop_pixel_x0) 
		+ " x "
		+ ((int)crop_pixel_y1 - (int)crop_pixel_y0));
}

// Define other methods and classes here
