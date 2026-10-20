# buttonNumber

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The number of the mouse button that caused the navigation request.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.10+
- visionOS 2.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var buttonNumber: UIEvent.ButtonMask { get }
```

*macOS*

```swift
var buttonNumber: Int { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, readonly) UIEventButtonMask buttonNumber;
```

*macOS*

```objc
@property (nonatomic, readonly) NSInteger buttonNumber;
```

## See Also

### Inspecting user actions
- [var modifierFlags: UIKeyModifierFlags](./modifierflags.md)
  The modifier keys that were pressed at the time of the navigation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/buttonnumber)*