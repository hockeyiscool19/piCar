#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

class MyClass {
    public:
        int num;
        string str;
};


int main() {
    
    MyClass myObj;
    myObj.num = 5;
    myObj.str = "Hello";
    cout << myObj.num << " " << myObj.str << "\n";


    string image_path = samples::findFile("starry.png");
    Mat img = imread(image_path, IMREAD_COLOR);
    if(img.empty())
    {
        cout << "Could not read the image: " << image_path << endl;
        return 1;
    }
    imshow("Display window", img);
    int k = waitKey(0); // Wait for a keystroke in the window
    if(k == 's')
    
    {
        imwrite("starry_night.png", img);
    }

    
    cout << "done with small images" << endl;
    cout << "Attempting video Capture\n";

    cv::VideoCapture cap(0); 
    
    // Check if camera opened successfully
    if(!cap.isOpened()){
      std::cout << "Error opening video stream or file" << std::endl;
      return -1;
    }
    
    while(1){
      cv::Mat frame;
      
      // Capture frame-by-frame
      cap >> frame;

      // If the frame is empty, break immediately
      if (frame.empty())
        break;
      
      // Display the resulting frame
      imshow( "Frame", frame );

      // Press  ESC on keyboard to exit
      char c = (char)cv::waitKey(25);
      if(c==27)
        break;
    }
    
    // When everything done, release the VideoCapture object
    cap.release();
    
    // Closes all the frames
    cv::destroyAllWindows();



    return 0;

}

