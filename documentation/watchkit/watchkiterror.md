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
- [static var downloadFailed: WatchKitError.Code](downloadfailed.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/downloadfailed))
  A download error.
- [static var invalidArgument: WatchKitError.Code](invalidargument.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/invalidargument))
  An invalid argument error.
- [static var mediaPlayerFailed: WatchKitError.Code](mediaplayerfailed.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/mediaplayerfailed))
  A media player error.
- [static var recordingFailed: WatchKitError.Code](recordingfailed.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/recordingfailed))
  An audio recording error.
- [static var unknown: WatchKitError.Code](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/unknown))
  An unknown error.
- [static var applicationDelegateWatchKitRequestReplyNotCalled: WatchKitError.Code](applicationdelegatewatchkitrequestreplynotcalled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/applicationdelegatewatchkitrequestreplynotcalled))
  An unresponsive delegate error.
### Accessing the Error Domain
- [let WatchKitErrorDomain: String](watchkiterrordomain.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterrordomain))
  The domain for WatchKit errors.
### Accessing Error Properties
- [WatchKitError.Code](code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/code))
  Error codes reported by WatchKit.
### Type Properties
- [static var errorDomain: String](errordomain.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/watchkiterror/errordomain))

## Relationships

### Conforms To
- CustomNSError ([Apple Docs](https://developer.apple.com/documentation/Foundation/CustomNSError))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Error ([Apple Docs](https://developer.apple.com/documentation/Swift/Error))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/watchkiterror)*