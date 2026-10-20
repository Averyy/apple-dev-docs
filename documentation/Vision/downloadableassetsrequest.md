# DownloadableAssetsRequest

**Framework**: Vision  
**Kind**: protocol  
**Role**: Protocol

A request whose execution depends on assets that may need to be downloaded.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol DownloadableAssetsRequest
```

#### Overview

Inspect [`assetStatus`](./downloadableassetsrequest/assetstatus.md) to determine whether the required assets are ready, and call [`downloadAssets()`](./downloadableassetsrequest/downloadassets%28%29.md) to initiate the download when they are not.

## Topics

### Getting the asset status
- [var assetStatus: DownloadableAssetsRequestStatus](./downloadableassetsrequest/assetstatus.md)
  The current download status of the assets required by the request.
### Downloading assets
- [func downloadAssets() async throws](./downloadableassetsrequest/downloadassets%28%29.md)
  Downloads the assets required to perform the request.
- [func downloadAssets(progress: consuming Subprogress) async throws](./downloadableassetsrequest/downloadassets%28progress%29.md)
  Downloads the assets required to perform the request, reporting progress through the provided subprogress.

## Relationships

### Conforming Types
- [GenerateIterativeSegmentationRequest](./generateiterativesegmentationrequest.md)

## See Also

### Protocols
- [protocol ImageProcessingRequest](./imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [protocol PoseProviding](./poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [protocol StatefulRequest](./statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.
- [protocol TargetedRequest](./targetedrequest.md)
  A type for analyzing two images together.
- [protocol VisionObservation](./visionobservation.md)
  A type for objects produced by image-analysis requests.
- [protocol VisionRequest](./visionrequest.md)
  A type for image-analysis requests.
- [enum DownloadableAssetsRequestStatus](./downloadableassetsrequeststatus.md)
  The status of the assets required by a [`DownloadableAssetsRequest`](./downloadableassetsrequest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequest)*