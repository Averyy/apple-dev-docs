# kFSEventStreamCreateFlagWatchRoot

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var kFSEventStreamCreateFlagWatchRoot: Int { get }
```

#### Discussion

Request notifications of changes along the path to the path(s) you're watching. For example, with this flag, if you watch "/foo/bar" and it is renamed to "/foo/bar.old", you would receive a RootChanged event. The same is true if the directory "/foo" were renamed. The event you receive is a special event: the path for the event is the original path you specified, the flag kFSEventStreamEventFlagRootChanged is set and event ID is zero. RootChanged events are useful to indicate that you should rescan a particular hierarchy because it changed completely (as opposed to the things inside of it changing). If you want to track the current location of a directory, it is best to open the directory before creating the stream so that you have a file descriptor for it and can issue an F_GETPATH fcntl() to find the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagwatchroot)*