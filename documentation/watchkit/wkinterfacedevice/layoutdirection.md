# layoutDirection

**Framework**: WatchKit  
**Kind**: property

The layout direction of the user interface.

**Availability**:
- watchOS 2.1+

## Declaration

```swift
var layoutDirection: WKInterfaceLayoutDirection { get }
```

#### Discussion

For a list of possible values, see [`WKInterfaceLayoutDirection`](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection).

## See Also

- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](interfacelayoutdirection(for:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/interfacelayoutdirection(for:)))
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceSemanticContentAttribute](wkinterfacesemanticcontentattribute.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute))
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [enum WKInterfaceLayoutDirection](wkinterfacelayoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection))
  Specifies the directional flow of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/layoutdirection)*