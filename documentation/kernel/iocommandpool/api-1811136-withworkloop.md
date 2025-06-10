# withWorkLoop(IOWorkLoop *)

**Framework**: Kernel  
**Kind**: instm

Primary factory method for the IOCommandPool class

## Declaration

```swift
static IOCommandPool *withWorkLoop(
 IOWorkLoop *inWorkLoop);
```

#### Return_value

Returns a pointer to an instance of IOCommandPool if successful, otherwise NULL.

#### Overview

The withWorkLoop method is what is known as a factory method. It creates a new instance of an IOCommandPool and returns a pointer to that object.

## Parameters

- `inWorkLoop`: The workloop that this command pool should synchronize with.

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
- [returnCommand](iocommandpool/1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](iocommandpool/1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811136-withworkloop)*