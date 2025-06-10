# matchPropertyTable

**Framework**: Kernel  
**Kind**: instm

Called by the provider during a match

## Declaration

```swift
virtual bool matchPropertyTable( 
 OSDictionary *table, 
 SInt32 *score);
```

#### Overview

Compare the properties in the supplied table to this object's properties.

## Parameters

- `table`: The property table that this device will match against

## See Also

- [free](iohidinterface/1812725-free.md)
  Free the IOHIDInterface object.
- [init](iohidinterface/1812739-init.md)
  Initialize an IOHIDInterface object.
- [start](iohidinterface/1812781-start.md)
  Start up the driver using the given provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidinterface/1812756-matchpropertytable)*