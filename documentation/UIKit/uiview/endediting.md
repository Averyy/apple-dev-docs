# endEditing(_:)

**Framework**: UIKit  
**Kind**: method

Causes the view (or one of its embedded text fields) to resign the first responder status.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func endEditing(_ force: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view resigned the first responder status or [`false`](https://developer.apple.com/documentation/swift/false) if it did not.

#### Discussion

This method looks at the current view and its subview hierarchy for the text field that is currently the first responder. If it finds one, it asks that text field to resign as first responder. If the `force` parameter is set to [`true`](https://developer.apple.com/documentation/swift/true), the text field is never even asked; it is forced to resign.

## Parameters

- `force`: Specify   to force the first responder to resign, regardless of whether it wants to do so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/endediting(_:))*