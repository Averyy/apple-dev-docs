# captureTraceURL

**Framework**: Core Image  
**Kind**: property

Tell the next using this destination to capture a Metal trace.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var captureTraceURL: URL? { get set }
```

#### Discussion

If this property is set to a file-based URL, then the next render using this destination will capture a Metal trace, deleting any existing file if present. This property is nil by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/capturetraceurl)*