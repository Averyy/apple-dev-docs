# UIScreen.ReferenceDisplayModeStatus.limited

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A status that indicates the screen’s in a limited reference display mode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+

## Declaration

```swift
case limited
```

```c
UIScreenReferenceDisplayModeStatusLimited
```

## Discussion

The screen may be unable to provide an accurate reference display mode due to thermal or power constraints.

## See Also

### Statuses
- [UIScreen.ReferenceDisplayModeStatus.notSupported](./notsupported.md)
  A status that indicates the screen doesn’t provide a reference display mode.
- [UIScreen.ReferenceDisplayModeStatus.notEnabled](./notenabled.md)
  A status that indicates the screen provides a reference display mode but it’s in a disabled state.
- [UIScreen.ReferenceDisplayModeStatus.enabled](./enabled.md)
  A status that indicates the screen’s in an accurate reference display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum/limited)*