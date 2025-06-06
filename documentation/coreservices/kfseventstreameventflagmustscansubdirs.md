# kFSEventStreamEventFlagMustScanSubDirs

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var kFSEventStreamEventFlagMustScanSubDirs: Int { get }
```

#### Discussion

Your application must rescan not just the directory given in the event, but all its children, recursively. This can happen if there was a problem whereby events were coalesced hierarchically. For example, an event in /Users/jsmith/Music and an event in /Users/jsmith/Pictures might be coalesced into an event with this flag set and path=/Users/jsmith. If this flag is set you may be able to get an idea of whether the bottleneck happened in the kernel (less likely) or in your client (more likely) by checking for the presence of the informational flags kFSEventStreamEventFlagUserDropped or kFSEventStreamEventFlagKernelDropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagmustscansubdirs)*