# recordingFailed

**Framework**: WatchKit  
**Kind**: property  
**Role**: Type Property

An audio recording error.

**Availability**:
- watchOS

## Declaration

```swift
static var recordingFailed: WatchKitError.Code { get }
```

#### Discussion

WatchKit reports this error when it’s unable to record audio using the audio recording interface.

## See Also

### Accessing Error Codes
- [static var downloadFailed: WatchKitError.Code](./downloadfailed.md)
  A download error.
- [static var invalidArgument: WatchKitError.Code](./invalidargument.md)
  An invalid argument error.
- [static var mediaPlayerFailed: WatchKitError.Code](./mediaplayerfailed.md)
  A media player error.
- [static var unknown: WatchKitError.Code](./unknown.md)
  An unknown error.
- [static var applicationDelegateWatchKitRequestReplyNotCalled: WatchKitError.Code](./applicationdelegatewatchkitrequestreplynotcalled.md)
  An unresponsive delegate error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/watchkiterror/recordingfailed)*