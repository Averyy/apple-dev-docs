# InvokeSelectorFunctionUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Invokes a selector callback function.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr InvokeSelectorFunctionUPP(OSType selector, SInt32 *response, SelectorFunctionUPP userUPP);
```

#### Return Value

A result code. See [Gestalt Manager](./carbon_core/gestalt_manager.md).

#### Discussion

You should not need to call this function, as the operating system invokes your selector callback for you.

## Parameters

- `selector`: The selector code for the function you want to invoke. You can provide any of the four-character sequences defined in [Constants](./carbon_core/gestalt_manager.md#1667886).
- `response`: On output, the value associated with the selector code.
- `userUPP`: A universal procedure pointer to the selector callback function you want to invoke. 

## See Also

### Working With Universal Procedure Pointers for Gestalt Selector Functions
- [NewSelectorFunctionUPP](./api-1472304-newselectorfunctionupp.md)
  Creates a universal procedure pointer (UPP) to a selector callback function.
- [DisposeSelectorFunctionUPP](./api-1472149-disposeselectorfunctionupp.md)
  Disposes of a universal procedure pointer to a selector callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473043-invokeselectorfunctionupp)*