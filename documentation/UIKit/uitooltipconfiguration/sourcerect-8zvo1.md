# sourceRect

**Framework**: UIKit  
**Kind**: property

The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var sourceRect: CGRect? { get }
```

#### Discussion

To set [`sourceRect`](uiviewcontrollerpreviewing/sourcerect.md), create a tooltip configuration object using the [`init(toolTip:in:)`](uitooltipconfiguration/init(tooltip:in:).md) method.

## See Also

- [var toolTip: String](uitooltipconfiguration/tooltip.md)
  The text to display in the tooltip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration/sourcerect-8zvo1)*