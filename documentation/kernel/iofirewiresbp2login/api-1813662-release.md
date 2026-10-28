# release

**Framework**: Kernel  
**Kind**: instm

Primary implementation of the release mechanism.

## Declaration

```cpp
virtual void release() const;
```

## Overview

See OSObject.h for more information. When retainCount == when then call free().

## See Also

### Miscellaneous
- [createORB](./api-1813411-createorb.md)
  Creates a new IOFireWireSBP2ORB for this login.
- [enableUnsolicitedStatus](./api-1813441-enableunsolicitedstatus.md)
  Enables unsolicited status.
- [getLoginFlags](./api-1813479-getloginflags.md)
  Returns the currently set login flags.
- [getLoginID](./api-1813507-getloginid.md)
  Returns the current login ID.
- [getMaxCommandBlockSize](./api-1813539-getmaxcommandblocksize.md)
  Returns the maximum command block size.
- [getMaxPayloadSize](./api-1813578-getmaxpayloadsize.md)
  Returns the currently set maximum payload size.
- [getReconnectTime](./api-1813610-getreconnecttime.md)
  Returns the currently set reconnect time.
- [getRefCon](./api-1813628-getrefcon.md)
  Returns the refCon set with setRefCon.
- [getStatusNotifyProc](./api-1813642-getstatusnotifyproc.md)
  Returns the callback to be called on normal command status.
- [getUnsolicitedStatusNotifyProc](./api-1813655-getunsolicitedstatusnotifyproc.md)
  Returns the callback to be called on unsolicited status.
- [ringDoorbell](./api-1813671-ringdoorbell.md)
  Rings the doorbell on the LUN.
- [setBusyTimeoutRegisterValue](./api-1813679-setbusytimeoutregistervalue.md)
  Sets the value to be written to the BUSY_TIMEOUT register.
- [setFetchAgentResetCompletion](./api-1813686-setfetchagentresetcompletion.md)
  Sets the callback to be called when a fetch agent reset completes.
- [setFetchAgentWriteCompletion](./api-1813693-setfetchagentwritecompletion.md)
  Sets the callback to be called when the fetch agent write completes.
- [setLoginCompletion](./api-1813704-setlogincompletion.md)
  Sets the callback to be called when a login attempt is complete.
- [setLoginFlags](./api-1813712-setloginflags.md)
  Sets login configuration flags.
- [setLoginRetryCountAndDelayTime](./api-1813721-setloginretrycountanddelaytime.md)
  Sets login retry behavior.
- [setLogoutCompletion](./api-1813730-setlogoutcompletion.md)
  Sets the callback to be called when a logout attempt is complete.
- [setMaxPayloadSize](./api-1813735-setmaxpayloadsize.md)
  Sets the maximum data transfer length for a normal command ORB.
- [setPassword(IOMemoryDescriptor *)](./api-1813740-setpassword.md)
  Sets the login password.
- [setPassword(void *, UInt32)](./api-1813743-setpassword.md)
  Sets the login password.
- [setReconnectTime](./api-1813747-setreconnecttime.md)
  Sets the desired reconnect duration.
- [setRefCon](./api-1813752-setrefcon.md)
  Sets the login refCon.
- [setStatusNotifyProc](./api-1813755-setstatusnotifyproc.md)
  Sets the callback to be called on normal command status.
- [setUnsolicitedStatusNotifyProc](./api-1813759-setunsolicitedstatusnotifyproc.md)
  Sets the callback to be called on normal command status.
- [submitFetchAgentReset](./api-1813764-submitfetchagentreset.md)
  Resets the LUN's fetch agent.
- [submitLogin](./api-1813766-submitlogin.md)
  Attempts to login to the LUN.
- [submitLogout](./api-1813770-submitlogout.md)
  Attempts to logout of the LUN.
- [submitORB](./api-1813772-submitorb.md)
  Submits the given orb


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2login/1813662-release)*