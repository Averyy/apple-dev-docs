# Segmenting objects using taps, scribbles or rectangles

**Framework**: Vision

Select objects or regions in a photo using taps, scribbles, or rectangle selection, and generate a segmentation mask using the iterative segmentation API.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC26 session 237: [`What’s new in image understanding`](https://developer.apple.comhttps://developer.apple.com/wwdc26/237/).

#### Configure the Sample Code Project

To configure the sample code project:

1. Open the sample with the latest version of Xcode.
2. Set the developer team for all targets to let Xcode automatically manage the provisioning profile. For more information, see [`Set the bundle ID`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution#Set-the-bundle-ID) and [`Assign the project to a team`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution#Assign-the-project-to-a-team).

> **Note**: This sample code needs to run on a physical device.

## See Also

- [struct GenerateForegroundInstanceMaskRequest](generateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticeable objects to separate from the background.
- [struct GeneratePersonInstanceMaskRequest](generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [class GeneratePersonSegmentationRequest](generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.
- [class GenerateIterativeSegmentationRequest](generateiterativesegmentationrequest.md)
  A request that generates a segmentation mask from points, a rectangle, or a scribble.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/segmenting-objects-using-taps-scribbles-or-rectangles)*