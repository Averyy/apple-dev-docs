# AEObjectInit()

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Initializes the Object Support Library.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEObjectInit() -> OSErr
```

```c
OSErr AEObjectInit(void);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

You must call this function before calling any of the Apple Event Manager functions that describe or manipulate Apple event objects.

You should call the `AEObjectInit` function to initialize the Apple Event Manager functions that handle object specifiers and Apple event objects. 

##### Version-Notes

To make these functions available to your application with version 1.01 and earlier versions of the Apple Event Manager, you must also link the Apple Event Object Support Library with your application when you build it. For more information, see the Version Notes section for the AppleScript Gestalt Selector described in *Inside macOS: Gestalt Manager Reference* and the function [`AERemoveSpecialHandler(_:_:_:)`](./api-1447960-aeremovespecialhandler.md).

## See Also

### Initializing the Object Support Library
- [func AESetObjectCallbacks(OSLCompareUPP!, OSLCountUPP!, OSLDisposeTokenUPP!, OSLGetMarkTokenUPP!, OSLMarkUPP!, OSLAdjustMarksUPP!, OSLGetErrDescUPP!) -> OSErr](./api-1447756-aesetobjectcallbacks.md)
  Specifies the object callback functions for your application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447372-aeobjectinit)*