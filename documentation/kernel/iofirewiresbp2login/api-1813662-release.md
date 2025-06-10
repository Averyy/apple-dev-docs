# release

**Framework**: Kernel  
**Kind**: instm

Primary implementation of the release mechanism.

## Declaration

```swift
virtual void release() const;
```

#### Overview

See OSObject.h for more information. When retainCount == when then call free().

## See Also

- [createORB](iofirewiresbp2login/1813411-createorb.md)
  Creates a new IOFireWireSBP2ORB for this login.
- [enableUnsolicitedStatus](iofirewiresbp2login/1813441-enableunsolicitedstatus.md)
  Enables unsolicited status.
- [getLoginFlags](iofirewiresbp2login/1813479-getloginflags.md)
  Returns the currently set login flags.
- [getLoginID](iofirewiresbp2login/1813507-getloginid.md)
  Returns the current login ID.
- [getMaxCommandBlockSize](iofirewiresbp2login/1813539-getmaxcommandblocksize.md)
  Returns the maximum command block size.
- [getMaxPayloadSize](iofirewiresbp2login/1813578-getmaxpayloadsize.md)
  Returns the currently set maximum payload size.
- [getReconnectTime](iofirewiresbp2login/1813610-getreconnecttime.md)
  Returns the currently set reconnect time.
- [getRefCon](iofirewiresbp2login/1813628-getrefcon.md)
  Returns the refCon set with setRefCon.
- [getStatusNotifyProc](iofirewiresbp2login/1813642-getstatusnotifyproc.md)
  Returns the callback to be called on normal command status.
- [getUnsolicitedStatusNotifyProc](iofirewiresbp2login/1813655-getunsolicitedstatusnotifyproc.md)
  Returns the callback to be called on unsolicited status.
- [ringDoorbell](iofirewiresbp2login/1813671-ringdoorbell.md)
  Rings the doorbell on the LUN.
- [setBusyTimeoutRegisterValue](iofirewiresbp2login/1813679-setbusytimeoutregistervalue.md)
  Sets the value to be written to the BUSY_TIMEOUT register.
- [setFetchAgentResetCompletion](iofirewiresbp2login/1813686-setfetchagentresetcompletion.md)
  Sets the callback to be called when a fetch agent reset completes.
- [setFetchAgentWriteCompletion](iofirewiresbp2login/1813693-setfetchagentwritecompletion.md)
  Sets the callback to be called when the fetch agent write completes.
- [setLoginCompletion](iofirewiresbp2login/1813704-setlogincompletion.md)
  Sets the callback to be called when a login attempt is complete.
- [setLoginFlags](iofirewiresbp2login/1813712-setloginflags.md)
  Sets login configuration flags.
- [setLoginRetryCountAndDelayTime](iofirewiresbp2login/1813721-setloginretrycountanddelaytime.md)
  Sets login retry behavior.
- [setLogoutCompletion](iofirewiresbp2login/1813730-setlogoutcompletion.md)
  Sets the callback to be called when a logout attempt is complete.
- [setMaxPayloadSize](iofirewiresbp2login/1813735-setmaxpayloadsize.md)
  Sets the maximum data transfer length for a normal command ORB.
- [setPassword(IOMemoryDescriptor *)](iofirewiresbp2login/1813740-setpassword.md)
  Sets the login password.
- [setPassword(void *, UInt32)](iofirewiresbp2login/1813743-setpassword.md)
  Sets the login password.
- [setReconnectTime](iofirewiresbp2login/1813747-setreconnecttime.md)
  Sets the desired reconnect duration.
- [setRefCon](iofirewiresbp2login/1813752-setrefcon.md)
  Sets the login refCon.
- [setStatusNotifyProc](iofirewiresbp2login/1813755-setstatusnotifyproc.md)
  Sets the callback to be called on normal command status.
- [setUnsolicitedStatusNotifyProc](iofirewiresbp2login/1813759-setunsolicitedstatusnotifyproc.md)
  Sets the callback to be called on normal command status.
- [submitFetchAgentReset](iofirewiresbp2login/1813764-submitfetchagentreset.md)
  Resets the LUN's fetch agent.
- [submitLogin](iofirewiresbp2login/1813766-submitlogin.md)
  Attempts to login to the LUN.
- [submitLogout](iofirewiresbp2login/1813770-submitlogout.md)
  Attempts to logout of the LUN.
- [submitORB](iofirewiresbp2login/1813772-submitorb.md)
  Submits the given orb


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2login/1813662-release)*