# IOHIDReportCallbackFunction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef void (*IOHIDReportCallbackFunction)(void *target, IOReturn result, void *refcon, void *sender, uint32_t bufferSize);
```

## Discussion

Type and arguments of callout C function that is used when a completion routine is called, see IOHIDLib.h:setReport().

## Parameters

- `target`: void * pointer to your data, often a pointer to an object.
- `result`: Completion result of desired operation.
- `refcon`: void * pointer to more data.
- `sender`: Interface instance sending the completion routine.
- `bufferSize`: Size of the buffer received upon completion.

## See Also

### Callbacks
- [IOHIDCallbackFunction](./iohidcallbackfunction.md)
- [IOHIDElementCallbackFunction](./iohidelementcallbackfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidreportcallbackfunction)*