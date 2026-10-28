# WSProtocolHandlerGetTypeID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns a `CFTypeID` for the current `WSProtocolHandlerRef`.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFTypeID WSProtocolHandlerGetTypeID(void);
```

## Return Value

A `CFTypeID`.

## Discussion

Returns the `CFTypeID` of the opaque `WSProtocolHandlerRef` most recently created by `WSProtocolHandlerCreate`. `CFTypeIDs` are only valid during a particular instance of a process and should not be used as static values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423455-wsprotocolhandlergettypeid)*