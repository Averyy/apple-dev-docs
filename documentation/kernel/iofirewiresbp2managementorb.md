# IOFireWireSBP2ManagementORB

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LUN interface.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFireWireSBP2ManagementORB : IOFWCommand
```

#### Overview

## Topics

### Miscellaneous
- [getCommandFunction()](./iofirewiresbp2managementorb/api-1813171-getcommandfunction.md)
  Returns the current function of the management ORB.
- [getCommandFunction()](./iofirewiresbp2managementorb/api-1813185-getcommandfunction.md)
  Returns the current managee command of the management ORB.
- [getManageeCommand](./iofirewiresbp2managementorb/api-1813195-getmanageecommand.md)
  Returns the current managee command of the management ORB.
- [getResponseBuffer](./iofirewiresbp2managementorb/api-1813205-getresponsebuffer.md)
  Returns the response buffer for the management ORB.
- [release](./iofirewiresbp2managementorb/api-1813216-release.md)
  Primary implementation of the release mechanism.
- [setCommandFunction](./iofirewiresbp2managementorb/api-1813224-setcommandfunction.md)
  Sets the function of the management ORB.
- [setManageeCommand](./iofirewiresbp2managementorb/api-1813235-setmanageecommand.md)
  Sets the command to be managed by the management ORB.
- [setResponseBuffer(IOMemoryDescriptor *)](./iofirewiresbp2managementorb/api-1813243-setresponsebuffer.md)
  Sets the response buffer for the management ORB.
- [setResponseBuffer(void *, UInt32)](./iofirewiresbp2managementorb/api-1813252-setresponsebuffer.md)
  Sets the response buffer for the management ORB.
### Instance Methods
- [- allocateResources](./iofirewiresbp2managementorb/api-1519801-allocateresources.md)
- [- clearAllTasksInSet](./iofirewiresbp2managementorb/api-1519810-clearalltasksinset.md)
- [- complete](./iofirewiresbp2managementorb/api-1519790-complete.md)
- [- execute](./iofirewiresbp2managementorb/api-1519815-execute.md)
- [- free](./iofirewiresbp2managementorb/api-1519808-free.md)
- [- getAsyncCallbackReference](./iofirewiresbp2managementorb/api-1519816-getasynccallbackreference.md)
- [- getCommandFunction](./iofirewiresbp2managementorb/api-1519818-getcommandfunction.md)
- [- getManageeCommand](./iofirewiresbp2managementorb/api-1519832-getmanageecommand.md)
- [- getMetaClass](./iofirewiresbp2managementorb/api-1519798-getmetaclass.md)
- [- getResponseBuffer](./iofirewiresbp2managementorb/api-1519820-getresponsebuffer.md)
- [- getUnitInformation](./iofirewiresbp2managementorb/api-1519785-getunitinformation.md)
- [- handleTimeout](./iofirewiresbp2managementorb/api-1519825-handletimeout.md)
- [- initWithLUN](./iofirewiresbp2managementorb/api-1519793-initwithlun.md)
- [- release](./iofirewiresbp2managementorb/api-1519830-release.md)
- [- removeManagementORB](./iofirewiresbp2managementorb/api-1519807-removemanagementorb.md)
- [- setAsyncCallbackReference](./iofirewiresbp2managementorb/api-1519791-setasynccallbackreference.md)
- [- setCommandFunction](./iofirewiresbp2managementorb/api-1519809-setcommandfunction.md)
- [- setManageeCommand](./iofirewiresbp2managementorb/api-1519800-setmanageecommand.md)
- [- setORBToDummy](./iofirewiresbp2managementorb/api-1519819-setorbtodummy.md)
- [- setResponseBuffer](./iofirewiresbp2managementorb/api-1519823-setresponsebuffer.md)
- [- setResponseBuffer](./iofirewiresbp2managementorb/api-3516726-setresponsebuffer.md)
- [- statusBlockWrite](./iofirewiresbp2managementorb/api-1519792-statusblockwrite.md)
- [- suspendedNotify](./iofirewiresbp2managementorb/api-1519828-suspendednotify.md)
- [- writeComplete](./iofirewiresbp2managementorb/api-1519811-writecomplete.md)
### Type Methods
- [+ handleTimeoutStatic](./iofirewiresbp2managementorb/api-1519797-handletimeoutstatic.md)
- [+ statusBlockWriteStatic](./iofirewiresbp2managementorb/api-1519805-statusblockwritestatic.md)
- [+ writeCompleteStatic](./iofirewiresbp2managementorb/api-1519783-writecompletestatic.md)

## Relationships

### Inherits From
- [IOFWCommand](./iofwcommand.md)

## See Also

### Serial Bus Protocol 2
- [IOFireWireSBP2Login](./iofirewiresbp2login.md)
  Supplies the login maintenance and Normal Command ORB execution portions of the API.
- [IOFireWireSBP2ORB](./iofirewiresbp2orb.md)
  Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2Login.
- [FWSBP2FetchAgentWriteCallback](./fwsbp2fetchagentwritecallback.md)
- [FWSBP2LoginCallback](./fwsbp2logincallback.md)
- [FWSBP2LoginCompleteParams](./fwsbp2logincompleteparams.md)
- [FWSBP2LoginCompleteParamsPtr](./fwsbp2logincompleteparamsptr.md)
- [FWSBP2LoginResponse](./fwsbp2loginresponse.md)
- [FWSBP2LoginResponsePtr](./fwsbp2loginresponseptr.md)
- [FWSBP2LogoutCallback](./fwsbp2logoutcallback.md)
- [FWSBP2LogoutCompleteParams](./fwsbp2logoutcompleteparams.md)
- [FWSBP2LogoutCompleteParamsPtr](./fwsbp2logoutcompleteparamsptr.md)
- [FWSBP2ManagementCallback](./fwsbp2managementcallback.md)
- [FWSBP2NotifyCallback](./fwsbp2notifycallback.md)
- [FWSBP2NotifyParams](./fwsbp2notifyparams.md)
- [FWSBP2NotifyParamsPtr](./fwsbp2notifyparamsptr.md)
- [FWSBP2ReconnectParams](./fwsbp2reconnectparams.md)
- [FWSBP2ReconnectParamsPtr](./fwsbp2reconnectparamsptr.md)
- [FWSBP2StatusBlock](./fwsbp2statusblock.md)
- [FWSBP2StatusCallback](./fwsbp2statuscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2managementorb)*