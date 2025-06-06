# WKInterfaceSemanticContentAttribute

**Framework**: Watchkit  
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
- [WKInterfaceSemanticContentAttribute.unspecified](wkinterfacesemanticcontentattribute/unspecified.md)
  The default value for views. The view is flipped when switching between left-to-right and right-to-left layouts.
- [WKInterfaceSemanticContentAttribute.playback](wkinterfacesemanticcontentattribute/playback.md)
  A view representing the playback controls, such as Play, Rewind, or Fast Forward buttons or playhead scrubbers. These views are not flipped when switching between left-to-right and right-to-left layouts.
- [WKInterfaceSemanticContentAttribute.spatial](wkinterfacesemanticcontentattribute/spatial.md)
  A view representing a directional control, for example a segment control for text alignment, or a D-pad control for a game. These views are not flipped when switching between left-to-right and right-to-left layouts.
- [WKInterfaceSemanticContentAttribute.forceLeftToRight](wkinterfacesemanticcontentattribute/forcelefttoright.md)
  A view that is always displayed using a left-to-right layout.
- [WKInterfaceSemanticContentAttribute.forceRightToLeft](wkinterfacesemanticcontentattribute/forcerighttoleft.md)
  A view that is always displayed using a left-to-right layout.
### Initializers
- [init?(rawValue: Int)](wkinterfacesemanticcontentattribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var layoutDirection: WKInterfaceLayoutDirection](wkinterfacedevice/layoutdirection.md)
  The layout direction of the user interface.
- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](wkinterfacedevice/interfacelayoutdirection(for:).md)
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceLayoutDirection](wkinterfacelayoutdirection.md)
  Specifies the directional flow of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute)*