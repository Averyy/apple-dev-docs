# init(toolTip:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a tooltip configuration and sets the tooltip text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toolTip: String)
```

```objc
+ (instancetype) configurationWithToolTip:(NSString *) toolTip;
```

## Discussion

Create a configuration using this method to show the tooltip when the pointer hovers over any area of the view or control. For example, the following code listing creates a configuration that instructs the view to show the tooltip when the pointer hovers over any area of the view:

```swift
let configuration = UIToolTipConfiguration(toolTip: "The color is \(colorName).")
```

## Parameters

- `toolTip`: The text that appears in the tooltip.

## See Also

### Creating a tooltip configuration
- [convenience init(toolTip: String, in: CGRect)](./init%28tooltip,in%29.md)
  Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration/init(tooltip:))*