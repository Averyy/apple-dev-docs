# isAvailable

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Whether the associated scene accessory is available for display by the system or not.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var isAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAvailable) BOOL available;
```

## Mentions

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md)

## Discussion

This value is observable during the `updateProperties` and `layoutSubviews` lifecycle events.

## See Also

### Observing availability and controlling display
- [var isEnabled: Bool](./isenabled.md)
  Whether the content defined by this scene accessory should be displayed or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isavailable)*