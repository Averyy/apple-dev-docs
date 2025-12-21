# captureTraceURL

**Framework**: Core Image  
**Kind**: property

Tell the next render using this destination to capture a Metal trace.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var captureTraceURL: URL? { get set }
```

#### Discussion

If this property is set to a file-based URL, then the next render using this destination will capture a Metal trace, deleting any existing file if present. This property is nil by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/capturetraceurl)*