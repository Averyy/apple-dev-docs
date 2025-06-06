# FSEventStreamFlushAsync(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamFlushAsync(_ streamRef: FSEventStreamRef) -> FSEventStreamEventId
```

#### Return_value

The largest event id of any event ever queued for this stream, otherwise zero if no events have been queued for this stream.

#### Discussion

Asks the FS Events service to flush out any events that have occurred but have not yet been delivered, due to the latency parameter that was supplied when the stream was created. This flushing occurs asynchronously -- do not expect the events to have already been delivered by the time this call returns.

FSEventStreamFlushAsync() can only be called after the stream has been started, via FSEventStreamStart().

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441727-fseventstreamflushasync)*