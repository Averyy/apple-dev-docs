# WatchKitError

**Framework**: Watchkit  
**Kind**: struct

An error reported by WatchKit.

**Availability**:
- watchOS ?+

## Declaration

```swift
struct WatchKitError
```

## Topics

### Accessing Error Codes
- [static var downloadFailed: WatchKitError.Code](watchkiterror/downloadfailed.md)
  A download error.
- [static var invalidArgument: WatchKitError.Code](watchkiterror/invalidargument.md)
  An invalid argument error.
- [static var mediaPlayerFailed: WatchKitError.Code](watchkiterror/mediaplayerfailed.md)
  A media player error.
- [static var recordingFailed: WatchKitError.Code](watchkiterror/recordingfailed.md)
  An audio recording error.
- [static var unknown: WatchKitError.Code](watchkiterror/unknown.md)
  An unknown error.
- [static var applicationDelegateWatchKitRequestReplyNotCalled: WatchKitError.Code](watchkiterror/applicationdelegatewatchkitrequestreplynotcalled.md)
  An unresponsive delegate error.
### Accessing the Error Domain
- [let WatchKitErrorDomain: String](watchkiterrordomain.md)
  The domain for WatchKit errors.
### Accessing Error Properties
- [WatchKitError.Code](watchkiterror/code.md)
  Error codes reported by WatchKit.
### Type Properties
- [static var errorDomain: String](watchkiterror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/watchkiterror)*