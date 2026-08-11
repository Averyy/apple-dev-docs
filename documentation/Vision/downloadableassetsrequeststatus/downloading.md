# DownloadableAssetsRequestStatus.downloading

**Framework**: Vision  
**Kind**: case

The assets are being downloaded. Check progress through the subprogress that was passed to [`downloadAssets(progress:)`](downloadableassetsrequest/downloadassets(progress:).md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case downloading
```

## See Also

- [DownloadableAssetsRequestStatus.error(_:)](downloadableassetsrequeststatus/error(_:).md)
  The asset download failed with an error.
- [DownloadableAssetsRequestStatus.notReady](downloadableassetsrequeststatus/notready.md)
  The assets are not ready or the status is unknown. Call [`downloadAssets()`](downloadableassetsrequest/downloadassets().md) or [`downloadAssets(progress:)`](downloadableassetsrequest/downloadassets(progress:).md) to initiate the download.
- [DownloadableAssetsRequestStatus.ready](downloadableassetsrequeststatus/ready.md)
  The assets are ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequeststatus/downloading)*