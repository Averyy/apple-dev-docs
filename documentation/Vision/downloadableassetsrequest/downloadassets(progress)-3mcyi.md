# downloadAssets(progress:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

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

#### Discussion

> **Throws**: An error if the download fails.

## Parameters

- `progress`: A subprogress to which the download progress is attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/downloadableassetsrequest/downloadassets(progress:)-3mcyi)*