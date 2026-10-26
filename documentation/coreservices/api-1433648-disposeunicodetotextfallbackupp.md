# DisposeUnicodeToTextFallbackUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes of a a new universal procedure pointer (UPP)to a Unicode-to-text fallback callback.

**Availability**:
- macOS 10.0+

## Declaration

```c
void DisposeUnicodeToTextFallbackUPP(UnicodeToTextFallbackUPP userUPP);
```

#### Discussion

See the callback [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md) formore information.

## Parameters

- `userUPP`: The universal procedure pointer. 

## See Also

### Working With Universal Procedure Pointers
- [NewUnicodeToTextFallbackUPP](./api-1433556-newunicodetotextfallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a Unicode-to-textfallback callback.
- [InvokeUnicodeToTextFallbackUPP](./api-1433599-invokeunicodetotextfallbackupp.md)
  Calls your Unicode-to-text fallback callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433648-disposeunicodetotextfallbackupp)*