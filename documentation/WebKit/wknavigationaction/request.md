# request

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The URL request object associated with the navigation action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var request: URLRequest { get }
```

```objc
@property (nonatomic, copy, readonly) NSURLRequest * request;
```

## See Also

### Inspecting navigation information
- [var sourceFrame: WKFrameInfo](./sourceframe.md)
  The frame that requested the navigation.
- [var targetFrame: WKFrameInfo?](./targetframe.md)
  The frame in which to display the new content.
- [var shouldPerformDownload: Bool](./shouldperformdownload.md)
  A Boolean value that indicates whether the web content provided an attribute that indicates a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/request)*