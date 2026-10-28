# Isolating an object from a tap, box, or scribble

**Framework**: Vision  
**Role**: Article

Generate and refine a mask that isolates an object in an image based on a person’s selection.

## Overview

When people interact with images in your app, they might want to select an object, such as an item on a desk or a subject in a photo. Vision provides [`GenerateIterativeSegmentationRequest`](./generateiterativesegmentationrequest.md) to generate an image mask that separates any selected object from its background.

Unlike automatic segmentation requests that detect specific categories like people or documents, iterative segmentation works with arbitrary objects based on coordinates your app provides:

- **Point**: A normalized coordinate at a tap location inside the object.
- **Bounding box**: A normalized rectangle enclosing the object, useful for regional selections or grouping nearby items.
- **Scribble**: A pixel buffer containing drawn strokes across one or more objects.

Vision evaluates the image at those coordinates using an on-device machine-learning model and produces an alpha mask as a [`PixelBufferObservation`](./pixelbufferobservation.md). In the resulting mask, pixel values define the object’s silhouette against the background. Your app can then use this mask to highlight the selection, separate the object from its surroundings, or render a visual effect over the subject.

The following figure depicts an object in a photo isolated from its surroundings with an active mask overlay:

![A photograph of a ceramic dish on a shelf with an active pink mask overlay highlighting its silhouette against the surrounding objects.](https://developer.apple.com/tutorials/images/Vision/pottery-dish-mask-overview@2x.png)

Because an initial selection might miss parts of an object or include unwanted background areas, you can let people refine the mask:

1. **Initial selection**: The person selects an object by tapping it, drawing a rectangle around it, or scribbling across it. The request generates an initial mask.
2. **Refinement**: The person adds *include points* ([`addIncludedPoint(_:)`](./generateiterativesegmentationrequest/addincludedpoint%28_%29.md)) to expand the mask over missed parts of the object, or *exclude points* ([`addExcludedPoint(_:)`](./generateiterativesegmentationrequest/addexcludedpoint%28_%29.md)) to trim background areas that the mask covers.
3. **Updated mask**: Performing the request again with the same handler incorporates the new points and recalculates the mask.

To generate the mask, the request uses a machine-learning model that Vision downloads on demand to the device. For a working example that shows how to select and refine objects in a photo, see [Segmenting objects using taps, scribbles or rectangles](./segmenting-objects-using-taps-scribbles-or-rectangles.md).

## Download the model on first use

Before your app performs the request the first time on a device, check whether the model is ready and download it if it isn’t. Read the request’s [`assetStatus`](./downloadableassetsrequest/assetstatus.md) property to get the current state, and call [`downloadAssets()`](./downloadableassetsrequest/downloadassets%28%29.md) if the state is [`DownloadableAssetsRequestStatus.notReady`](./downloadableassetsrequeststatus/notready.md). The request throws an error if you perform it before Vision downloads the model.

```swift
let request = GenerateIterativeSegmentationRequest(seedPoint: NormalizedPoint(x: 0.5, y: 0.5))

switch await request.assetStatus {
case .ready:
    break
case .notReady:
    try await request.downloadAssets()
case .downloading, .error:
    return
@unknown default:
    return
}
```

The switch handles each [`DownloadableAssetsRequestStatus`](./downloadableassetsrequeststatus.md) case so the request only proceeds after the model is on the device. To report download progress in your app’s UI, use [`downloadAssets(progress:)`](./downloadableassetsrequest/downloadassets%28progress%29.md) instead.

## Create the request from the person’s selection

Choose one of three initializers based on how the person selected the object:

- For a tap on a single object, use [`init(seedPoint:_:)`](./generateiterativesegmentationrequest/init%28seedpoint,_%29.md) and pass a [`NormalizedPoint`](./normalizedpoint.md) at the tap location. A tap works well for simple objects.
- For a drag around a region, use [`init(seedBox:_:)`](./generateiterativesegmentationrequest/init%28seedbox,_%29.md) and pass a [`NormalizedRect`](./normalizedrect.md) that covers the drag. A rectangle can cover more than one object at a time, such as a cup and the saucer under it.
- For a scribble across one or more objects, use [`init(seedScribbleBuffer:_:)`](./generateiterativesegmentationrequest/init%28seedscribblebuffer,_%29.md) and pass a [`CVReadOnlyPixelBuffer`](../CoreVideo/cvreadonlypixelbuffer.md) with the stroke drawn into it. A scribble segments multiple objects at once. To create a read-only buffer from a scribble your app captured, draw the scribble strokes into a [`CVPixelBuffer`](../CoreVideo/cvpixelbuffer.md), and then convert it using [`init(unsafeBuffer:)`](../CoreVideo/cvreadonlypixelbuffer/init%28unsafebuffer%29.md).

The point and rectangle initializers use the Vision framework’s normalized coordinate system, where values run from `0` to `1` and the origin sits at the lower-left corner. This differs from [UIKit](../UIKit/UIKit.md) and [SwiftUI](../SwiftUI/SwiftUI.md), where the y-axis points down from the top left. Convert view coordinates to normalized coordinates and flip the y-axis before passing them to the request.

```swift
let pointRequest = GenerateIterativeSegmentationRequest(
    seedPoint: NormalizedPoint(x: 0.5, y: 0.5)
)

let boxRequest = GenerateIterativeSegmentationRequest(
    seedBox: NormalizedRect(x: 0.2, y: 0.3, width: 0.4, height: 0.5)
)

let scribbleRequest = GenerateIterativeSegmentationRequest(
    seedScribbleBuffer: CVReadOnlyPixelBuffer(unsafeBuffer: scribblePixelBuffer)
)
```

Each initializer accepts an optional revision parameter that pins the request to a specific algorithm revision. If you don’t pass one, the request uses the SDK’s default revision. To find the available revisions, check [`supportedRevisions`](./generateiterativesegmentationrequest/supportedrevisions.md).

## Perform the request

To generate the mask, run the request against the image using an [`ImageRequestHandler`](./imagerequesthandler.md). Create a handler for the image and call [`perform(_:)`](./imagerequesthandler/perform%28_%29-7b6g5.md) with the request. The result is a [`PixelBufferObservation`](./pixelbufferobservation.md) whose [`pixelBuffer`](./pixelbufferobservation/pixelbuffer.md) property contains the mask.

```swift
let request = GenerateIterativeSegmentationRequest(
    seedPoint: NormalizedPoint(x: 0.5, y: 0.5)
)
let handler = ImageRequestHandler(URL(filePath: "/path/to/image.jpg"))

let observation = try await handler.perform(request)
let mask = observation?.pixelBuffer
```

Reuse the same [`ImageRequestHandler`](./imagerequesthandler.md) instance when refining the mask. Reusing the handler preserves intermediate image representations in memory, allowing Vision to update the mask quickly as you add points without reloading the image.

## Refine the mask

To expand the mask, add an include point inside the object with [`addIncludedPoint(_:)`](./generateiterativesegmentationrequest/addincludedpoint%28_%29.md). To trim the mask, add an exclude point outside the object with [`addExcludedPoint(_:)`](./generateiterativesegmentationrequest/addexcludedpoint%28_%29.md). Perform the request through the same handler to get the updated mask.

The following figures show how adding include points expands the mask over omitted parts of an object:

![An initial mask covering the upper neck of a vase, with an unhighlighted lower vessel body.](https://developer.apple.com/tutorials/images/Vision/pottery-vase-refined-mask@2x.png)

![The refined mask extending down over the entire vase structure after adding include points.](https://developer.apple.com/tutorials/images/Vision/pottery-vase-initial-mask@2x.png)

```swift
try request.addIncludedPoint(NormalizedPoint(x: 0.6, y: 0.4))
try request.addExcludedPoint(NormalizedPoint(x: 0.2, y: 0.8))

let refinedObservation = try await handler.perform(request)
let refinedMask = refinedObservation?.pixelBuffer
```

The request holds up to 13 total points when you create it with a point or scribble, or 11 when you create it with a bounding box. Adding a point past this limit throws an error. To isolate a different object, create a new request and a new handler.

## Choose a mask quality level

Configure [`qualityLevel`](./generateiterativesegmentationrequest/qualitylevel-swift.property.md) before performing the request to balance mask resolution against processing time:

- [`GenerateIterativeSegmentationRequest.QualityLevel.fast`](./generateiterativesegmentationrequest/qualitylevel-swift.enum/fast.md): Generates a lower-resolution mask with the shortest processing time. Prioritizes responsiveness over fine edge detail.
- [`GenerateIterativeSegmentationRequest.QualityLevel.balanced`](./generateiterativesegmentationrequest/qualitylevel-swift.enum/balanced.md): The default setting. Balances mask fidelity with processing time.
- [`GenerateIterativeSegmentationRequest.QualityLevel.accurate`](./generateiterativesegmentationrequest/qualitylevel-swift.enum/accurate.md): Generates the highest-resolution mask with precise edge detail, but requires the most processing time.

The following figures compare mask edge fidelity across each quality level:

![A close-up view of an object processed with the fast quality setting, showing a coarse, stepped edge contour.](https://developer.apple.com/tutorials/images/Vision/pottery-dish-quality-fast@2x.png)

![A close-up view of the object processed with the balanced quality setting, showing a smooth edge contour.](https://developer.apple.com/tutorials/images/Vision/pottery-dish-quality-balanced@2x.png)

![A close-up view of the object processed with the accurate quality setting, showing a crisp, highly detailed silhouette conforming tightly to the object contour.](https://developer.apple.com/tutorials/images/Vision/pottery-dish-quality-accurate@2x.png)

The following code sets the quality level to accurate:

```swift
request.qualityLevel = .accurate
```

## See Also

### Image segmentation and subject lifting
- [Segmenting objects using taps, scribbles or rectangles](./segmenting-objects-using-taps-scribbles-or-rectangles.md)
  Select objects or regions in a photo using taps, scribbles, or rectangle selection, and generate a segmentation mask using the iterative segmentation API.
- [struct GenerateForegroundInstanceMaskRequest](./generateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticeable objects to separate from the background.
- [struct GeneratePersonInstanceMaskRequest](./generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [class GeneratePersonSegmentationRequest](./generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.
- [class GenerateIterativeSegmentationRequest](./generateiterativesegmentationrequest.md)
  A request that generates a segmentation mask from points, a rectangle, or a scribble.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/segmenting-objects-with-iterative-refinement)*