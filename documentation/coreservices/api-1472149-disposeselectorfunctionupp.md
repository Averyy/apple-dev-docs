# DisposeSelectorFunctionUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes of a universal procedure pointer to a selector callback function.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
void DisposeSelectorFunctionUPP(SelectorFunctionUPP userUPP);
```

## Parameters

- `userUPP`: The universal procedure pointer you want to dispose of. 

## See Also

### Working With Universal Procedure Pointers for Gestalt Selector Functions
- [NewSelectorFunctionUPP](./api-1472304-newselectorfunctionupp.md)
  Creates a universal procedure pointer (UPP) to a selector callback function.
- [InvokeSelectorFunctionUPP](./api-1473043-invokeselectorfunctionupp.md)
  Invokes a selector callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472149-disposeselectorfunctionupp)*