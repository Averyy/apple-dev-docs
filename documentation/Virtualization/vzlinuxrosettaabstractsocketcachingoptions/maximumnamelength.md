# maximumNameLength

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The maximum length of name that the framework allows.

**Availability**:
- macOS 14.0+

## Declaration

```objc
@property (class, readonly) NSUInteger maximumNameLength;
```

#### Discussion

The `sockaddr_un` structure in Linux defines the maximum length for the path [`name`](./name.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaabstractsocketcachingoptions/maximumnamelength)*