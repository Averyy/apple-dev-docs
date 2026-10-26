# Launch Apple Event Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

In a `kAEOpenApplication` event, specify information about how the receiving application was launched.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
enum : AEKeyword {
    ...
};
```

## Topics

### Constants
- [keyAELaunchedAsLogInItem](./api-1556410-launch_apple_event_constants/keyaelaunchedasloginitem.md)
  If present in a `kAEOpenApplication` event, the receiving application was launched as a login item and should only perform actions suitable to that environment—for example, it probably shouldn't open an untitled document.
- [keyAELaunchedAsServiceItem](./api-1556410-launch_apple_event_constants/keyaelaunchedasserviceitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1556410-launch_apple_event_constants)*