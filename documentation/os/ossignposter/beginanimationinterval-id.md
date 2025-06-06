# beginAnimationInterval(_:id:_:)

**Framework**: os  
**Kind**: method

Begins a signposted interval for measuring an animation, and attaches a message.

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
func beginAnimationInterval(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata) -> OSSignpostIntervalState
```

#### Return Value

The interval state that the signposter derives from the specified `id` parameter.

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`SignpostMetadata`](signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

 Don’t create an instance of [`SignpostMetadata`](signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously. If only one interval with a specific configuration can execute at any particular time, use [`exclusive`](ossignpostid/exclusive.md) for the `id` parameter. Otherwise, use the [`makeSignpostID()`](ossignposter/makesignpostid().md) and [`makeSignpostID(from:)`](ossignposter/makesignpostid(from:).md) methods to generate a signpost identifier.

To end a signposted interval, pass the return value to one of the [`endInterval(_:_:)`](ossignposter/endinterval(_:_:).md) or [`endInterval(_:_:_:)`](ossignposter/endinterval(_:_:_:).md) methods. If you don’t have access to the returned interval state when you want to end the signposted interval, recreate it by passing the same signpost ID to the [`beginState(id:)`](ossignpostintervalstate/beginstate(id:).md) method.

If you need to pass the returned interval state across process boundaries, you must encode it first. For more information, see [`OSSignpostIntervalState`](ossignpostintervalstate.md).

The following example shows how to use a signpost ID and interval state to signpost the beginning and the end of an interval that measures an animation, and also demonstrates the use of message interpolation:

```swift
let x: CGFloat = 0.235
let y: CGFloat = 6.12
        
// Create a signposter that uses the default subsystem.
let signposter = OSSignposter()
                
// Generate a signpost ID to associate with the signposted interval.
let signpostID = signposter.makeSignpostID()
                
// Create a name that the signposter uses, along with the 
// signpost ID, to disambiguate the begin call and end call. 
// The type must be StaticString.
let name: StaticString = "Animation"
        
// Begin the signposted interval and attach a message that interpolates
// the current location of the animated object.
let state = signposter.beginAnimationInterval(name, id: signpostID,
    "x:\(x, align: .right(columns: 5)) y:\(y, align: .right(columns: 5))")
                
// Perform the animation that you want to measure.
                
// Use the interval state from the begin call to end the
// corresponding signposted interval.
signposter.endInterval(name, state)
```

## Parameters

- `name`: The signpost’s name.
- `id`: The signpost’s identifier. The default value is  .
- `message`: The interpolated string that the signposter attaches to the signpost. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see  .

## See Also

- [func beginInterval(StaticString, id: OSSignpostID) -> OSSignpostIntervalState](ossignposter/begininterval(_:id:).md)
  Begins a signposted interval.
- [func beginInterval(StaticString, id: OSSignpostID, SignpostMetadata) -> OSSignpostIntervalState](ossignposter/begininterval(_:id:_:).md)
  Begins a signposted interval and attaches the specified message.
- [func beginAnimationInterval(StaticString, id: OSSignpostID) -> OSSignpostIntervalState](ossignposter/beginanimationinterval(_:id:).md)
  Begins a signposted interval for measuring an animation.
- [class OSSignpostIntervalState](ossignpostintervalstate.md)
  An object that tracks the state of a signposted interval.
- [typealias SignpostMetadata](signpostmetadata.md)
  The type that represents a message you attach to a signpost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/beginanimationinterval(_:id:_:))*