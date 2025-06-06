# textView(_:writingToolsIgnoredRangesInEnclosingRange:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to specify any ranges of text you want the writing tools to ignore.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, writingToolsIgnoredRangesInEnclosingRange enclosingRange: NSRange) -> [NSValue]
```

## Mentions

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md)

#### Return Value

One or more ranges of text you want the writing tools to ignore. Return an empty array to allow the modification of all the proposed text.

#### Discussion

Use this method to prevent the writing tools session from modifying portions of the current text. For example, you might prevent the writing tools session from modifying code or read-only text. The text view provides you with the overall range of text to consider, and you return one or more subranges you want the writing tools to ignore.

## Parameters

- `textView`: The text view with the active writing tools session.
- `enclosingRange`: The text range that the writing tools are examining. When computing the text ranges to ignore, skip any text that falls outside of this boundary.

## See Also

- [func textViewWritingToolsWillBegin(UITextView)](uitextviewdelegate/textviewwritingtoolswillbegin(_:).md)
  Tells the delegate that an interaction with the writing tools interface is about to begin.
- [func textViewWritingToolsDidEnd(UITextView)](uitextviewdelegate/textviewwritingtoolsdidend(_:).md)
  Tells the delegate that the current writing tools session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:))*