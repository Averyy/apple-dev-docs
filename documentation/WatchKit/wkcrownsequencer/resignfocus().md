# resignFocus()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Ends the delivery of crown events to the current crown sequencer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func resignFocus()
```

```objc
- (void) resignFocus;
```

#### Discussion

Call this method when you no longer want to receive crown events in the current crown sequencer. If the user taps a picker object or a scrollable scene in your interface, the system automatically removes the focus from any active crown sequencer.

## See Also

### Managing the Focus
- [func focus()](./focus%28%29.md)
  Begins the delivery of crown events to the current crown sequencer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/resignfocus())*