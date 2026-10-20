# UIScreenMode

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A possible set of attributes that can apply to a screen object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
class UIScreenMode
```

```objc
@interface UIScreenMode : NSObject
```

## Mentions

- [Presenting content on a connected display](./presenting-content-on-a-connected-display.md)

#### Overview

A screen mode object encapsulates information about the size of the screen’s underlying display buffer and the aspect ratio it uses for individual pixels. Most developers should never need to use the information provided by this class and should simply use the bounds provided by the [`UIScreen`](./uiscreen.md) object for their drawing space. The bounds of screen and window objects automatically take the pixel aspect ratio and underlying drawing hardware into consideration. However, developers that work with pixel-level information more directly may use the information in the current screen mode object to tailor their code for the target screen.

You don’t create instances of this class directly. Instead, you get the screen modes supported by a given screen from the corresponding [`UIScreen`](./uiscreen.md) object.

## Topics

### Accessing the screen mode attributes
- [var size: CGSize](./uiscreenmode/size.md)
  The screen size, measured in pixels.
- [var pixelAspectRatio: CGFloat](./uiscreenmode/pixelaspectratio.md)
  The aspect ratio of a single pixel.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Screens
- [Presenting content on a connected display](./presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.
- [class UIScreen](./uiscreen.md)
  An object that defines the properties associated with a hardware-based display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreenmode)*