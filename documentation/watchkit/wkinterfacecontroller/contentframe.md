# contentFrame

**Framework**: Watchkit  
**Kind**: property

The frame rectangle used to display your app’s content.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
var contentFrame: CGRect { get }
```

#### Discussion

The rectangle in this property is specified in points. This rectangle may be different than the screen bounds.

## See Also

- [var contentSafeAreaInsets: UIEdgeInsets](wkinterfacecontroller/contentsafeareainsets.md)
  Insets that define the area where it’s safe to display content on the screen.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](wkinterfacecontroller/systemminimumlayoutmargins.md)
  Leading and trailing insets that represent the minimum layout margins for text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentframe)*