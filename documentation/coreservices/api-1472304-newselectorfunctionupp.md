# NewSelectorFunctionUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a universal procedure pointer (UPP) to a selector callback function.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
SelectorFunctionUPP NewSelectorFunctionUPP(SelectorFunctionProcPtr userRoutine);
```

#### Return Value

On return, a universal procedure pointer to the selector callback function. See the description of the `SelectorFunctionUPP` data type.

#### Discussion

You use the `NewSelectorFunctionUPP` function to create a UPP to pass to the `NewGestalt` or `ReplaceGestalt` functions. 

## Parameters

- `userRoutine`: The address of the selector callback function. 

## See Also

### Working With Universal Procedure Pointers for Gestalt Selector Functions
- [DisposeSelectorFunctionUPP](./api-1472149-disposeselectorfunctionupp.md)
  Disposes of a universal procedure pointer to a selector callback function.
- [InvokeSelectorFunctionUPP](./api-1473043-invokeselectorfunctionupp.md)
  Invokes a selector callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472304-newselectorfunctionupp)*