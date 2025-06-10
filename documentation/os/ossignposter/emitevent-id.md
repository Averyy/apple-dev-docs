# emitEvent(_:id:_:)

**Framework**: os  
**Kind**: method

Marks a point of interest in time and attaches the specified message.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func emitEvent(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata)
```

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`SignpostMetadata`](signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

You can use the [`makeSignpostID()`](ossignposter/makesignpostid().md) and [`makeSignpostID(from:)`](ossignposter/makesignpostid(from:).md) methods to generate an identifier for the event, as the following example shows:

```swift
let accountNumber = "12345678"

// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the event.
let signpostID = signposter.makeSignpostID()
        
// Emit a named event using the signpost ID and attach a message
// that securely interpolates sensitive data.
signposter.emitEvent("New Account Created", id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))")
```

## Parameters

- `name`: The event’s name.
- `id`: The event’s identifier. The default value is  .
- `message`: The interpolated string that the signposter attaches to the event. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see  .

## See Also

- [func emitEvent(StaticString, id: OSSignpostID)](ossignposter/emitevent(_:id:).md)
  Marks a point of interest in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:_:))*