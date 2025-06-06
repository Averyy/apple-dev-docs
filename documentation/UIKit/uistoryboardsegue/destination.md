# destination

**Framework**: UIKit  
**Kind**: property

The destination view controller for the segue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var destination: UIViewController { get }
```

#### Discussion

This property contains the view controller whose contents should be displayed at the end of the segue.

## See Also

- [var source: UIViewController](uistoryboardsegue/source.md)
  The source view controller for the segue.
- [var identifier: String?](uistoryboardsegue/identifier.md)
  The identifier for the segue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/destination)*