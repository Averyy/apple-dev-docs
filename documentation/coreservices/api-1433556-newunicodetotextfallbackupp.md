# NewUnicodeToTextFallbackUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a new universal procedure pointer (UPP) to a Unicode-to-textfallback callback.

**Availability**:
- macOS 10.0+

## Declaration

```c
UnicodeToTextFallbackUPP NewUnicodeToTextFallbackUPP(UnicodeToTextFallbackProcPtr userRoutine);
```

## Return Value

On return, a UPP tothe Unicode-to-text fallback callback.

## Discussion

See the callback [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md) formore information.

## Parameters

- `userRoutine`: A pointer to your Unicode-to-text fallback callback.

## See Also

### Working With Universal Procedure Pointers
- [DisposeUnicodeToTextFallbackUPP](./api-1433648-disposeunicodetotextfallbackupp.md)
  Disposes of a a new universal procedure pointer (UPP)to a Unicode-to-text fallback callback.
- [InvokeUnicodeToTextFallbackUPP](./api-1433599-invokeunicodetotextfallbackupp.md)
  Calls your Unicode-to-text fallback callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433556-newunicodetotextfallbackupp)*