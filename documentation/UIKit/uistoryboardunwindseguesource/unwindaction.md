# unwindAction

**Framework**: UIKit  
**Kind**: property

The action method associated with the unwind segue.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var unwindAction: Selector { get }
```

#### Discussion

Each unwind segue has an associated action method. The view controller that’s the destination of the unwind segue must implement this action method.

## See Also

- [var source: UIViewController](uistoryboardunwindseguesource/source.md)
  The view controller being dismissed by the unwind segue.
- [var sender: Any?](uistoryboardunwindseguesource/sender.md)
  The object that performed the unwind action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/unwindaction)*