# gatedGetCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn gatedGetCommand(
 IOCommand **vCommand,
 boolvBlock);
```

#### Return_value

Returns kIOReturnNoResources if no command is available and the client doesn't wish to block until one does become available. kIOReturnSuccess if the vCommand argument is valid.

#### Overview

The gatedGetCommand method is used to serialize the extraction of a command from the pool behind a command gate, runAction-ed by getCommand.

## Parameters

- `vCommand`: A pointer to a pointer to an IOCommand object where the returned command will be stored.
- `vBlock`: A bool that indicates whether to block the request until a command becomes available.

## See Also

- [commandPool](iocommandpool/1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedReturnCommand](iocommandpool/1811045-gatedreturncommand.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811028-gatedgetcommand)*