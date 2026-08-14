# DownloadableAssetsRequestStatus

**Framework**: Vision  
**Kind**: enum

The status of the assets required by a [`DownloadableAssetsRequest`](downloadableassetsrequest.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum DownloadableAssetsRequestStatus
```

## Topics

### Download status cases
- [DownloadableAssetsRequestStatus.error(_:)](downloadableassetsrequeststatus/error(_:).md)
  The asset download failed with an error.
- [DownloadableAssetsRequestStatus.notReady](downloadableassetsrequeststatus/notready.md)
  The assets are not ready or the status is unknown. Call [`downloadAssets()`](downloadableassetsrequest/downloadassets().md) or [`downloadAssets(progress:)`](downloadableassetsrequest/downloadassets(progress:).md) to initiate the download.
- [DownloadableAssetsRequestStatus.ready](downloadableassetsrequeststatus/ready.md)
  The assets are ready.
- [DownloadableAssetsRequestStatus.downloading](downloadableassetsrequeststatus/downloading.md)
  The assets are being downloaded. Check progress through the subprogress that was passed to [`downloadAssets(progress:)`](downloadableassetsrequest/downloadassets(progress:).md).

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [protocol DownloadableAssetsRequest](downloadableassetsrequest.md)
  A request whose execution depends on assets that may need to be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequeststatus)*