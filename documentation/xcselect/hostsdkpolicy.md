# HostSDKPolicy

**Framework**: xcselect  
**Kind**: enum  
**Role**: Enumeration

Describe the preferred policy for locating an SDK appropriate for building host content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
enum HostSDKPolicy
```

```c
enum xcselect_host_sdk_policy_t : uint32_t;
```

## Topics

### Enumeration Cases
- [HostSDKPolicy.latest](./hostsdkpolicy/latest.md)
  Return the latest macOS SDK available.
- [HostSDKPolicy.matchingOnly](./hostsdkpolicy/matchingonly.md)
  Return an SDK that matches the host’s major OS version.
- [HostSDKPolicy.matchingPreferred](./hostsdkpolicy/matchingpreferred.md)
  Return an SDK that matches the host’s major OS version if it is available, otherwise return the latest macOS SDK available.
### Initializers
- [init?(rawValue: UInt32)](./hostsdkpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcselect/hostsdkpolicy)*