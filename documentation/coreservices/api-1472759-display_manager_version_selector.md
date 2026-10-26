# Display Manager Version Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies version information for the Display Manager.

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
- [gestaltDisplayMgrVers](./api-1472759-display_manager_version_selector/gestaltdisplaymgrvers.md)
  The `Gestalt` selector you pass to determine what version of the Display Manager is present. For example, a Gestalt result may be 0x00020500, which means that the Display Manager version 2.5 is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472759-display_manager_version_selector)*