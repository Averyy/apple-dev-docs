# contentFrame

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The frame rectangle used to display your app’s content.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var contentFrame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect contentFrame;
```

#### Discussion

The rectangle in this property is specified in points. This rectangle may be different than the screen bounds.

## See Also

### Respecting safe areas and layout margins
- [var contentSafeAreaInsets: UIEdgeInsets](./contentsafeareainsets.md)
  Insets that define the area where it’s safe to display content on the screen.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](./systemminimumlayoutmargins.md)
  Leading and trailing insets that represent the minimum layout margins for text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentframe)*