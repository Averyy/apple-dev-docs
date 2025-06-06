# FSEventStreamCopyPathsBeingWatched(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamCopyPathsBeingWatched(_ streamRef: ConstFSEventStreamRef) -> CFArray
```

#### Return_value

A CFArray of CFStringRefs corresponding to those supplied when the stream was created. Ownership follows the Copy rule.

#### Discussion

Fetches the paths supplied when the stream was created via one of the FSEventStreamCreate...() functions.

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447917-fseventstreamcopypathsbeingwatch)*