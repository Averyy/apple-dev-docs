# commandPool

**Framework**: Kernel  
**Kind**: instm

Should never be used, obsolete. See IOCommandPool::withWorkLoop.

## Declaration

```swift
static IOCommandPool *commandPool(
 IOService *inOwner, 
 IOWorkLoop *inWorkLoop, 
 UInt32 inSize = kIOCommandPoolDefaultSize);
```

## See Also

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
- [withWorkLoop(IOWorkLoop *)](iocommandpool/1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811017-commandpool)*