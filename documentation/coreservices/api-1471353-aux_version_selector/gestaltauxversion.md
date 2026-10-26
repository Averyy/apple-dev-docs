# gestaltAUXVersion

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

The version of A/UX if it is currently executing. The result is placed into the low-order word of the response parameter. If A/UX is not executing, the `Gestalt` function returns `gestaltUnknownErr`.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltAUXVersion = 'a/ux'
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471353-aux_version_selector/gestaltauxversion)*