# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Whether the content defined by this scene accessory should be displayed or not.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isEnabled) BOOL enabled;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

## Discussion

This value does not reflect the availability of the scene accessory, which is determined by the system.

## See Also

### Observing availability and controlling display
- [var isAvailable: Bool](./isavailable.md)
  Whether the associated scene accessory is available for display by the system or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isenabled)*