# FSEventStreamCreate(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamCreate(_ allocator: CFAllocator?, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ pathsToWatch: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef?
```

#### Return_value

A valid FSEventStreamRef.

#### Discussion

Creates a new FS event stream object with the given parameters. In order to start receiving callbacks you must also call FSEventStreamScheduleWithRunLoop() and FSEventStreamStart().

## Parameters

- `allocator`: The CFAllocator to be used to allocate memory for the stream. Pass NULL or kCFAllocatorDefault to use the current default allocator.
- `callback`: An FSEventStreamCallback which will be called when FS events occur.
- `context`: A pointer to the FSEventStreamContext structure the client wants to associate with this stream. Its fields are copied out into the stream itself so its memory can be released after the stream is created. Passing NULL is allowed and has the same effect as passing a structure whose fields are all set to zero.
- `pathsToWatch`: A CFArray of CFStringRefs, each specifying a path to a directory, signifying the root of a filesystem hierarchy to be watched for modifications.
- `sinceWhen`: The service will supply events that have happened after the given event ID. To ask for events "since now" pass the constant kFSEventStreamEventIdSinceNow. Often, clients will supply the highest-numbered FSEventStreamEventId they have received in a callback, which they can obtain via the FSEventStreamGetLatestEventId() accessor. Do not pass zero for sinceWhen, unless you want to receive events for every directory modified since "the beginning of time" -- an unlikely scenario.
- `latency`: The number of seconds the service should wait after hearing about an event from the kernel before passing it along to the client via its callback. Specifying a larger value may result in more effective temporal coalescing, resulting in fewer callbacks and greater overall efficiency.
- `flags`: Flags that modify the behavior of the stream being created. See FSEventStreamCreateFlags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate)*