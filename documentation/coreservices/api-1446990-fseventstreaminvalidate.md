# FSEventStreamInvalidate(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamInvalidate(_ streamRef: FSEventStreamRef)
```

#### Discussion

Invalidates the stream, like CFRunLoopSourceInvalidate() does for a CFRunLoopSourceRef. It will be unscheduled from any runloops or dispatch queues upon which it had been scheduled.

FSEventStreamInvalidate() can only be called on the stream after you have called FSEventStreamScheduleWithRunLoop() or FSEventStreamSetDispatchQueue().

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446990-fseventstreaminvalidate)*