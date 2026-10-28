# WSGetWSTypeIDFromCFType

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the `WSTypeID` associated with a given `CFTypeRef`.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
WSTypeID WSGetWSTypeIDFromCFType(CFTypeRef ref);
```

## Return Value

the `WSTypeID` used in serializing the object.  If no `WSTypeID` matches, `eWSUnknownType` is returned.  

## Discussion

Returns the `WSTypeID` associated with `CFTypeRef`.  Because there is not a one to one mapping between `CFTypeID` and `WSTypesID` an actual instance of a CFType must be passed.

## Parameters

- `ref`: A `CFTypeRef` object. An actual instance of a CFType must be passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1508442-wsgetwstypeidfromcftype)*