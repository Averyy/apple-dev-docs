# sourceFrame

**Framework**: WebKit  
**Kind**: property

The frame that requested the navigation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var sourceFrame: WKFrameInfo { get }
```

## See Also

- [var request: URLRequest](wknavigationaction/request.md)
  The URL request object associated with the navigation action.
- [var targetFrame: WKFrameInfo?](wknavigationaction/targetframe.md)
  The frame in which to display the new content.
- [var shouldPerformDownload: Bool](wknavigationaction/shouldperformdownload.md)
  A Boolean value that indicates whether the web content provided an attribute that indicates a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/sourceframe)*