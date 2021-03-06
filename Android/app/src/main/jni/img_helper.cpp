#ifdef FORIPHONE
  #import <opencv2/opencv.hpp>
#else
  #include <opencv/cv.h>
#endif
#include <opencv2/core/core.hpp>
using namespace cv;

#include "img_helper.h"

/**
 * Resize an image to match a particular width while preserving aspect ratio.
 */
Mat img_helper::resizeSetWidth(Mat image, int width) {
  Mat newimage;
  double ratio = double(width) / image.cols;
  Size* dim = new Size(width, int(image.rows * ratio));
  resize(image, newimage, *dim, 0.0, 0.0, INTER_AREA);
  return newimage;
}
