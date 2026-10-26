# kFSEventStreamEventFlagUserDropped

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
kFSEventStreamEventFlagUserDropped = 0x00000002
```

#### Discussion

The kFSEventStreamEventFlagUserDropped or kFSEventStreamEventFlagKernelDropped flags may be set in addition to the kFSEventStreamEventFlagMustScanSubDirs flag to indicate that a problem occurred in buffering the events (the particular flag set indicates where the problem occurred) and that the client must do a full scan of any directories (and their subdirectories, recursively) being monitored by this stream. If you asked to monitor multiple paths with this stream then you will be notified about all of them. Your code need only check for the kFSEventStreamEventFlagMustScanSubDirs flag; these flags (if present) only provide information to help you diagnose the problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflaguserdropped)*