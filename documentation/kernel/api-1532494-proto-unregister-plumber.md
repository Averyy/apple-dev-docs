# proto_unregister_plumber

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void proto_unregister_plumber(protocol_family_t proto_fam, ifnet_family_t if_fam);
```

#### Discussion

Unregisters a previously registered plumbing function.

## Parameters

- `proto_fam`: The protocol family these plumbing functions handle.
- `if_fam`: The interface family these plumbing functions handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1532494-proto_unregister_plumber)*