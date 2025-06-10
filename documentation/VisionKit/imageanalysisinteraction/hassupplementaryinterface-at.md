# hasSupplementaryInterface(at:)

**Framework**: VisionKit  
**Kind**: method

Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func hasSupplementaryInterface(at point: CGPoint) -> Bool
```

#### Return Value

`true` if supplementary interface objects exist at `point`; otherwise, `false`.

#### Discussion

Supplementary interface objects include the Live Text button and Quick Actions, depending on the item type.

## Parameters

- `point`: A point in the image, in view coordinates.

## See Also

- [var liveTextButtonVisible: Bool](imageanalysisinteraction/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](imageanalysisinteraction/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](imageanalysisinteraction/hasinteractiveitem(at:).md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisinteraction/selectableitemshighlighted.md)
  A Boolean value that indicates whether the interaction highlights actionable text or data the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/hassupplementaryinterface(at:))*