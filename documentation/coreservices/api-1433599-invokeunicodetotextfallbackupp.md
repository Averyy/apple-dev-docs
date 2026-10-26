# InvokeUnicodeToTextFallbackUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Calls your Unicode-to-text fallback callback.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus InvokeUnicodeToTextFallbackUPP(UniChar *iSrcUniStr, ByteCount iSrcUniStrLen, ByteCount *oSrcConvLen, TextPtr oDestStr, ByteCount iDestStrLen, ByteCount *oDestConvLen, LogicalAddress iInfoPtr, ConstUnicodeMappingPtr iUnicodeMappingPtr, UnicodeToTextFallbackUPP userUPP);
```

#### Discussion

You should not need to use the function `InvokeUnicodeToTextFallbackUPP`,as the system calls your Unicode-to-text fallback callback for you.See the callback [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md) formore information.

## See Also

### Working With Universal Procedure Pointers
- [NewUnicodeToTextFallbackUPP](./api-1433556-newunicodetotextfallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a Unicode-to-textfallback callback.
- [DisposeUnicodeToTextFallbackUPP](./api-1433648-disposeunicodetotextfallbackupp.md)
  Disposes of a a new universal procedure pointer (UPP)to a Unicode-to-text fallback callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433599-invokeunicodetotextfallbackupp)*