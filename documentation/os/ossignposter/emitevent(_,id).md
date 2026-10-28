# emitEvent(_:id:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Marks a point of interest in time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func emitEvent(_ name: StaticString, id: OSSignpostID = .exclusive)
```

## Mentions

- [Recording Performance Data](../recording-performance-data.md)

## Discussion

You can use the [`makeSignpostID()`](./makesignpostid%28%29.md) and [`makeSignpostID(from:)`](./makesignpostid%28from%29.md) methods to generate an identifier for the event, as the following example shows:

```swift
// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the event.
let signpostID = signposter.makeSignpostID()
        
// Emit a named event using the signpost ID.
signposter.emitEvent("Example Event", id: signpostID)
```

## Parameters

- `name`: The event’s name.
- `id`: The event’s identifier. The default value is [`exclusive`](../ossignpostid/exclusive.md).

## See Also

### Emitting Individual Signposts
- [func emitEvent(StaticString, id: OSSignpostID, SignpostMetadata)](./emitevent%28_,id,_%29.md)
  Marks a point of interest in time and attaches the specified message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:))*