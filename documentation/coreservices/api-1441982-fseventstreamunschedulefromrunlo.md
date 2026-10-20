# FSEventStreamUnscheduleFromRunLoop(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.5+ - Deprecated in 13.0

> **Deprecated**: Use [`FSEventStreamSetDispatchQueue(_:_:)`](./api-1444164-fseventstreamsetdispatchqueue.md) instead.

## Declaration

```swift
func FSEventStreamUnscheduleFromRunLoop(_ streamRef: FSEventStreamRef, _ runLoop: CFRunLoop, _ runLoopMode: CFString)
```

```c
void FSEventStreamUnscheduleFromRunLoop(FSEventStreamRef streamRef, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

#### Discussion

This function removes the stream from the specified run loop, like CFRunLoopRemoveSource() does for a CFRunLoopSourceRef.

## Parameters

- `streamRef`: A valid stream.
- `runLoop`: The run loop from which to unschedule the stream.
- `runLoopMode`: The run loop mode from which to unschedule the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441982-fseventstreamunschedulefromrunlo)*