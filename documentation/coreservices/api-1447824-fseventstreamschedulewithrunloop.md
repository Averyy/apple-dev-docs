# FSEventStreamScheduleWithRunLoop(_:_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.5+ - Deprecated in 13.0

## Declaration

```swift
func FSEventStreamScheduleWithRunLoop(_ streamRef: FSEventStreamRef, _ runLoop: CFRunLoop, _ runLoopMode: CFString)
```

#### Discussion

This function schedules the stream on the specified run loop, like CFRunLoopAddSource() does for a CFRunLoopSourceRef. The caller is responsible for ensuring that the stream is scheduled on at least one run loop and that at least one of the run loops on which the stream is scheduled is being run.

To start receiving events on the stream, call FSEventStreamStart().

To remove the stream from the run loops upon which it has been scheduled, call FSEventStreamUnscheduleFromRunLoop() or FSEventStreamInvalidate().

## Parameters

- `streamRef`: A valid stream.
- `runLoop`: The run loop on which to schedule the stream.
- `runLoopMode`: A run loop mode on which to schedule the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447824-fseventstreamschedulewithrunloop)*