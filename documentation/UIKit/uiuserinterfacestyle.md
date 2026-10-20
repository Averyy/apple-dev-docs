# UIUserInterfaceStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the interface style for the app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UIUserInterfaceStyle
```

```c
enum UIUserInterfaceStyle : NSInteger;
```

## Topics

### Interface styles
- [UIUserInterfaceStyle.unspecified](./uiuserinterfacestyle/unspecified.md)
  An unspecified interface style.
- [UIUserInterfaceStyle.light](./uiuserinterfacestyle/light.md)
  The light interface style.
- [UIUserInterfaceStyle.dark](./uiuserinterfacestyle/dark.md)
  The dark interface style.
### Initializers
- [init(ColorScheme?)](./uiuserinterfacestyle/init%28_%29.md)
  Creates a user interface style from the specified SwiftUI color scheme.
- [init?(rawValue: Int)](./uiuserinterfacestyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adjusting the interface style
- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](./uiviewcontroller/overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](./uiviewcontroller/preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [var childViewControllerForUserInterfaceStyle: UIViewController?](./uiviewcontroller/childviewcontrollerforuserinterfacestyle.md)
  The child view controller that supports the preferred user interface style.
- [func setNeedsUserInterfaceAppearanceUpdate()](./uiviewcontroller/setneedsuserinterfaceappearanceupdate%28%29.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle)*