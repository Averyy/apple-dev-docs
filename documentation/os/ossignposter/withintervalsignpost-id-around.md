# withIntervalSignpost(_:id:_:around:)

**Framework**: os  
**Kind**: method

Measures the execution of a closure and attaches the specified message.

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
func withIntervalSignpost<T>(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata, around task: () throws -> T) rethrows -> T
```

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`SignpostMetadata`](signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

 Don’t create an instance of [`SignpostMetadata`](signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously. If only one interval with a specific configuration can execute at any particular time, pass [`exclusive`](ossignpostid/exclusive.md) as the `id` parameter. Otherwise, use the [`makeSignpostID()`](ossignposter/makesignpostid().md) and [`makeSignpostID(from:)`](ossignposter/makesignpostid(from:).md) methods to generate a signpost identifier, as the following example shows:

```swift
let accountNumber = "12345678"
                
// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the signpost.
let signpostID = signposter.makeSignpostID()
        
// Signpost the interval of a closure that encapsulates
// one or more related tasks, and attach a message that
// securely interpolates sensitive data.
signposter.withIntervalSignpost("Account Reconciliation", id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))") {
    
    // Perform the related tasks.
    processTransactions()
    updateBalance()
}
```

## Parameters

- `name`: The signpost’s name.
- `id`: The signpost’s ID. The default value is  .
- `message`: The interpolated string that the signposter attaches to the signpost. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see  .
- `task`: The closure around which to create the signposted interval.

## See Also

- [func withIntervalSignpost<T>(StaticString, id: OSSignpostID, around: () throws -> T) rethrows -> T](ossignposter/withintervalsignpost(_:id:around:).md)
  Measures the execution of the specified closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/withintervalsignpost(_:id:_:around:))*