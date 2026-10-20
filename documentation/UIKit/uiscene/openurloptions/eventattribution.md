# eventAttribution

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An event attribution associated with the URL to open.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
var eventAttribution: UIEventAttribution? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIEventAttribution * eventAttribution;
```

#### Discussion

For more information about event attribution data, see [`UIEventAttribution`](../../uieventattribution.md).

## See Also

### Specifying the URL details
- [var sourceApplication: String?](./sourceapplication.md)
  The bundle ID of the app that originated the request.
- [var annotation: Any?](./annotation.md)
  A property-list object that contains the annotation data provided by a document interaction controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions/eventattribution)*