# PMRelease(_:)

**Framework**: Application Services  
**Kind**: func

Releases a printing object by decrementing its reference count.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMRelease(_ object: PMObject?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

Your application should use the `PMRelease` function to release any printing objects it creates or retains. When an object’s reference count reaches 0, the object is deallocated.

For example, to terminate a printing session created with the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md), pass the associated [`PMPrintSession`](pmprintsession.md) object to `PMRelease`. To release printing objects created with the functions [`PMCreatePageFormat(_:)`](1459485-pmcreatepageformat.md) and [`PMCreatePrintSettings(_:)`](1463239-pmcreateprintsettings.md), pass the associated `PMPageFormat` and `PMPrintSettings` objects to `PMRelease`.

## Parameters

- `object`: The printing object you want to release.

## See Also

- [func PMRetain(PMObject?) -> OSStatus](1460190-pmretain.md)
  Retains a printing object by incrementing its reference count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461402-pmrelease)*