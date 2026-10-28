# hasSupplementaryInterface(at:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether supplementary interface objects exist at the specified point.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func hasSupplementaryInterface(at point: CGPoint) -> Bool
```

## Return Value

`true` if supplementary interface objects exist at `point`; otherwise, `false`.

## Discussion

Supplementary interface objects include the Live Text button and Quick Actions, depending on the item type.

## Parameters

- `point`: A point in the image, in view coordinates.

## See Also

### Querying the interface state
- [var liveTextButtonVisible: Bool](./livetextbuttonvisible.md)
  A Boolean value that indicates whether the Live Text button appears.
- [var isSupplementaryInterfaceHidden: Bool](./issupplementaryinterfacehidden.md)
  A Boolean value that indicates whether the view hides supplementary interface objects.
- [func hasInteractiveItem(at: CGPoint) -> Bool](./hasinteractiveitem%28at%29.md)
  Returns a Boolean value that indicates whether active text, data detectors, or supplementary interface objects exist at the specified point.
- [var selectableItemsHighlighted: Bool](./selectableitemshighlighted.md)
  A Boolean value that indicates whether the overlay view highlights actionable text or data that the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/hassupplementaryinterface(at:))*