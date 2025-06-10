# getCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOCommand *getCommand(
 bool blockForCommand = true);
```

#### Return_value

If the caller passes true in blockForCommand, getCommand guarantees that the result will be a pointer to an IOCommand object from the pool. If the caller passes false, s/he is responsible for checking whether a non-NULL pointer was returned.

#### Overview

The getCommand method is used to get a pointer to an object of type IOCommand from the pool.

## Parameters

- `blockForCommand`: If the caller would like to have its thread slept until a command is available, it should pass true, else false.

## See Also

- [commandPool](iocommandpool/1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](iocommandpool/1811028-gatedgetcommand.md)
- [gatedReturnCommand](iocommandpool/1811045-gatedreturncommand.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811062-getcommand)*