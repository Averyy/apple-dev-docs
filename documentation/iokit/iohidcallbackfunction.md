# IOHIDCallbackFunction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
typedef void (*IOHIDCallbackFunction)(void *target, IOReturn result, void *refcon, void *sender);
```

#### Discussion

Type and arguments of callout C function that is used when a completion routine is called, see IOHIDLib.h:setRemovalCallback().

## Parameters

- `target`: void * pointer to your data, often a pointer to an object.
- `result`: Completion result of desired operation.
- `refcon`: void * pointer to more data.
- `sender`: Interface instance sending the completion routine.

## See Also

### Callbacks
- [IOHIDElementCallbackFunction](./iohidelementcallbackfunction.md)
- [IOHIDReportCallbackFunction](./iohidreportcallbackfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidcallbackfunction)*