# currentMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current screen mode associated with the screen.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
var currentMode: UIScreenMode? { get set }
```

*tvOS*

```swift
var currentMode: UIScreenMode? { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, strong, nullable) UIScreenMode * currentMode;
```

*tvOS*

```objc
@property (nonatomic, strong, readonly, nullable) UIScreenMode * currentMode;
```

## Discussion

The default value of this property is the mode containing the highest resolution supported by the screen.

On iOS, you can change the value of this property to support different resolutions as needed. For example, you might want to lower the default resolution to one that your application supports more readily. The value must be one of the values described in the [`availableModes`](./availablemodes.md) property.

On tvOS, the screen mode is read-only.

## See Also

### Managing screen modes
- [var preferredMode: UIScreenMode?](./preferredmode.md)
  The preferred display mode for the screen.
- [var availableModes: [UIScreenMode]](./availablemodes.md)
  The display modes that can be associated with the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/currentmode)*