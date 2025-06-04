# resignFocus()

**Framework**: WatchKit  
**Kind**: method

Ends the delivery of crown events to the current crown sequencer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func resignFocus()
```

#### Discussion

Call this method when you no longer want to receive crown events in the current crown sequencer. If the user taps a picker object or a scrollable scene in your interface, the system automatically removes the focus from any active crown sequencer.

## See Also

- [func focus()](wkcrownsequencer/focus.md)
  Begins the delivery of crown events to the current crown sequencer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/resignfocus())*