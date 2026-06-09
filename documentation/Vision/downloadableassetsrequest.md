# DownloadableAssetsRequest

**Framework**: Vision  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol DownloadableAssetsRequest
```

## Topics

### Instance Properties
- [var assetStatus: DownloadableAssetsRequestStatus](downloadableassetsrequest/assetstatus.md)
### Instance Methods
- [func downloadAssets() async throws](downloadableassetsrequest/downloadassets.md)
- [func downloadAssets(progress: consuming Subprogress) async throws](downloadableassetsrequest/downloadassets(progress:).md)
- [func downloadAssetsWithProgress() throws -> DownloadableAssetsProgress](downloadableassetsrequest/downloadassetswithprogress.md)

## Relationships

### Conforming Types
- [GenerateIterativeSegmentationRequest](generateiterativesegmentationrequest.md)
- [GenerateSelectedObjectSegmentationRequest](generateselectedobjectsegmentationrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequest)*