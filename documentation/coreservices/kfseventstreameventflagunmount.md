# kFSEventStreamEventFlagUnmount

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var kFSEventStreamEventFlagUnmount: Int { get }
```

#### Discussion

Denotes a special event sent when a volume is unmounted underneath one of the paths being monitored. The path in the event is the path to the directory from which the volume was unmounted. You will receive one of these notifications for every volume unmount event inside the kernel. This is not a substitute for the notifications provided by the DiskArbitration framework; you only get notified after the unmount has occurred. Beware that unmounting a volume could uncover an arbitrarily large directory hierarchy, although macOS never does that.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreameventflagunmount)*