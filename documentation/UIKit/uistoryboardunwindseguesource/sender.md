# sender

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that performed the unwind action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sender: Any? { get }
```

```objc
@property (readonly, nullable) id sender;
```

#### Discussion

Use this property to determine which object in your interface triggered the unwind segue.

## See Also

### Getting the unwind segue attributes
- [var source: UIViewController](./source.md)
  The view controller being dismissed by the unwind segue.
- [var unwindAction: Selector](./unwindaction.md)
  The action method associated with the unwind segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/sender)*