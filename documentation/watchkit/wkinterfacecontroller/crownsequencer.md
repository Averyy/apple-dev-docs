# crownSequencer

**Framework**: WatchKit  
**Kind**: property

The object to use when directly tracking crown events.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
var crownSequencer: WKCrownSequencer { get }
```

#### Discussion

Use the object in this property to monitor crown-related events yourself. You can use this object in an interface that also includes a [`WKInterfacePicker`](https://developer.apple.com/documentation/watchkit/wkinterfacepicker), but only one of those objects can receive crown events at any given time. For information about how to configure a crown sequencer object, see [`WKCrownSequencer`](https://developer.apple.com/documentation/watchkit/wkcrownsequencer).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/crownsequencer)*