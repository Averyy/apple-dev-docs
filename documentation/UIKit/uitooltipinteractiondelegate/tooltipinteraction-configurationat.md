# toolTipInteraction(_:configurationAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a tooltip configuration that describes the tooltip settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
optional func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration?
```

#### Return Value

A tooltip configuration that specifies the text that appears in the tooltip and the region of the view or control where the pointer must hover over to trigger the display of the tooltip. Return `nil` to prevent the display of the tooltip.

#### Discussion

Implement this method to provide a tooltip configuration based on logic specific to your app. For example, the following code listing returns a tooltip configuration when the pointer hovers over the top or bottom regions of the view. If the pointer hovers over the middle region, the method returns `nil` to prevent the display of a tooltip.

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

- `interaction`: The tooltip interaction requesting a tooltip configuration.
- `point`: The current position of the pointer in the coordinate space of the view or control associated to the tooltip interaction.

## See Also

- [class UIToolTipConfiguration](uitooltipconfiguration.md)
  An object that a tooltip interaction delegate uses to describe the tooltip settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:))*