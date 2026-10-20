# PMRelease(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Releases a printing object by decrementing its reference count.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMRelease(_ object: PMObject?) -> OSStatus
```

```c
OSStatus PMRelease(PMObject object);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

Your application should use the `PMRelease` function to release any printing objects it creates or retains. When an object’s reference count reaches 0, the object is deallocated.

For example, to terminate a printing session created with the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md), pass the associated [`PMPrintSession`](./pmprintsession.md) object to `PMRelease`. To release printing objects created with the functions [`PMCreatePageFormat(_:)`](./api-1459485-pmcreatepageformat.md) and [`PMCreatePrintSettings(_:)`](./api-1463239-pmcreateprintsettings.md), pass the associated `PMPageFormat` and `PMPrintSettings` objects to `PMRelease`.

## Parameters

- `object`: The printing object you want to release.

## See Also

### Releasing and Retaining Printing Objects
- [func PMRetain(PMObject?) -> OSStatus](./api-1460190-pmretain.md)
  Retains a printing object by incrementing its reference count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461402-pmrelease)*