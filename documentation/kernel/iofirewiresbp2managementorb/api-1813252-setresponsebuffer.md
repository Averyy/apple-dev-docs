# setResponseBuffer(void *, UInt32)

**Framework**: Kernel  
**Kind**: instm

Sets the response buffer for the management ORB.

## Declaration

```swift
virtual IOReturn setResponseBuffer(
 void *buf,
 UInt32len );
```

#### Return_value

Returns kIOReturnSuccess on a success.

#### Overview

Sets the response buffer for the management ORB. kFWSBP2QueryLogins returns a response to its query and needs to write it somewhere. This routine allows you to specify the location.

## Parameters

- `buf`: backing store for buffer
- `len`: length of buffer.

## See Also

- [getCommandFunction()](iofirewiresbp2managementorb/1813171-getcommandfunction.md)
  Returns the current function of the management ORB.
- [getCommandFunction()](iofirewiresbp2managementorb/1813185-getcommandfunction.md)
  Returns the current managee command of the management ORB.
- [getManageeCommand](iofirewiresbp2managementorb/1813195-getmanageecommand.md)
  Returns the current managee command of the management ORB.
- [getResponseBuffer](iofirewiresbp2managementorb/1813205-getresponsebuffer.md)
  Returns the response buffer for the management ORB.
- [release](iofirewiresbp2managementorb/1813216-release.md)
  Primary implementation of the release mechanism.
- [setCommandFunction](iofirewiresbp2managementorb/1813224-setcommandfunction.md)
  Sets the function of the management ORB.
- [setManageeCommand](iofirewiresbp2managementorb/1813235-setmanageecommand.md)
  Sets the command to be managed by the management ORB.
- [setResponseBuffer(IOMemoryDescriptor *)](iofirewiresbp2managementorb/1813243-setresponsebuffer.md)
  Sets the response buffer for the management ORB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2managementorb/1813252-setresponsebuffer)*