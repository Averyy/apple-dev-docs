# maximumPathLength

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The maximum allowed length of the path to the UNIX domain socket.

**Availability**:
- macOS 14.0+

## Declaration

```objc
@property (class, readonly) NSUInteger maximumPathLength;
```

#### Discussion

The `sockaddr_un` structure in Linux defines the maximum length for this path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaunixsocketcachingoptions/maximumpathlength)*