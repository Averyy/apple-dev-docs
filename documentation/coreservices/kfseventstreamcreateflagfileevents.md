# kFSEventStreamCreateFlagFileEvents

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
var kFSEventStreamCreateFlagFileEvents: Int { get }
```

#### Discussion

Request file-level notifications. Your stream will receive events about individual files in the hierarchy you're watching instead of only receiving directory level notifications. Use this flag with care as it will generate significantly more events than without it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagfileevents)*