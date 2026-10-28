# Implementing saliency-based image cropping in iOS and watchOS

**Framework**: Vision  
**Role**: Sample Code  
**Download**: [ImplementingSaliencyBasedImageCroppingInIOSAndWatchOS.zip](https://docs-assets.developer.apple.com/published/6bca173a2580/ImplementingSaliencyBasedImageCroppingInIOSAndWatchOS.zip)

Crop regions most likely drawing people’s attention from an image in your iOS or watchOS app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Overview

> **Note**: This sample code project is associated with WWDC26 session 237: [What’s new in image understanding](https://developer.apple.com/wwdc26/237/).

## Configure the sample code project

To configure the sample code project, do the following:

1. Open the sample with the latest version of Xcode.
2. Set the developer team for all targets to let Xcode automatically manage the provisioning profile. For more information, see [Set the bundle ID](../Xcode/preparing-your-app-for-distribution.md#Set-the-bundle-ID) and [Assign the project to a team](../Xcode/preparing-your-app-for-distribution.md#Assign-the-project-to-a-team).

> **Note**: This sample code needs to run on a physical device.

## See Also

### Image quality and saliency analysis
- [Generating high-quality thumbnails from videos](./generating-thumbnails-from-videos.md)
  Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.
- [struct CalculateImageAestheticsScoresRequest](./calculateimageaestheticsscoresrequest.md)
  A request that analyzes an image for aesthetically pleasing attributes.
- [struct DetectLensSmudgeRequest](./detectlenssmudgerequest.md)
  A request that detects a smudge on a lens from an image or video frame capture.
- [struct GenerateAttentionBasedSaliencyImageRequest](./generateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [struct GenerateObjectnessBasedSaliencyImageRequest](./generateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/implementing-saliency-based-image-cropping-in-ios-and-watchos)*