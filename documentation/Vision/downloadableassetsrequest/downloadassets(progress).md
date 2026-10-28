# downloadAssets(progress:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Downloads the assets required to perform the request, reporting progress through the provided subprogress.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func downloadAssets(progress: consuming Subprogress) async throws
```

## Mentions

- [Isolating an object from a tap, box, or scribble](../segmenting-objects-with-iterative-refinement.md)

## Discussion

> **Throws**: An error if the download fails.

## Parameters

- `progress`: A subprogress to which the download progress is attached.

## Default Implementations

### DownloadableAssetsRequest Implementations
- [func downloadAssets(progress: consuming Subprogress) async throws](./downloadassets%28progress%29-3mcyi.md)
  Downloads the assets required to perform the request, reporting progress through the provided subprogress.

## See Also

### Downloading assets
- [func downloadAssets() async throws](./downloadassets%28%29.md)
  Downloads the assets required to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequest/downloadassets(progress:))*