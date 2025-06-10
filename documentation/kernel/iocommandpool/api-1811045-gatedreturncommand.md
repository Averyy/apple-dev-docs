# gatedReturnCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn gatedReturnCommand(
 IOCommand *vCommand);
```

#### Return_value

Always returns kIOReturnSuccess if the vCommand argument is valid.

#### Overview

The gatedReturnCommand method is used to serialize the return of a command to the pool behind a command gate, runAction-ed by returnCommand.

## Parameters

- `vCommand`: A pointer to the IOCommand object to be returned to the pool.

## See Also

- [commandPool](iocommandpool/1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](iocommandpool/1811028-gatedgetcommand.md)
- [getCommand](iocommandpool/1811062-getcommand.md)
- [init](iocommandpool/1811075-init.md)
  Should never be used, obsolete. See initWithWorkLoop.
- [initWithWorkLoop](iocommandpool/1811086-initwithworkloop.md)
  Primary initializer for an IOCommandPool object.
- [returnCommand](iocommandpool/1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](iocommandpool/1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](iocommandpool/1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811045-gatedreturncommand)*