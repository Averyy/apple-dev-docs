# toolTip

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the tooltip.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var toolTip: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * toolTip;
```

## Discussion

To set the tooltip text, create a tooltip configuration object using either the [`init(toolTip:)`](./init%28tooltip%29.md) or [`init(toolTip:in:)`](./init%28tooltip,in%29.md) methods.

## See Also

### Accessing the configuration settings
- [var sourceRect: CGRect?](./sourcerect-8zvo1.md)
  The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.
- [sourceRect](./sourcerect-iltv.md)
  The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration/tooltip)*