# initWithWorkLoop

**Framework**: Kernel  
**Kind**: instm

Primary initializer for an IOCommandPool object.

## Declaration

```swift
virtual bool initWithWorkLoop(
 IOWorkLoop *inWorkLoop);
```

#### Return_value

Returns true if command pool was successfully initialized.

#### Overview

Primary initializer for an IOCommandPool. Should probably use IOCommandPool::withWorkLoop() as it is easier to use.

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
- [returnCommand](iocommandpool/1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](iocommandpool/1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](iocommandpool/1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811086-initwithworkloop)*