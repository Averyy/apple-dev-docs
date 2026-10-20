# init(_:)

**Framework**: VisionKit  
**Kind**: init  
**Role**: Initializer

Creates an overlay view with the specified delegate object.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
convenience init(_ delegate: any ImageAnalysisOverlayViewDelegate)
```

## Parameters

- `delegate`: The object that provides details about the interface.

## See Also

### Creating overlay views
- [init(frame: NSRect)](./init%28frame%29.md)
  Creates an overlay view with the specified frame rectangle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an overlay view from data in a coder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/init(_:))*