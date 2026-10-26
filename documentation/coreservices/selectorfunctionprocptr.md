# SelectorFunctionProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a selector callback function that returns information associated with your own selector code.  

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef OSErr (*SelectorFunctionProcPtr)(OSType selector, SInt32 *response);
```

#### Return Value

A result code. See [Gestalt Manager](./carbon_core/gestalt_manager.md).

#### Discussion

Your selector function places the requested information in the `response` parameter and returns a result code. If the information is not available, the selector function returns the appropriate error code, which the `Gestalt` function returns as its function result.

A selector function can call `Gestalt` or even other selector functions. 

## Parameters

- `selector`: The selector code that triggers the function. This should be a four-character sequence similar to those defined in [Constants](./carbon_core/gestalt_manager.md#1667886).
- `response`: On output, the information associated with the selector code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/selectorfunctionprocptr)*