# request

**Framework**: Webkit  
**Kind**: property

The URL request object associated with the navigation action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var request: URLRequest { get }
```

## See Also

- [var sourceFrame: WKFrameInfo](wknavigationaction/sourceframe.md)
  The frame that requested the navigation.
- [var targetFrame: WKFrameInfo?](wknavigationaction/targetframe.md)
  The frame in which to display the new content.
- [var shouldPerformDownload: Bool](wknavigationaction/shouldperformdownload.md)
  A Boolean value that indicates whether the web content provided an attribute that indicates a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/request)*