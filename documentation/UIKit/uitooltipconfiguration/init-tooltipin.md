# init(toolTip:in:)

**Framework**: UIKit  
**Kind**: init

Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(toolTip: String, in sourceRect: CGRect)
```

#### Discussion

Create a configuration using this method to show the tooltip when the pointer hovers over the specified region of the view or control. For example, the following code listing returns a configuration that instructs the view shows the tooltip only when the pointer hovers over either top or bottom regions of a view. The tooltip does’t appear when the pointer hovers over the middle region of the view.

```swift
func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
    var topRect = self.bounds
    var bottomRect = self.bounds
    
    let partHeight = self.bounds.size.height / 3
    topRect.size.height = partHeight
    bottomRect.size.height = partHeight
    bottomRect.origin.y = partHeight * 2
    
    // Display tooltip if the pointer within the top or bottom rects.
    if topRect.contains(point) {
        return UIToolTipConfiguration(toolTip: "Top area of the view.", in: topRect)
    } else if bottomRect.contains(point) {
        return UIToolTipConfiguration(toolTip: "Bottom area of the view.", in: bottomRect)
    }
    
    // Pointer is in the middle of the view. Don't display a tooltip.
    return nil
}
```

## Parameters

- `toolTip`: The text that appears in the tooltip.
- `sourceRect`: The region of the view or control where the pointer must hover to trigger the display of the tooltip.

## See Also

- [convenience init(toolTip: String)](uitooltipconfiguration/init(tooltip:).md)
  Creates a tooltip configuration and sets the tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration/init(tooltip:in:))*