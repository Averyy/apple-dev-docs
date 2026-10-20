# attributedText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string of attributed text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var attributedText: NSAttributedString? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedText;
```

#### Discussion

You cannot change the value of this property once drawing begins for a print job. The delegate method [`printInteractionControllerWillStartJob(_:)`](../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob%28_%29.md) is called immediately before the formatting is set for the job.

Assigning a value to this property also replaces the value in the [`text`](./text.md) property with the same string data, albeit without any formatting information.

## See Also

### Related Documentation
- [init(attributedText: NSAttributedString)](./init%28attributedtext%29.md)
  Returns a simple-text print formatter initialized with attributed text.
### Getting and setting the text
- [var text: String?](./text.md)
  A string of plain text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/attributedtext)*