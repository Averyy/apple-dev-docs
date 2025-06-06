# FSEventStreamCallback

**Framework**: Core Services  
**Kind**: tdef

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
typealias FSEventStreamCallback = (ConstFSEventStreamRef, UnsafeMutableRawPointer?, Int, UnsafeMutableRawPointer, UnsafePointer<FSEventStreamEventFlags>, UnsafePointer<FSEventStreamEventId>) -> Void
```

#### Discussion

This is the type of the callback function supplied by the client when creating a new stream. This callback is invoked by the service from the client's runloop(s) when events occur, per the parameters specified when the stream was created.

## Parameters

- `streamRef`: The stream for which event(s) occurred.
- `clientCallBackInfo`: The info field that was supplied in the context when this stream was created.
- `numEvents`: The number of events being reported in this callback. Each of the arrays (eventPaths, eventFlags, eventIds) will have this many elements.
- `eventPaths`: A path might be "/" if ether of these flags is set for the event: kFSEventStreamEventFlagUserDropped, kFSEventStreamEventFlagKernelDropped.
- `eventFlags`: An array of flag words corresponding to the paths in the eventPaths parameter. If no flags are set, then there was some change in the directory at the specific path supplied in this event. See FSEventStreamEventFlags.
- `eventIds`: Each event ID comes from the most recent event being reported in the corresponding directory named in the eventPaths parameter. Event IDs all come from a single global source. They are guaranteed to always be increasing, usually in leaps and bounds, even across system reboots and moving drives from one machine to another. Just before invoking your callback your stream is updated so that calling the accessor FSEventStreamGetLatestEventId() will return the largest of the values passed in the eventIds parameter; if you were to stop processing events from this stream after this callback and resume processing them later from a newly-created FSEventStream, this is the value you would pass for the sinceWhen parameter to the FSEventStreamCreate...() function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fseventstreamcallback)*