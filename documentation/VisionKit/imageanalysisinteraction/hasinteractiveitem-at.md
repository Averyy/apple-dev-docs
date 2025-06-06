# hasInteractiveItem(at:)

**Framework**: Visionkit  
**Kind**: method

Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func hasInteractiveItem(at point: CGPoint) -> Bool
```

#### Return Value

`true` if active text, data detectors, or supplementary interface objects exist at `point`; otherwise, `false`.

## Parameters

- `point`: A point in the image, in view coordinates.

## See Also

- [var liveTextButtonVisible: Bool](imageanalysisinteraction/livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](imageanalysisinteraction/issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasSupplementaryInterface(at: CGPoint) -> Bool](imageanalysisinteraction/hassupplementaryinterface(at:).md)
  Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](imageanalysisinteraction/selectableitemshighlighted.md)
  A Boolean value that indicates whether the interaction highlights actionable text or data the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/hasinteractiveitem(at:))*