# DownloadableAssetsRequest

**Framework**: Vision  
**Kind**: protocol

A request whose execution depends on assets that may need to be downloaded.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol DownloadableAssetsRequest
```

#### Overview

Inspect [`assetStatus`](downloadableassetsrequest/assetstatus.md) to determine whether the required assets are ready, and call [`downloadAssets()`](downloadableassetsrequest/downloadassets().md) to initiate the download when they are not.

## Topics

### Getting the asset status
- [var assetStatus: DownloadableAssetsRequestStatus](downloadableassetsrequest/assetstatus.md)
  The current download status of the assets required by the request.
### Downloading assets
- [func downloadAssets() async throws](downloadableassetsrequest/downloadassets.md)
  Downloads the assets required to perform the request.
- [func downloadAssets(progress: consuming Subprogress) async throws](downloadableassetsrequest/downloadassets(progress:).md)
  Downloads the assets required to perform the request, reporting progress through the provided subprogress.

## Relationships

### Conforming Types
- [GenerateIterativeSegmentationRequest](generateiterativesegmentationrequest.md)

## See Also

- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [protocol StatefulRequest](statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.
- [protocol TargetedRequest](targetedrequest.md)
  A type for analyzing two images together.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.
- [enum DownloadableAssetsRequestStatus](downloadableassetsrequeststatus.md)
  The status of the assets required by a [`DownloadableAssetsRequest`](downloadableassetsrequest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequest)*