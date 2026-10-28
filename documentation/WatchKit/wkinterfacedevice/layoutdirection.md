# layoutDirection

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The layout direction of the user interface.

**Availability**:
- watchOS 2.1+

## Declaration

```swift
var layoutDirection: WKInterfaceLayoutDirection { get }
```

```objc
@property (nonatomic, readonly) WKInterfaceLayoutDirection layoutDirection;
```

## Discussion

For a list of possible values, see [`WKInterfaceLayoutDirection`](../wkinterfacelayoutdirection.md).

## See Also

### Accessing the Layout Direction
- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](./interfacelayoutdirection%28for%29.md)
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceSemanticContentAttribute](../wkinterfacesemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [enum WKInterfaceLayoutDirection](../wkinterfacelayoutdirection.md)
  Specifies the directional flow of the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/layoutdirection)*