# Feature Detection Keys

**Framework**: Core Image

Keys used in the options dictionary for [`features(in:options:)`](cidetector/features(in:options:).md).

## Topics

### Constants
- [let CIDetectorImageOrientation: String](cidetectorimageorientation.md)
  An option for the display orientation of the image whose features you want to detect.
- [let CIDetectorEyeBlink: String](cidetectoreyeblink.md)
  An option for whether Core Image will perform additional processing to recognize closed eyes in detected faces.
- [let CIDetectorSmile: String](cidetectorsmile.md)
  An option for whether Core Image will perform additional processing to recognize smiles in detected faces.
- [let CIDetectorFocalLength: String](cidetectorfocallength.md)
  An option identifying the focal length in pixels used in capturing images to be processed by the detector.
- [let CIDetectorAspectRatio: String](cidetectoraspectratio.md)
  An option specifying the aspect ratio (width divided by height) of rectangles to search for.
- [let CIDetectorReturnSubFeatures: String](cidetectorreturnsubfeatures.md)
  An option specifying whether to return feature information for components of detected features.

## See Also

- [Detector Types](detector-types.md)
  Strings used to declare the detector for which you are interested.
- [Detector Configuration Keys](detector-configuration-keys.md)
  Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](detector-accuracy-options.md)
  Value options used to specify the desired accuracy of the detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/feature-detection-keys)*