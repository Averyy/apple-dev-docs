# Implementing saliency-based image cropping in iOS and watchOS

**Framework**: Vision

Crop regions most likely drawing people’s attention from an image in your iOS or watchOS app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC26 session 237: [`What’s new in image understanding`](https://developer.apple.comhttps://developer.apple.com/wwdc26/237/).

#### Configure the Sample Code Project

To configure the sample code project, do the following:

1. Open the sample with the latest version of Xcode.
2. Set the developer team for all targets to let Xcode automatically manage the provisioning profile. For more information, see [`Set the bundle ID`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution#Set-the-bundle-ID) and [`Assign the project to a team`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution#Assign-the-project-to-a-team).

> **Note**: This sample code needs to run on a physical device.

## See Also

- [Generating high-quality thumbnails from videos](generating-thumbnails-from-videos.md)
  Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.
- [struct CalculateImageAestheticsScoresRequest](calculateimageaestheticsscoresrequest.md)
  A request that analyzes an image for aesthetically pleasing attributes.
- [struct DetectLensSmudgeRequest](detectlenssmudgerequest.md)
  A request that detects a smudge on a lens from an image or video frame capture.
- [struct GenerateAttentionBasedSaliencyImageRequest](generateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [struct GenerateObjectnessBasedSaliencyImageRequest](generateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/implementing-saliency-based-image-cropping-in-ios-and-watchos)*