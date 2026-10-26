# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.12+

## Declaration

*Mac Catalyst*

```c
enum : unsigned int;
```

*macOS*

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kLSLaunchHasUntrustedContents](./api-1645929-anonymous/klslaunchhasuntrustedcontents.md)
  A request that the system marks the launch items as untrustworthy. 
- [kLSLaunchInClassic](./api-1645929-anonymous/klslaunchinclassic.md)
  A request that the system forces the app to launch in the Classic emulation environment.
- [kLSLaunchInhibitBGOnly](./api-1645929-anonymous/klslaunchinhibitbgonly.md)
  A request that the system fails the launch if the app is background-only.
- [kLSLaunchNoParams](./api-1645929-anonymous/klslaunchnoparams.md)
  A request that the system uses the app’s information property to determine the launch parameters.
- [kLSLaunchStartClassic](./api-1645929-anonymous/klslaunchstartclassic.md)
  A request that the system starts up the Classic emulation environment if the app requires it. If this flag is not set and the app requires the Classic environment, the launch fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1645929-anonymous)*