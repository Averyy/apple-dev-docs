# isSecureTextEntry

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a text object disables copying, and in some cases, prevents recording/broadcasting and also hides the text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional var isSecureTextEntry: Bool { get set }
```

```objc
@property (nonatomic, getter=isSecureTextEntry) BOOL secureTextEntry;
```

## Discussion

This property is set to [`false`](../../Swift/false.md) by default. Setting this property to [`true`](../../Swift/true.md) in any view that conforms to [`UITextInputTraits`](../uitextinputtraits.md) disables the user’s ability to copy the text in the view and, in some cases, also disables the user’s ability to record and broadcast the text in the view.

Setting this property to [`true`](../../Swift/true.md) in a [`UITextField`](../uitextfield.md) object additionally enables a password-style experience, in which the text being entered is obscured.

## See Also

### Managing the keyboard behavior
- [var enablesReturnKeyAutomatically: Bool](./enablesreturnkeyautomatically.md)
  A Boolean value that indicates whether the system automatically enables the Return key when the user enters text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/issecuretextentry)*