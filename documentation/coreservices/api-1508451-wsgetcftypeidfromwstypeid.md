# WSGetCFTypeIDFromWSTypeID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the CFType associated with a given WSType

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFTypeID WSGetCFTypeIDFromWSTypeID(WSTypeID typeID);
```

## Return Value

Returns a `CFTypeID`, or 0 if not found

## Discussion

Returns the `CFTypeID` that is associated with a given `WSTypeID`.  `CFTypeIDs` are only valid during a particular instance of a process and should not be used as static values.

## Parameters

- `typeID`: The `WSTypeID` for which you need a `CFTypeID`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1508451-wsgetcftypeidfromwstypeid)*