# targetFrame

**Framework**: Webkit  
**Kind**: property

The frame in which to display the new content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var targetFrame: WKFrameInfo? { get }
```

#### Discussion

If the target of the navigation is a new window, this property is `nil`.

## See Also

- [var request: URLRequest](wknavigationaction/request.md)
  The URL request object associated with the navigation action.
- [var sourceFrame: WKFrameInfo](wknavigationaction/sourceframe.md)
  The frame that requested the navigation.
- [var shouldPerformDownload: Bool](wknavigationaction/shouldperformdownload.md)
  A Boolean value that indicates whether the web content provided an attribute that indicates a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/targetframe)*