# eventAttribution

**Framework**: UIKit  
**Kind**: property

An event attribution associated with the URL to open.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var eventAttribution: UIEventAttribution? { get }
```

#### Discussion

For more information about event attribution data, see [`UIEventAttribution`](uieventattribution.md).

## See Also

- [var sourceApplication: String?](uiscene/openurloptions/sourceapplication.md)
  The bundle ID of the app that originated the request.
- [var annotation: Any?](uiscene/openurloptions/annotation.md)
  A property-list object that contains the annotation data provided by a document interaction controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions/eventattribution)*