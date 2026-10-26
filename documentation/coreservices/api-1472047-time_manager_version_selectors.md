# Time Manager Version Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify version information for the Time Manager.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltTimeMgrVersion](./api-1472047-time_manager_version_selectors/gestalttimemgrversion.md)
  The Gestalt selector you pass to determine what version of the Time Manager is present.
- [gestaltStandardTimeMgr](./api-1472047-time_manager_version_selectors/gestaltstandardtimemgr.md)
  If this bit is set, the original Time Manager is present.
- [gestaltRevisedTimeMgr](./api-1472047-time_manager_version_selectors/gestaltrevisedtimemgr.md)
  If this bit is set, the revised Time Manager is present.
- [gestaltExtendedTimeMgr](./api-1472047-time_manager_version_selectors/gestaltextendedtimemgr.md)
  If this bit is set, the extended Time Manager is present.
- [gestaltNativeTimeMgr](./api-1472047-time_manager_version_selectors/gestaltnativetimemgr.md)
  If this bit is set, the native Time Manager is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472047-time_manager_version_selectors)*