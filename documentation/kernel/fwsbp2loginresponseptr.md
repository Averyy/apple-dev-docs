# FWSBP2LoginResponsePtr

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct FWSBP2LoginResponse *FWSBP2LoginResponsePtr;
```

## See Also

- [IOFireWireSBP2Login](iofirewiresbp2login.md)
  Supplies the login maintenance and Normal Command ORB execution portions of the API.
- [IOFireWireSBP2ManagementORB](iofirewiresbp2managementorb.md)
  Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LUN interface.
- [IOFireWireSBP2ORB](iofirewiresbp2orb.md)
  Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2Login.
- [FWSBP2FetchAgentWriteCallback](fwsbp2fetchagentwritecallback.md)
- [FWSBP2LoginCallback](fwsbp2logincallback.md)
- [FWSBP2LoginCompleteParams](fwsbp2logincompleteparams.md)
- [FWSBP2LoginCompleteParamsPtr](fwsbp2logincompleteparamsptr.md)
- [FWSBP2LoginResponse](fwsbp2loginresponse.md)
- [FWSBP2LogoutCallback](fwsbp2logoutcallback.md)
- [FWSBP2LogoutCompleteParams](fwsbp2logoutcompleteparams.md)
- [FWSBP2LogoutCompleteParamsPtr](fwsbp2logoutcompleteparamsptr.md)
- [FWSBP2ManagementCallback](fwsbp2managementcallback.md)
- [FWSBP2NotifyCallback](fwsbp2notifycallback.md)
- [FWSBP2NotifyParams](fwsbp2notifyparams.md)
- [FWSBP2NotifyParamsPtr](fwsbp2notifyparamsptr.md)
- [FWSBP2ReconnectParams](fwsbp2reconnectparams.md)
- [FWSBP2ReconnectParamsPtr](fwsbp2reconnectparamsptr.md)
- [FWSBP2StatusBlock](fwsbp2statusblock.md)
- [FWSBP2StatusCallback](fwsbp2statuscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fwsbp2loginresponseptr)*