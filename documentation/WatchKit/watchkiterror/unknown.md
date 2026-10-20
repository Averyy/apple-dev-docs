# unknown

**Framework**: WatchKit  
**Kind**: property  
**Role**: Type Property

An unknown error.

**Availability**:
- watchOS

## Declaration

```swift
static var unknown: WatchKitError.Code { get }
```

#### Discussion

WatchKit reports this error when it can’t determine the precise reason for the failure.

## See Also

### Accessing Error Codes
- [static var downloadFailed: WatchKitError.Code](./downloadfailed.md)
  A download error.
- [static var invalidArgument: WatchKitError.Code](./invalidargument.md)
  An invalid argument error.
- [static var mediaPlayerFailed: WatchKitError.Code](./mediaplayerfailed.md)
  A media player error.
- [static var recordingFailed: WatchKitError.Code](./recordingfailed.md)
  An audio recording error.
- [static var applicationDelegateWatchKitRequestReplyNotCalled: WatchKitError.Code](./applicationdelegatewatchkitrequestreplynotcalled.md)
  An unresponsive delegate error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/watchkiterror/unknown)*