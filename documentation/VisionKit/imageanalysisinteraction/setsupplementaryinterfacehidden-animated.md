# setSupplementaryInterfaceHidden(_:animated:)

**Framework**: Visionkit  
**Kind**: method

Hides or shows supplementary interface objects, such as the Live Action button and Quick Actions, depending on the item type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func setSupplementaryInterfaceHidden(_ hidden: Bool, animated: Bool)
```

## Parameters

- `hidden`:   to   hide the supplementary interface; otherwise,   .
- `animated`:   to   animate the interface transition; otherwise,   .

## See Also

- [var allowLongPressForDataDetectorsInTextMode: Bool](imageanalysisinteraction/allowlongpressfordatadetectorsintextmode.md)
  A Boolean value that indicates whether people can press and hold text to activate data detectors.
- [var supplementaryInterfaceContentInsets: UIEdgeInsets](imageanalysisinteraction/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [var supplementaryInterfaceFont: UIFont?](imageanalysisinteraction/supplementaryinterfacefont.md)
  The font to use for the supplementary interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/setsupplementaryinterfacehidden(_:animated:))*