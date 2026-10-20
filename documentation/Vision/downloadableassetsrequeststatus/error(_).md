# DownloadableAssetsRequestStatus.error(_:)

**Framework**: Vision  
**Kind**: case  
**Role**: Case

The asset download failed with an error.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case error(any Error)
```

## See Also

### Download status cases
- [DownloadableAssetsRequestStatus.notReady](./notready.md)
  The assets are not ready or the status is unknown. Call [`downloadAssets()`](../downloadableassetsrequest/downloadassets%28%29.md) or [`downloadAssets(progress:)`](../downloadableassetsrequest/downloadassets%28progress%29.md) to initiate the download.
- [DownloadableAssetsRequestStatus.ready](./ready.md)
  The assets are ready.
- [DownloadableAssetsRequestStatus.downloading](./downloading.md)
  The assets are being downloaded. Check progress through the subprogress that was passed to [`downloadAssets(progress:)`](../downloadableassetsrequest/downloadassets%28progress%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequeststatus/error(_:))*