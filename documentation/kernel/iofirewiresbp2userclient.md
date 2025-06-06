# IOFireWireSBP2UserClient

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireSBP2UserClient : IOUserClient
```

## Topics

### Instance Methods
- [- LSIWorkaroundSetCommandBuffersAsRanges](iofirewiresbp2userclient/1529748-lsiworkaroundsetcommandbuffersas.md)
- [- LSIWorkaroundSyncBuffersForInput](iofirewiresbp2userclient/1529651-lsiworkaroundsyncbuffersforinput.md)
- [- LSIWorkaroundSyncBuffersForOutput](iofirewiresbp2userclient/1529724-lsiworkaroundsyncbuffersforoutpu.md)
- [- checkArguments](iofirewiresbp2userclient/1529652-checkarguments.md)
- [- clientClose](iofirewiresbp2userclient/1529712-clientclose.md)
- [- clientDied](iofirewiresbp2userclient/1529756-clientdied.md)
- [- close](iofirewiresbp2userclient/1529754-close.md)
- [- createLogin](iofirewiresbp2userclient/1529744-createlogin.md)
- [- createMgmtORB](iofirewiresbp2userclient/1529742-createmgmtorb.md)
- [- createORB](iofirewiresbp2userclient/1529678-createorb.md)
- [- enableUnsolicitedStatus](iofirewiresbp2userclient/1529766-enableunsolicitedstatus.md)
- [- externalMethod](iofirewiresbp2userclient/1529649-externalmethod.md)
- [- fetchAgentResetComplete](iofirewiresbp2userclient/1529667-fetchagentresetcomplete.md)
- [- fetchAgentWriteComplete](iofirewiresbp2userclient/1529661-fetchagentwritecomplete.md)
- [- flushAllManagementORBs](iofirewiresbp2userclient/1529707-flushallmanagementorbs.md)
- [- free](iofirewiresbp2userclient/1529677-free.md)
- [- getLoginID](iofirewiresbp2userclient/1529658-getloginid.md)
- [- getMaxCommandBlockSize](iofirewiresbp2userclient/1529739-getmaxcommandblocksize.md)
- [- getMetaClass](iofirewiresbp2userclient/1529656-getmetaclass.md)
- [- getMgmtORBAsyncCallbackReference](iofirewiresbp2userclient/1529731-getmgmtorbasynccallbackreference.md)
- [- getSessionRef](iofirewiresbp2userclient/1529682-getsessionref.md)
- [- initWithTask](iofirewiresbp2userclient/1529672-initwithtask.md)
- [- loginCallback](iofirewiresbp2userclient/1529692-logincallback.md)
- [- logoutCallback](iofirewiresbp2userclient/1529681-logoutcallback.md)
- [- message](iofirewiresbp2userclient/1529680-message.md)
- [- mgmtORBCallback](iofirewiresbp2userclient/1529687-mgmtorbcallback.md)
- [- open](iofirewiresbp2userclient/1529730-open.md)
- [- openWithSessionRef](iofirewiresbp2userclient/1529654-openwithsessionref.md)
- [- releaseCommandBuffers](iofirewiresbp2userclient/1529717-releasecommandbuffers.md)
- [- releaseLogin](iofirewiresbp2userclient/1529674-releaselogin.md)
- [- releaseMgmtORB](iofirewiresbp2userclient/1529721-releasemgmtorb.md)
- [- releaseORB](iofirewiresbp2userclient/1529763-releaseorb.md)
- [- ringDoorbell](iofirewiresbp2userclient/1529719-ringdoorbell.md)
- [- setBusyTimeoutRegisterValue](iofirewiresbp2userclient/1529713-setbusytimeoutregistervalue.md)
- [- setCommandBlock](iofirewiresbp2userclient/1529660-setcommandblock.md)
- [- setCommandBuffersAsRanges](iofirewiresbp2userclient/1529700-setcommandbuffersasranges.md)
- [- setCommandFlags](iofirewiresbp2userclient/1529685-setcommandflags.md)
- [- setCommandGeneration](iofirewiresbp2userclient/1529728-setcommandgeneration.md)
- [- setCommandTimeout](iofirewiresbp2userclient/1529746-setcommandtimeout.md)
- [- setFetchAgentWriteCompletion](iofirewiresbp2userclient/1529696-setfetchagentwritecompletion.md)
- [- setLoginCallback](iofirewiresbp2userclient/1529758-setlogincallback.md)
- [- setLoginFlags](iofirewiresbp2userclient/1529710-setloginflags.md)
- [- setLogoutCallback](iofirewiresbp2userclient/1529722-setlogoutcallback.md)
- [- setMaxORBPayloadSize](iofirewiresbp2userclient/1529755-setmaxorbpayloadsize.md)
- [- setMaxPayloadSize](iofirewiresbp2userclient/1529709-setmaxpayloadsize.md)
- [- setMessageCallback](iofirewiresbp2userclient/1529740-setmessagecallback.md)
- [- setMgmtORBAsyncCallbackReference](iofirewiresbp2userclient/1529752-setmgmtorbasynccallbackreference.md)
- [- setMgmtORBCallback](iofirewiresbp2userclient/1529726-setmgmtorbcallback.md)
- [- setMgmtORBCommandFunction](iofirewiresbp2userclient/1529673-setmgmtorbcommandfunction.md)
- [- setMgmtORBManageeLogin](iofirewiresbp2userclient/1529706-setmgmtorbmanageelogin.md)
- [- setMgmtORBManageeORB](iofirewiresbp2userclient/1529702-setmgmtorbmanageeorb.md)
- [- setMgmtORBResponseBuffer](iofirewiresbp2userclient/1529735-setmgmtorbresponsebuffer.md)
- [- setORBRefCon](iofirewiresbp2userclient/1529720-setorbrefcon.md)
- [- setPassword](iofirewiresbp2userclient/1529725-setpassword.md)
- [- setReconnectTime](iofirewiresbp2userclient/1529736-setreconnecttime.md)
- [- setStatusNotify](iofirewiresbp2userclient/1529665-setstatusnotify.md)
- [- setToDummy](iofirewiresbp2userclient/1529698-settodummy.md)
- [- setUnsolicitedStatusNotify](iofirewiresbp2userclient/1529718-setunsolicitedstatusnotify.md)
- [- start](iofirewiresbp2userclient/1529732-start.md)
- [- statusNotify](iofirewiresbp2userclient/1529738-statusnotify.md)
- [- submitFetchAgentReset](iofirewiresbp2userclient/1529750-submitfetchagentreset.md)
- [- submitLogin](iofirewiresbp2userclient/1529675-submitlogin.md)
- [- submitLogout](iofirewiresbp2userclient/1529683-submitlogout.md)
- [- submitMgmtORB](iofirewiresbp2userclient/1529761-submitmgmtorb.md)
- [- submitORB](iofirewiresbp2userclient/1529655-submitorb.md)
- [- unsolicitedNotify](iofirewiresbp2userclient/1529704-unsolicitednotify.md)
### Type Methods
- [+ staticFetchAgentResetComplete](iofirewiresbp2userclient/1529671-staticfetchagentresetcomplete.md)
- [+ staticFetchAgentWriteComplete](iofirewiresbp2userclient/1529760-staticfetchagentwritecomplete.md)
- [+ staticLoginCallback](iofirewiresbp2userclient/1529690-staticlogincallback.md)
- [+ staticLogoutCallback](iofirewiresbp2userclient/1529663-staticlogoutcallback.md)
- [+ staticMgmtORBCallback](iofirewiresbp2userclient/1529676-staticmgmtorbcallback.md)
- [+ staticStatusNotify](iofirewiresbp2userclient/1529694-staticstatusnotify.md)
- [+ staticUnsolicitedNotify](iofirewiresbp2userclient/1529715-staticunsolicitednotify.md)

## Relationships

### Inherits From
- [IOUserClient](iouserclient.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2userclient)*