# FSEventStreamStart(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamStart(_ streamRef: FSEventStreamRef) -> Bool
```

#### Return_value

True if it succeeds, otherwise False if it fails. It ought to always succeed, but in the event it does not then your code should fall back to performing recursive scans of the directories of interest as appropriate.

#### Discussion

Attempts to register with the FS Events service to receive events per the parameters in the stream.

FSEventStreamStart() can only be called once the stream has been scheduled on at least one runloop, via FSEventStreamScheduleWithRunLoop().

Once started, the stream can be stopped via FSEventStreamStop().

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448000-fseventstreamstart)*