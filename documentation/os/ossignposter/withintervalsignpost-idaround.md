# withIntervalSignpost(_:id:around:)

**Framework**: os  
**Kind**: method

Measures the execution of the specified closure.

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
func withIntervalSignpost<T>(_ name: StaticString, id: OSSignpostID = .exclusive, around task: () throws -> T) rethrows -> T
```

#### Discussion

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously. If only one interval with a specific configuration can execute at any particular time, pass [`exclusive`](ossignpostid/exclusive.md) as the `id` parameter. Otherwise, use the [`makeSignpostID()`](ossignposter/makesignpostid().md) and [`makeSignpostID(from:)`](ossignposter/makesignpostid(from:).md) methods to generate a signpost identifier, as the following example shows:

```swift
// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the signpost.
let signpostID = signposter.makeSignpostID()
        
// Signpost the interval of a closure that encapsulates 
// one or more related tasks.
signposter.withIntervalSignpost("Example Signpost", id: signpostID) {
    // Perform one or more related tasks.
}
```

## Parameters

- `name`: The signpost’s name.
- `id`: The signpost’s ID. The default value is  .
- `task`: The closure around which to create the signposted interval.

## See Also

- [func withIntervalSignpost<T>(StaticString, id: OSSignpostID, SignpostMetadata, around: () throws -> T) rethrows -> T](ossignposter/withintervalsignpost(_:id:_:around:).md)
  Measures the execution of a closure and attaches the specified message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/withintervalsignpost(_:id:around:))*