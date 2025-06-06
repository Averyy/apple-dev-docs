# FSEventStreamStop(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamStop(_ streamRef: FSEventStreamRef)
```

#### Discussion

Unregisters with the FS Events service. The client callback will not be called for this stream while it is stopped.

FSEventStreamStop() can only be called if the stream has been started, via FSEventStreamStart().

Once stopped, the stream can be restarted via FSEventStreamStart(), at which point it will resume receiving events from where it left off ("sinceWhen").

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447673-fseventstreamstop)*