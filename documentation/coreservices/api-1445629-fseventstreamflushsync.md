# FSEventStreamFlushSync(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamFlushSync(_ streamRef: FSEventStreamRef)
```

#### Discussion

Asks the FS Events service to flush out any events that have occurred but have not yet been delivered, due to the latency parameter that was supplied when the stream was created. This flushing occurs synchronously -- by the time this call returns, your callback will have been invoked for every event that had already occurred at the time you made this call.

FSEventStreamFlushSync() can only be called after the stream has been started, via FSEventStreamStart().

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445629-fseventstreamflushsync)*