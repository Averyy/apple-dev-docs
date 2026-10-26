# sourceRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) CGRect sourceRect;
```

#### Discussion

To set [`sourceRect`](./sourcerect-iltv.md), create a tooltip configuration object using the [`init(toolTip:in:)`](./init%28tooltip,in%29.md) method.

## See Also

### Accessing the configuration settings
- [var toolTip: String](./tooltip.md)
  The text to display in the tooltip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration/sourcerect-iltv)*