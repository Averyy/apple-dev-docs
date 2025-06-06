# FSEventStreamCreateRelativeToDevice(_:_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamCreateRelativeToDevice(_ allocator: CFAllocator?, _ callback: FSEventStreamCallback, _ context: UnsafeMutablePointer<FSEventStreamContext>?, _ deviceToWatch: dev_t, _ pathsToWatchRelativeToDevice: CFArray, _ sinceWhen: FSEventStreamEventId, _ latency: CFTimeInterval, _ flags: FSEventStreamCreateFlags) -> FSEventStreamRef?
```

#### Return_value

A valid FSEventStreamRef.

#### Discussion

Creates a new FS event stream object for a particular device with the given parameters. In order to start receiving callbacks you must also call FSEventStreamScheduleWithRunLoop() and FSEventStreamStart().

## Parameters

- `allocator`: The CFAllocator to be used to allocate memory for the stream. Pass NULL or kCFAllocatorDefault to use the current default allocator.
- `callback`: An FSEventStreamCallback which will be called when FS events occur.
- `context`: A pointer to the FSEventStreamContext structure the client wants to associate with this stream. Its fields are copied out into the stream itself so its memory can be released after the stream is created.
- `deviceToWatch`: A dev_t corresponding to the device which you want to receive notifications from. The dev_t is the same as the st_dev field from a stat structure of a file on that device or the f_fsid[0] field of a statfs structure. If the value of dev is zero, it is ignored.
- `pathsToWatchRelativeToDevice`: A CFArray of CFStringRefs, each specifying a relative path to a directory on the device identified by the dev parameter. The paths should be relative to the root of the device. For example, if a volume "MyData" is mounted at "/Volumes/MyData" and you want to watch "/Volumes/MyData/Pictures/July", specify a path string of "Pictures/July". To watch the root of a volume pass a path of "" (the empty string).
- `sinceWhen`: The service will supply events that have happened after the given event ID. To ask for events "since now" pass the constant kFSEventStreamEventIdSinceNow. Often, clients will supply the highest-numbered FSEventStreamEventId they have received in a callback, which they can obtain via the FSEventStreamGetLatestEventId() accessor. Do not pass zero for sinceWhen, unless you want to receive events for every directory modified since "the beginning of time" -- an unlikely scenario.
- `latency`: The number of seconds the service should wait after hearing about an event from the kernel before passing it along to the client via its callback. Specifying a larger value may result in more effective temporal coalescing, resulting in fewer callbacks.
- `flags`: Flags that modify the behavior of the stream being created. See FSEventStreamCreateFlags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev)*