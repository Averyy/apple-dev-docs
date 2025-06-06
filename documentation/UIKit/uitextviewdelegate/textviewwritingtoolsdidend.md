# textViewWritingToolsDidEnd(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the current writing tools session ended.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func textViewWritingToolsDidEnd(_ textView: UITextView)
```

## Mentions

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md)

#### Discussion

Use this method to undo any actions you took at the start of a writing tools session to modify your app’s behavior.  The text view calls this method after the writing session finishes. At this point, the text view contains the final text the person chose.

## Parameters

- `textView`: The text view that ended a writing tools session.

## See Also

- [func textViewWritingToolsWillBegin(UITextView)](uitextviewdelegate/textviewwritingtoolswillbegin(_:).md)
  Tells the delegate that an interaction with the writing tools interface is about to begin.
- [func textView(UITextView, writingToolsIgnoredRangesInEnclosingRange: NSRange) -> [NSValue]](uitextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:).md)
  Asks the delegate to specify any ranges of text you want the writing tools to ignore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewwritingtoolsdidend(_:))*