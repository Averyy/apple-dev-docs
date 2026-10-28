# Segmenting objects using taps, scribbles or rectangles

**Framework**: Vision  
**Role**: Sample Code  
**Download**: [SegmentingObjectsUsingTapsScribblesOrRectangles.zip](https://docs-assets.developer.apple.com/published/a5070681a498/SegmentingObjectsUsingTapsScribblesOrRectangles.zip)

Select objects or regions in a photo using taps, scribbles, or rectangle selection, and generate a segmentation mask using the iterative segmentation API.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- Xcode 27.0+

## Overview

> **Note**: This sample code project is associated with WWDC26 session 237: [What’s new in image understanding](https://developer.apple.com/wwdc26/237/).

## Configure the sample code project

To configure the sample code project:

1. Open the sample with the latest version of Xcode.
2. Set the developer team for all targets to let Xcode automatically manage the provisioning profile. For more information, see [Set the bundle ID](../Xcode/preparing-your-app-for-distribution.md#Set-the-bundle-ID) and [Assign the project to a team](../Xcode/preparing-your-app-for-distribution.md#Assign-the-project-to-a-team).

> **Note**: This sample code needs to run on a physical device.

## See Also

### Image segmentation and subject lifting
- [Isolating an object from a tap, box, or scribble](./segmenting-objects-with-iterative-refinement.md)
  Generate and refine a mask that isolates an object in an image based on a person’s selection.
- [struct GenerateForegroundInstanceMaskRequest](./generateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticeable objects to separate from the background.
- [struct GeneratePersonInstanceMaskRequest](./generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [class GeneratePersonSegmentationRequest](./generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.
- [class GenerateIterativeSegmentationRequest](./generateiterativesegmentationrequest.md)
  A request that generates a segmentation mask from points, a rectangle, or a scribble.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/segmenting-objects-using-taps-scribbles-or-rectangles)*