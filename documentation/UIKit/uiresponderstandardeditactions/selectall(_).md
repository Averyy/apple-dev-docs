# selectAll(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Selects all of the content in the current responder.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func selectAll(_ sender: Any?)
```

```objc
- (void) selectAll:(id) sender;
```

## Discussion

UIKit calls this method when the user selects the Select All command from an editing menu. The command selects all content in the responder. For example, a text view selects all of its text and displays an appropriate selection interface.

## Parameters

- `sender`: The object calling this method.

## See Also

### Handling selection commands
- [func select(Any?)](./select%28_%29.md)
  Selects the content in your responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/selectall(_:))*