# modifierFlags

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The modifier keys that were pressed at the time of the navigation request.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.10+
- visionOS 2.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var modifierFlags: UIKeyModifierFlags { get }
```

*macOS*

```swift
var modifierFlags: NSEvent.ModifierFlags { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, readonly) UIKeyModifierFlags modifierFlags;
```

*macOS*

```objc
@property (nonatomic, readonly) NSEventModifierFlags modifierFlags;
```

## See Also

### Inspecting user actions
- [var buttonNumber: UIEvent.ButtonMask](./buttonnumber.md)
  The number of the mouse button that caused the navigation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/modifierflags)*