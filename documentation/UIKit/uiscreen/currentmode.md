# currentMode

**Framework**: UIKit  
**Kind**: property

The current screen mode associated with the screen.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var currentMode: UIScreenMode? { get set }
```

#### Discussion

The default value of this property is the mode containing the highest resolution supported by the screen.

On iOS, you can change the value of this property to support different resolutions as needed. For example, you might want to lower the default resolution to one that your application supports more readily. The value must be one of the values described in the [`availableModes`](uiscreen/availablemodes.md) property.

On tvOS, the screen mode is read-only.

## See Also

- [var preferredMode: UIScreenMode?](uiscreen/preferredmode.md)
  The preferred display mode for the screen.
- [var availableModes: [UIScreenMode]](uiscreen/availablemodes.md)
  The display modes that can be associated with the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/currentmode)*