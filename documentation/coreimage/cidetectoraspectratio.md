# CIDetectorAspectRatio

**Framework**: Core Image  
**Kind**: var

An option specifying the aspect ratio (width divided by height) of rectangles to search for.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorAspectRatio: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object whose value is a positive floating-point number. Use this option with the [`CIDetectorTypeRectangle`](cidetectortyperectangle.md) detector type to fine-tune the accuracy of the detector. For example, to more accurately find a business card (3.5 x 2 inches) in an image, specify an aspect ratio of `1.75` (3.5 / 2).

## See Also

- [let CIDetectorImageOrientation: String](cidetectorimageorientation.md)
  An option for the display orientation of the image whose features you want to detect.
- [let CIDetectorEyeBlink: String](cidetectoreyeblink.md)
  An option for whether Core Image will perform additional processing to recognize closed eyes in detected faces.
- [let CIDetectorSmile: String](cidetectorsmile.md)
  An option for whether Core Image will perform additional processing to recognize smiles in detected faces.
- [let CIDetectorFocalLength: String](cidetectorfocallength.md)
  An option identifying the focal length in pixels used in capturing images to be processed by the detector.
- [let CIDetectorReturnSubFeatures: String](cidetectorreturnsubfeatures.md)
  An option specifying whether to return feature information for components of detected features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)*