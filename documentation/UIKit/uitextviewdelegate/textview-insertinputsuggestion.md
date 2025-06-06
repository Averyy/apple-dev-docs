# textView(_:insertInputSuggestion:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the keyboard delivers an input suggestion.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, insertInputSuggestion inputSuggestion: UIInputSuggestion)
```

## Mentions

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)

## Parameters

- `textView`: The text view that is currently the first responder.
- `inputSuggestion`: The input suggestion that the user or system selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:insertinputsuggestion:))*