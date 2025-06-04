# interfaceLayoutDirection(for:)

**Framework**: WatchKit  
**Kind**: method

Returns the user interface direction for the given semantic content attribute.

**Availability**:
- watchOS 2.1+

## Declaration

```swift
class func interfaceLayoutDirection(for semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection
```

#### Return Value

The user interface layout direction (left-to-right or right-to-left). For a list of possible values, see [`WKInterfaceLayoutDirection`](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection).

## Parameters

- `semanticContentAttribute`: The semantic content attribute. For a list of possible values, see  .

## See Also

- [var layoutDirection: WKInterfaceLayoutDirection](layoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/layoutdirection))
  The layout direction of the user interface.
- [enum WKInterfaceSemanticContentAttribute](wkinterfacesemanticcontentattribute.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute))
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [enum WKInterfaceLayoutDirection](wkinterfacelayoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection))
  Specifies the directional flow of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/interfacelayoutdirection(for:))*