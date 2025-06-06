# supplementaryInterfaceFont

**Framework**: Visionkit  
**Kind**: property

The font to use for the supplementary interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var supplementaryInterfaceFont: UIFont? { get set }
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

The interaction also uses the font weight for image symbols, but ignores the point size to keep button sizes consistent.

## See Also

- [var allowLongPressForDataDetectorsInTextMode: Bool](imageanalysisinteraction/allowlongpressfordatadetectorsintextmode.md)
  A Boolean value that indicates whether people can press and hold text to activate data detectors.
- [func setSupplementaryInterfaceHidden(Bool, animated: Bool)](imageanalysisinteraction/setsupplementaryinterfacehidden(_:animated:).md)
  Hides or shows supplementary interface objects, such as the Live Action button and Quick Actions, depending on the item type.
- [var supplementaryInterfaceContentInsets: UIEdgeInsets](imageanalysisinteraction/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/supplementaryinterfacefont)*