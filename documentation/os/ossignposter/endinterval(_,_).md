# endInterval(_:_:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Ends the signposted interval that corresponds to the specified name and state.

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
func endInterval(_ name: StaticString, _ state: OSSignpostIntervalState)
```

## Mentions

- [Recording Performance Data](../recording-performance-data.md)

#### Discussion

The signposter uses interval state to enforce the following runtime assertions:

- Multiple end calls don’t consume the same interval state.
- The begin call and end call use the same name.
- The begin call and end call emit signposts to the same underlying log.
- You don’t use the [`exclusive`](../ossignpostid/exclusive.md) signpost ID for intervals that cross process boundaries.

In debug builds, any assertion failures result in a crash. In production builds, your app continues to run and, instead, the signposter attaches an error message to the interval’s closing signpost.

If you don’t have access to the returned interval state from the corresponding begin call, or the cost you incur when serializing the state to pass between processes is unacceptable, recreate the interval state by passing the interval’s signpost ID to [`beginState(id:)`](../ossignpostintervalstate/beginstate%28id%29.md). For more information about serializing interval state, see [`OSSignpostIntervalState`](../ossignpostintervalstate.md).

> ❗ **Important**:  Recreating interval state using the [`beginState(id:)`](../ossignpostintervalstate/beginstate%28id%29.md) method bypasses runtime assertions that check for consistency between the beginning and the end of a signposted interval.

The following example demonstrates how to recreate interval state in a scope other than the one that includes the begin call:

```swift
// A closure that represents a process in the context of this example.
let processA: () -> OSSignpostID = {
    // Create a signposter that uses the default subsystem.
    let signposter = OSSignposter()
            
    // Generate a signpost ID to associate with the signposted interval.
    let signpostID = signposter.makeSignpostID()
            
    // Begin a signposted interval and return the signpost ID to the caller.
    let _ = signposter.beginInterval("Example", id: signpostID)
    return signpostID
}
        
// Another closure representing a different process.
let processB: (OSSignpostID) -> Void = { signpostID in
    // Create a signposter that uses the same subsystem as
    // the original, which, in this case, is the default.
    let signposter = OSSignposter()
            
    // Recreate the interval state using the provided signpost ID.
    let state = OSSignpostIntervalState.beginState(id: signpostID)
            
    // End the signposted interval using the recreated state.
    signposter.endInterval("Example", state)
}
        
// Execute the two closures.
let signpostID = processA()
processB(signpostID)
```

## Parameters

- `name`: The signpost’s name.
- `state`: The returned interval state from the matching begin call.

## See Also

### Stopping a Signposted Interval
- [func endInterval(StaticString, OSSignpostIntervalState, SignpostMetadata)](./endinterval%28_,_,_%29.md)
  Ends a signposted interval and attaches the specified message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/endinterval(_:_:))*