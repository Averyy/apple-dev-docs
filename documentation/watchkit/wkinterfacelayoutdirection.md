# WKInterfaceLayoutDirection

**Framework**: WatchKit  
**Kind**: enum

Specifies the directional flow of the user interface.

**Availability**:
- watchOS 2.1+

## Declaration

```swift
enum WKInterfaceLayoutDirection
```

## Topics

### Constants
- [WKInterfaceLayoutDirection.leftToRight](wkinterfacelayoutdirection/lefttoright.md)
  The layout direction is left-to-right.
- [WKInterfaceLayoutDirection.rightToLeft](wkinterfacelayoutdirection/righttoleft.md)
  The layout direction right-to-left. This value is appropriate when your app is running with localizations such as Arabic or Hebrew that should have the user interface layout origin on the right edge of the coordinate system.
### Initializers
- [init?(rawValue: Int)](wkinterfacelayoutdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [var layoutDirection: WKInterfaceLayoutDirection](wkinterfacedevice/layoutdirection.md)
  The layout direction of the user interface.
- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](wkinterfacedevice/interfacelayoutdirection(for:).md)
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceSemanticContentAttribute](wkinterfacesemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection)*