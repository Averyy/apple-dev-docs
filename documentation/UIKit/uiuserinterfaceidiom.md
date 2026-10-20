# UIUserInterfaceIdiom

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum UIUserInterfaceIdiom
```

```c
enum UIUserInterfaceIdiom : NSInteger;
```

## Topics

### Idioms
- [UIUserInterfaceIdiom.unspecified](./uiuserinterfaceidiom/unspecified.md)
  An unspecified idiom.
- [UIUserInterfaceIdiom.phone](./uiuserinterfaceidiom/phone.md)
  An interface designed for iPhone and iPod touch.
- [UIUserInterfaceIdiom.pad](./uiuserinterfaceidiom/pad.md)
  An interface designed for iPad.
- [UIUserInterfaceIdiom.tv](./uiuserinterfaceidiom/tv.md)
  An interface designed for tvOS and Apple TV.
- [UIUserInterfaceIdiom.carPlay](./uiuserinterfaceidiom/carplay.md)
  An interface designed for an in-car experience.
- [UIUserInterfaceIdiom.mac](./uiuserinterfaceidiom/mac.md)
  An interface designed for the Mac.
- [UIUserInterfaceIdiom.vision](./uiuserinterfaceidiom/vision.md)
  An interface designed for visionOS and Apple Vision Pro.
### Initializers
- [init?(rawValue: Int)](./uiuserinterfaceidiom/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the current idiom
- [func UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiom](./ui_user_interface_idiom%28%29.md)
  Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom)*