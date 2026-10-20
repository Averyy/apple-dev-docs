# source

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller being dismissed by the unwind segue.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var source: UIViewController { get }
```

```objc
@property (readonly) UIViewController * sourceViewController;
```

## See Also

### Getting the unwind segue attributes
- [var unwindAction: Selector](./unwindaction.md)
  The action method associated with the unwind segue.
- [var sender: Any?](./sender.md)
  The object that performed the unwind action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/source)*