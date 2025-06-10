# release

**Framework**: Kernel  
**Kind**: instm

Primary implementation of the release mechanism.

## Declaration

```swift
virtual void release() const;
```

#### Overview

See OSObject.h for more information.

## Parameters

- `when`: When retainCount == when then call free().

## See Also

- [getCommandFunction()](iofirewiresbp2managementorb/1813171-getcommandfunction.md)
  Returns the current function of the management ORB.
- [getCommandFunction()](iofirewiresbp2managementorb/1813185-getcommandfunction.md)
  Returns the current managee command of the management ORB.
- [getManageeCommand](iofirewiresbp2managementorb/1813195-getmanageecommand.md)
  Returns the current managee command of the management ORB.
- [getResponseBuffer](iofirewiresbp2managementorb/1813205-getresponsebuffer.md)
  Returns the response buffer for the management ORB.
- [setCommandFunction](iofirewiresbp2managementorb/1813224-setcommandfunction.md)
  Sets the function of the management ORB.
- [setManageeCommand](iofirewiresbp2managementorb/1813235-setmanageecommand.md)
  Sets the command to be managed by the management ORB.
- [setResponseBuffer(IOMemoryDescriptor *)](iofirewiresbp2managementorb/1813243-setresponsebuffer.md)
  Sets the response buffer for the management ORB.
- [setResponseBuffer(void *, UInt32)](iofirewiresbp2managementorb/1813252-setresponsebuffer.md)
  Sets the response buffer for the management ORB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2managementorb/1813216-release)*