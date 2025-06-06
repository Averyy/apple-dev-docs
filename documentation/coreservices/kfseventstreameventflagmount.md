# kFSEventStreamEventFlagMount

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var kFSEventStreamEventFlagMount: Int { get }
```

#### Discussion

Denotes a special event sent when a volume is mounted underneath one of the paths being monitored. The path in the event is the path to the newly-mounted volume. You will receive one of these notifications for every volume mount event inside the kernel (independent of DiskArbitration). Beware that a newly-mounted volume could contain an arbitrarily large directory hierarchy. Avoid pitfalls like triggering a recursive scan of a non-local filesystem, which you can detect by checking for the absence of the MNT_LOCAL flag in the f_flags returned by statfs(). Also be aware of the MNT_DONTBROWSE flag that is set for volumes which should not be displayed by user interface elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagmount)*