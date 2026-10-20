# text

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string of plain text.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var text: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * text;
```

#### Discussion

You cannot change the value of this property once drawing begins for a print job. The delegate method [`printInteractionControllerWillStartJob(_:)`](../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob%28_%29.md) is called immediately before the formatting is set for the job.

Assigning a value to this property replaces the value in the [`attributedText`](./attributedtext.md) property with the same string data, albeit without any inherent style attributes. Instead, the print formatter styles the new string using the text attribute properties of this class.

## See Also

### Related Documentation
- [init(text: String)](./init%28text%29.md)
  Returns a simple-text print formatter initialized with plain text.
### Getting and setting the text
- [var attributedText: NSAttributedString?](./attributedtext.md)
  A string of attributed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/text)*