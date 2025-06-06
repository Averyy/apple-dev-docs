# sender

**Framework**: UIKit  
**Kind**: property

The object that performed the unwind action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sender: Any? { get }
```

#### Discussion

Use this property to determine which object in your interface triggered the unwind segue.

## See Also

- [var source: UIViewController](uistoryboardunwindseguesource/source.md)
  The view controller being dismissed by the unwind segue.
- [var unwindAction: Selector](uistoryboardunwindseguesource/unwindaction.md)
  The action method associated with the unwind segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/sender)*