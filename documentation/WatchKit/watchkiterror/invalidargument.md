# invalidArgument

**Framework**: WatchKit  
**Kind**: property  
**Role**: Type Property

An invalid argument error.

**Availability**:
- watchOS

## Declaration

```swift
static var invalidArgument: WatchKitError.Code { get }
```

## Discussion

WatchKit reports this error when you specify invalid settings for one of the system supplied interfaces.

## See Also

### Accessing Error Codes
- [static var downloadFailed: WatchKitError.Code](./downloadfailed.md)
  A download error.
- [static var mediaPlayerFailed: WatchKitError.Code](./mediaplayerfailed.md)
  A media player error.
- [static var recordingFailed: WatchKitError.Code](./recordingfailed.md)
  An audio recording error.
- [static var unknown: WatchKitError.Code](./unknown.md)
  An unknown error.
- [static var applicationDelegateWatchKitRequestReplyNotCalled: WatchKitError.Code](./applicationdelegatewatchkitrequestreplynotcalled.md)
  An unresponsive delegate error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/watchkiterror/invalidargument)*