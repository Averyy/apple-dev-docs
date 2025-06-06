# attributedText

**Framework**: UIKit  
**Kind**: property

A string of attributed text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var attributedText: NSAttributedString? { get set }
```

#### Discussion

You cannot change the value of this property once drawing begins for a print job. The delegate method [`printInteractionControllerWillStartJob(_:)`](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:).md) is called immediately before the formatting is set for the job.

Assigning a value to this property also replaces the value in the [`text`](uisimpletextprintformatter/text.md) property with the same string data, albeit without any formatting information.

## See Also

- [init(attributedText: NSAttributedString)](uisimpletextprintformatter/init(attributedtext:).md)
  Returns a simple-text print formatter initialized with attributed text.
- [var text: String?](uisimpletextprintformatter/text.md)
  A string of plain text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/attributedtext)*