# FSEventStreamSetDispatchQueue(_:_:)

**Framework**: Core Services  
**Kind**: func

Schedules the stream on the specified dispatch queue.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func FSEventStreamSetDispatchQueue(_ streamRef: FSEventStreamRef, _ q: dispatch_queue_t?)
```

#### Discussion

The caller is responsible for ensuring that the stream is scheduled on a dispatch queue and that the queue is started.

If there’s a problem scheduling the stream on the queue, an error will be returned when you try to start the stream.

To start receiving events on the stream, call [`FSEventStreamStart(_:)`](1448000-fseventstreamstart.md).

To remove the stream from the queue on which it was scheduled, call [`FSEventStreamSetDispatchQueue(_:_:)`](1444164-fseventstreamsetdispatchqueue.md) with a `NULL` queue parameter or call [`FSEventStreamInvalidate(_:)`](1446990-fseventstreaminvalidate.md) which does the same thing. You must eventually call [`FSEventStreamInvalidate(_:)`](1446990-fseventstreaminvalidate.md) and it’s an error to call [`FSEventStreamInvalidate(_:)`](1446990-fseventstreaminvalidate.md) without having the stream either scheduled on a runloop or a dispatch queue, so don’t set the dispatch queue to `NULL` before calling [`FSEventStreamInvalidate(_:)`](1446990-fseventstreaminvalidate.md).

## Parameters

- `streamRef`: A valid stream.
- `q`: The dispatch queue to use to receive events (or   to stop receiving events from the stream).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444164-fseventstreamsetdispatchqueue)*