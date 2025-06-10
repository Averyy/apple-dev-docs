# returnCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual void returnCommand(
 IOCommand *commmand);
```

#### Overview

The returnCommand method is used to place an object of type IOCommand into the pool, whether it be the first time, or the 1000th time.

## Parameters

- `commmand`: The command to place in the pool.

## See Also

- [commandPool](iocommandpool/1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](iocommandpool/1811028-gatedgetcommand.md)
- [gatedReturnCommand](iocommandpool/1811045-gatedreturncommand.md)
- [getCommand](iocommandpool/1811062-getcommand.md)
- [init](iocommandpool/1811075-init.md)
  Should never be used, obsolete. See initWithWorkLoop.
- [initWithWorkLoop](iocommandpool/1811086-initwithworkloop.md)
  Primary initializer for an IOCommandPool object.
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](iocommandpool/1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](iocommandpool/1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811102-returncommand)*