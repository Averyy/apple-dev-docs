# kFSEventStreamEventFlagEventIdsWrapped

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
kFSEventStreamEventFlagEventIdsWrapped = 0x00000008
```

## Discussion

If kFSEventStreamEventFlagEventIdsWrapped is set, it means the 64-bit event ID counter wrapped around. As a result, previously-issued event ID's are no longer valid arguments for the sinceWhen parameter of the FSEventStreamCreate...() functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1455361-fseventstreameventflags/kfseventstreameventflageventidswrapped)*