# WSMethodInvocationCopyProperty

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a copy of a named property of the invocation reference.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFTypeRef WSMethodInvocationCopyProperty(WSMethodInvocationRef invocation, CFStringRef propertyName);
```

## Return Value

the `CFTypeRef` value of the property, or `NULL` if the property was not specified.

## Discussion

Returns a property from an invocation.  If the result is `NULL`, the property doesn't exist.  Being a copy call, you must release the result.

## Parameters

- `invocation`: The method invocation.
- `propertyName`: The name of the property to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576432-wsmethodinvocationcopyproperty)*