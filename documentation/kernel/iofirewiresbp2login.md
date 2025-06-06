# IOFireWireSBP2Login

**Framework**: Kernel  
**Kind**: cl

Supplies the login maintenance and Normal Command ORB execution portions of the API.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireSBP2Login : OSObject
```

#### Overview

Supplies APIs for login maintenance and command execution. Drivers can use this object to create IOFireWireSBP2ORB objects and execute them. Solicited and unsolicited status callback routines can be registered and the SBP2 services will notify the driver when the appropriate status arrives. This class also handles login maintenance. Supplies APIs for logging in and logging out and attempts to reconnect to the LUN after bus resets. The base FireWire services deliver bus reset notification via the IOKit message routine. The SBP2 services build on this behavior and deliver reconnectFailed and reconnectComplete through the message routine as well.

## Topics

### Miscellaneous
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
- [release](iofirewiresbp2login/1813662-release.md)
  Primary implementation of the release mechanism.
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
### Instance Methods
- [- abortLogin](iofirewiresbp2login/1572200-abortlogin.md)
- [- addORB](iofirewiresbp2login/1572184-addorb.md)
- [- allocateResources](iofirewiresbp2login/1572137-allocateresources.md)
- [- appendORB](iofirewiresbp2login/1572215-appendorb.md)
- [- appendORBImmediate](iofirewiresbp2login/1572253-appendorbimmediate.md)
- [- cancelORBTimer](iofirewiresbp2login/1572180-cancelorbtimer.md)
- [- clearAllTasksInSet](iofirewiresbp2login/1572228-clearalltasksinset.md)
- [- clearLoginGeneration](iofirewiresbp2login/1572238-clearlogingeneration.md)
- [- completeLogin](iofirewiresbp2login/1572259-completelogin.md)
- [- completeLogout](iofirewiresbp2login/1572182-completelogout.md)
- [- createORB](iofirewiresbp2login/1572197-createorb.md)
- [- doReconnect](iofirewiresbp2login/1572252-doreconnect.md)
- [- doorbellComplete](iofirewiresbp2login/1572287-doorbellcomplete.md)
- [- enableUnsolicitedStatus](iofirewiresbp2login/1572227-enableunsolicitedstatus.md)
- [- executeAddORB](iofirewiresbp2login/1572219-executeaddorb.md)
- [- executeDoorbell](iofirewiresbp2login/1572181-executedoorbell.md)
- [- executeFetchAgentReset](iofirewiresbp2login/1572235-executefetchagentreset.md)
- [- executeLogin](iofirewiresbp2login/1572248-executelogin.md)
- [- executeLogout](iofirewiresbp2login/1572169-executelogout.md)
- [- executeORB](iofirewiresbp2login/1572282-executeorb.md)
- [- executeRemoveORB](iofirewiresbp2login/1572199-executeremoveorb.md)
- [- executeSetBusyTimeout](iofirewiresbp2login/1572138-executesetbusytimeout.md)
- [- executeUnsolicitedStatusEnable](iofirewiresbp2login/1572166-executeunsolicitedstatusenable.md)
- [- fetchAgentResetComplete](iofirewiresbp2login/1572268-fetchagentresetcomplete.md)
- [- fetchAgentRetryTimer](iofirewiresbp2login/1572168-fetchagentretrytimer.md)
- [- fetchAgentWriteComplete](iofirewiresbp2login/1572254-fetchagentwritecomplete.md)
- [- fetchAgentWriteComplete](iofirewiresbp2login/3516724-fetchagentwritecomplete.md)
- [- free](iofirewiresbp2login/1572232-free.md)
- [- getARDMMax](iofirewiresbp2login/1572132-getardmmax.md)
- [- getFireWireLUN](iofirewiresbp2login/1572271-getfirewirelun.md)
- [- getFireWireUnit](iofirewiresbp2login/1572113-getfirewireunit.md)
- [- getLoginFlags](iofirewiresbp2login/1572226-getloginflags.md)
- [- getLoginID](iofirewiresbp2login/1572136-getloginid.md)
- [- getMaxCommandBlockSize](iofirewiresbp2login/1572118-getmaxcommandblocksize.md)
- [- getMaxPayloadSize](iofirewiresbp2login/1572190-getmaxpayloadsize.md)
- [- getMetaClass](iofirewiresbp2login/1572158-getmetaclass.md)
- [- getReconnectTime](iofirewiresbp2login/1572173-getreconnecttime.md)
- [- getRefCon](iofirewiresbp2login/1572129-getrefcon.md)
- [- getStatusNotifyProc](iofirewiresbp2login/1572280-getstatusnotifyproc.md)
- [- getTarget](iofirewiresbp2login/1572205-gettarget.md)
- [- getUnitInformation](iofirewiresbp2login/1572189-getunitinformation.md)
- [- getUnsolicitedStatusNotifyProc](iofirewiresbp2login/1572244-getunsolicitedstatusnotifyproc.md)
- [- initORBWithLogin](iofirewiresbp2login/1572176-initorbwithlogin.md)
- [- initWithLUN](iofirewiresbp2login/1572127-initwithlun.md)
- [- initialExecuteLogin](iofirewiresbp2login/1572154-initialexecutelogin.md)
- [- isConnected](iofirewiresbp2login/1572165-isconnected.md)
- [- isFetchAgentWriteInProgress](iofirewiresbp2login/1572109-isfetchagentwriteinprogress.md)
- [- isORBAppended](iofirewiresbp2login/1572217-isorbappended.md)
- [- isORBTimerSet](iofirewiresbp2login/1572157-isorbtimerset.md)
- [- isPhysicalAccessEnabled](iofirewiresbp2login/1572288-isphysicalaccessenabled.md)
- [- loginRetryTimeout](iofirewiresbp2login/1572171-loginretrytimeout.md)
- [- loginTimeout](iofirewiresbp2login/1572278-logintimeout.md)
- [- loginWriteComplete](iofirewiresbp2login/1572223-loginwritecomplete.md)
- [- logoutTimeout](iofirewiresbp2login/1572162-logouttimeout.md)
- [- logoutWriteComplete](iofirewiresbp2login/1572216-logoutwritecomplete.md)
- [- prepareORBForExecution](iofirewiresbp2login/1572123-prepareorbforexecution.md)
- [- processLoginWrite](iofirewiresbp2login/1572224-processloginwrite.md)
- [- reconnectRetryTimeout](iofirewiresbp2login/1572111-reconnectretrytimeout.md)
- [- reconnectStatusBlockWrite](iofirewiresbp2login/1572265-reconnectstatusblockwrite.md)
- [- reconnectTimeout](iofirewiresbp2login/1572112-reconnecttimeout.md)
- [- reconnectWriteComplete](iofirewiresbp2login/1572163-reconnectwritecomplete.md)
- [- release](iofirewiresbp2login/1572125-release.md)
- [- removeLogin](iofirewiresbp2login/1572203-removelogin.md)
- [- removeORB](iofirewiresbp2login/1572264-removeorb.md)
- [- restartReconnect](iofirewiresbp2login/1572140-restartreconnect.md)
- [- resumeNotify](iofirewiresbp2login/1572260-resumenotify.md)
- [- ringDoorbell](iofirewiresbp2login/1572192-ringdoorbell.md)
- [- sendReconnectNotification](iofirewiresbp2login/1572233-sendreconnectnotification.md)
- [- sendReconnectNotificationWithStatusBlock](iofirewiresbp2login/1572272-sendreconnectnotificationwithsta.md)
- [- sendTimeoutNotification](iofirewiresbp2login/1572239-sendtimeoutnotification.md)
- [- setAddressLoForLoginORBAndResponse](iofirewiresbp2login/1572106-setaddressloforloginorbandrespon.md)
- [- setBusyTimeoutComplete](iofirewiresbp2login/1572188-setbusytimeoutcomplete.md)
- [- setBusyTimeoutRegisterValue](iofirewiresbp2login/1572126-setbusytimeoutregistervalue.md)
- [- setFetchAgentResetCompletion](iofirewiresbp2login/1572247-setfetchagentresetcompletion.md)
- [- setFetchAgentWriteCompletion](iofirewiresbp2login/1572115-setfetchagentwritecompletion.md)
- [- setLoginCompletion](iofirewiresbp2login/1572117-setlogincompletion.md)
- [- setLoginFlags](iofirewiresbp2login/1572119-setloginflags.md)
- [- setLoginGeneration](iofirewiresbp2login/1572231-setlogingeneration.md)
- [- setLoginRetryCountAndDelayTime](iofirewiresbp2login/1572195-setloginretrycountanddelaytime.md)
- [- setLogoutCompletion](iofirewiresbp2login/1572256-setlogoutcompletion.md)
- [- setMaxPayloadSize](iofirewiresbp2login/1572145-setmaxpayloadsize.md)
- [- setNextORBAddress](iofirewiresbp2login/1572251-setnextorbaddress.md)
- [- setORBIsAppended](iofirewiresbp2login/1572107-setorbisappended.md)
- [- setPassword](iofirewiresbp2login/1572237-setpassword.md)
- [- setPassword](iofirewiresbp2login/3516725-setpassword.md)
- [- setReconnectTime](iofirewiresbp2login/1572110-setreconnecttime.md)
- [- setRefCon](iofirewiresbp2login/1572135-setrefcon.md)
- [- setStatusNotifyProc](iofirewiresbp2login/1572214-setstatusnotifyproc.md)
- [- setUnsolicitedStatusNotifyProc](iofirewiresbp2login/1572191-setunsolicitedstatusnotifyproc.md)
- [- startFetchAgentRetryTimer](iofirewiresbp2login/1572229-startfetchagentretrytimer.md)
- [- startLoginRetryTimer](iofirewiresbp2login/1572196-startloginretrytimer.md)
- [- startORBTimer](iofirewiresbp2login/1572286-startorbtimer.md)
- [- startReconnectRetryTimer](iofirewiresbp2login/1572221-startreconnectretrytimer.md)
- [- startReconnectTimer](iofirewiresbp2login/1572277-startreconnecttimer.md)
- [- statusBlockWrite](iofirewiresbp2login/1572194-statusblockwrite.md)
- [- stopFetchAgentRetryTimer](iofirewiresbp2login/1572170-stopfetchagentretrytimer.md)
- [- stopLoginRetryTimer](iofirewiresbp2login/1572146-stoploginretrytimer.md)
- [- stopReconnectRetryTimer](iofirewiresbp2login/1572267-stopreconnectretrytimer.md)
- [- submitFetchAgentReset](iofirewiresbp2login/1572193-submitfetchagentreset.md)
- [- submitLogin](iofirewiresbp2login/1572172-submitlogin.md)
- [- submitLogout](iofirewiresbp2login/1572240-submitlogout.md)
- [- submitORB](iofirewiresbp2login/1572266-submitorb.md)
- [- suspendedNotify](iofirewiresbp2login/1572222-suspendednotify.md)
- [- terminateNotify](iofirewiresbp2login/1572250-terminatenotify.md)
- [- unsolicitedStatusEnableComplete](iofirewiresbp2login/1572160-unsolicitedstatusenablecomplete.md)
### Type Methods
- [+ doorbellCompleteStatic](iofirewiresbp2login/1572177-doorbellcompletestatic.md)
- [+ fetchAgentResetCompleteStatic](iofirewiresbp2login/1572201-fetchagentresetcompletestatic.md)
- [+ fetchAgentRetryTimerStatic](iofirewiresbp2login/1572255-fetchagentretrytimerstatic.md)
- [+ fetchAgentWriteCompleteStatic](iofirewiresbp2login/1572206-fetchagentwritecompletestatic.md)
- [+ loginRetryTimeoutStatic](iofirewiresbp2login/1572208-loginretrytimeoutstatic.md)
- [+ loginTimeoutStatic](iofirewiresbp2login/1572147-logintimeoutstatic.md)
- [+ loginWriteCompleteStatic](iofirewiresbp2login/1572174-loginwritecompletestatic.md)
- [+ logoutTimeoutStatic](iofirewiresbp2login/1572249-logouttimeoutstatic.md)
- [+ logoutWriteCompleteStatic](iofirewiresbp2login/1572185-logoutwritecompletestatic.md)
- [+ reconnectRetryTimeoutStatic](iofirewiresbp2login/1572210-reconnectretrytimeoutstatic.md)
- [+ reconnectStatusBlockWriteStatic](iofirewiresbp2login/1572209-reconnectstatusblockwritestatic.md)
- [+ reconnectTimeoutStatic](iofirewiresbp2login/1572143-reconnecttimeoutstatic.md)
- [+ reconnectWriteCompleteStatic](iofirewiresbp2login/1572178-reconnectwritecompletestatic.md)
- [+ setBusyTimeoutCompleteStatic](iofirewiresbp2login/1572148-setbusytimeoutcompletestatic.md)
- [+ staticExecuteAddORB](iofirewiresbp2login/1572142-staticexecuteaddorb.md)
- [+ staticExecuteDoorbell](iofirewiresbp2login/1572236-staticexecutedoorbell.md)
- [+ staticExecuteFetchAgentReset](iofirewiresbp2login/1572186-staticexecutefetchagentreset.md)
- [+ staticExecuteLogin](iofirewiresbp2login/1572257-staticexecutelogin.md)
- [+ staticExecuteLogout](iofirewiresbp2login/1572261-staticexecutelogout.md)
- [+ staticExecuteORB](iofirewiresbp2login/1572151-staticexecuteorb.md)
- [+ staticExecuteRemoveORB](iofirewiresbp2login/1572263-staticexecuteremoveorb.md)
- [+ staticExecuteUnsolicitedStatusEnable](iofirewiresbp2login/1572262-staticexecuteunsolicitedstatusen.md)
- [+ statusBlockWriteStatic](iofirewiresbp2login/1572144-statusblockwritestatic.md)
- [+ unsolicitedStatusEnableCompleteStatic](iofirewiresbp2login/1572198-unsolicitedstatusenablecompletes.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOFireWireSBP2ManagementORB](iofirewiresbp2managementorb.md)
  Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LUN interface.
- [IOFireWireSBP2ORB](iofirewiresbp2orb.md)
  Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2Login.
- [FWSBP2FetchAgentWriteCallback](fwsbp2fetchagentwritecallback.md)
- [FWSBP2LoginCallback](fwsbp2logincallback.md)
- [FWSBP2LoginCompleteParams](fwsbp2logincompleteparams.md)
- [FWSBP2LoginCompleteParamsPtr](fwsbp2logincompleteparamsptr.md)
- [FWSBP2LoginResponse](fwsbp2loginresponse.md)
- [FWSBP2LoginResponsePtr](fwsbp2loginresponseptr.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2login)*