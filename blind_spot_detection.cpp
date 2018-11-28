
/*
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>


*/

#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>


using namespace cv;
using namespace std;


int main(int argc, char** argv)
{
        Mat img;

        // capture from test video file
        VideoCapture cap("/home/learningbee/Desktop/PPT_SC/Day_1/shift_2/source_code/pjt1_car_detection/code/cpp/test/video4.mp4");
        //capture from web camera init
        //VideoCapture cap(0);
        //cap.open(0);


        // Load cascate classifier placed in sulution folder
        CascadeClassifier detector;
        string cascadeName = "/home/learningbee/Desktop/PPT_SC/Day_1/shift_2/source_code/pjt1_car_detection/code/cpp/cars.xml";
        bool loaded = detector.load(cascadeName);

        // Parameters of detectMultiscale Cascade Classifier
        int min_neighbours = 2;
        double scaleStep = 1.1;
        Size minimalObjectSize(80, 80);
        Size maximalObjectSize(200, 200);

        // Vector of returned faces
        vector<Rect> found;


        for (;;)
        {

                // Image from camera to Mat

                cap >> img;
                //img = imread("test/pic1.jpg", CV_LOAD_IMAGE_COLOR);
                // Convert input to greyscale
                Mat image_grey;
                cvtColor(img, image_grey, CV_BGR2GRAY);

                // why not
                found.clear();

                // Detect cars
                detector.detectMultiScale(image_grey, found, scaleStep, min_neighbours,2, minimalObjectSize, maximalObjectSize);
                // Draw the rectangular box
                if (found.size() > 0) {
                        for (int i = 0; i <= found.size() - 1; i++) {
                                rectangle(img, found[i].br(), found[i].tl(), Scalar(0, 0, 255), 2, 8, 0);
                        }
                }

                //Show the results

                imshow("output", img);
                char c = (char)waitKey(1);
                if( c == 27 || c == 'q' || c == 'Q' )
                    break;

        }
        return 0;
}
