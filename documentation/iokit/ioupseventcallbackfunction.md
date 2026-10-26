# IOUPSEventCallbackFunction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
typedef void (*IOUPSEventCallbackFunction)(void *target, IOReturn result, void *refcon, void *sender, CFDictionaryRef event);
```

#### Discussion

Type and arguments of callout C function that is used when a completion routine is called. This function pointer is set via setEventCallback and is called when an event is available from the UPS.

## Parameters

- `target`: void * pointer to your data, often a pointer to an object.
- `result`: Completion result of desired operation.
- `refcon`: void * pointer to more data.
- `sender`: Interface instance sending the completion routine.
- `event`: CFDictionaryRef containing event data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupseventcallbackfunction)*