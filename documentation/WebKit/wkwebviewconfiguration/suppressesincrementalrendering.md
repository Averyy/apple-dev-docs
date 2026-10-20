# suppressesIncrementalRendering

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the web view suppresses content rendering until the content is fully loaded into memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var suppressesIncrementalRendering: Bool { get set }
```

```objc
@property (nonatomic) BOOL suppressesIncrementalRendering;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the rendering behavior
- [var ignoresViewportScaleLimits: Bool](./ignoresviewportscalelimits.md)
  A Boolean value that determines whether a web view allows scaling of the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/suppressesincrementalrendering)*