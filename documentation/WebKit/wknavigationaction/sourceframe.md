# sourceFrame

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

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
var sourceFrame: WKFrameInfo { get }
```

```objc
@property (nonatomic, copy, readonly) WKFrameInfo * sourceFrame;
```

## See Also

### Inspecting navigation information
- [var request: URLRequest](./request.md)
  The URL request object associated with the navigation action.
- [var targetFrame: WKFrameInfo?](./targetframe.md)
  The frame in which to display the new content.
- [var shouldPerformDownload: Bool](./shouldperformdownload.md)
  A Boolean value that indicates whether the web content provided an attribute that indicates a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/sourceframe)*