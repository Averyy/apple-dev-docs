# isHapticFeedbackEnabled

**Framework**: WatchKit  
**Kind**: property

A Boolean value that determines whether the crown sequencer’s haptic feedback is enabled.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var isHapticFeedbackEnabled: Bool { get set }
```

#### Discussion

By default, this property is set to [`true`](https://developer.apple.com/documentation/Swift/true). In Apple Watch Series 4 and later, the watch provides linear haptic feedback as the user rotates the digital crown. Set this property to [`false`](https://developer.apple.com/documentation/Swift/false) to disable the haptic feedback while the crown sequencer has the focus. For example, you can use this property to disable haptic feedback if the feedback does not match the screen’s animation.

## See Also

- [var isTableScrollingHapticFeedbackEnabled: Bool](wkinterfacecontroller/istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/ishapticfeedbackenabled)*