# WKInterfaceSemanticContentAttribute

**Framework**: WatchKit  
**Kind**: enum

A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.

**Availability**:
- watchOS 2.1+

## Declaration

```swift
enum WKInterfaceSemanticContentAttribute
```

## Topics

### Constants
- [WKInterfaceSemanticContentAttribute.unspecified](unspecified.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/unspecified))
  The default value for views. The view is flipped when switching between left-to-right and right-to-left layouts.
- [WKInterfaceSemanticContentAttribute.playback](playback.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/playback))
  A view representing the playback controls, such as Play, Rewind, or Fast Forward buttons or playhead scrubbers. These views are not flipped when switching between left-to-right and right-to-left layouts.
- [WKInterfaceSemanticContentAttribute.spatial](spatial.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/spatial))
  A view representing a directional control, for example a segment control for text alignment, or a D-pad control for a game. These views are not flipped when switching between left-to-right and right-to-left layouts.
- [WKInterfaceSemanticContentAttribute.forceLeftToRight](forcelefttoright.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/forcelefttoright))
  A view that is always displayed using a left-to-right layout.
- [WKInterfaceSemanticContentAttribute.forceRightToLeft](forcerighttoleft.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/forcerighttoleft))
  A view that is always displayed using a left-to-right layout.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [var layoutDirection: WKInterfaceLayoutDirection](layoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/layoutdirection))
  The layout direction of the user interface.
- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](interfacelayoutdirection(for:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/interfacelayoutdirection(for:)))
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceLayoutDirection](wkinterfacelayoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection))
  Specifies the directional flow of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute)*