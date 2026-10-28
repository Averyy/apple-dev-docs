# Gestalt

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains information about the operating environment.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr Gestalt(OSType selector, SInt32 *response);
```

## Return Value

A result code. See [Gestalt Manager](./carbon_core/gestalt_manager.md).

## Discussion

The Apple-defined selector codes fall into two categories: environmental selectors, which supply specific environmental information you can use to control the behavior of your application, and informational selectors, which can’t supply information you can use to determine what hardware or software features are available. You can use one of the selector codes defined by Apple or a selector code defined by a third-party product.

Selectors with the suffix `Attr` return a 32-bit response value in which the individual bits represent specific attributes. The constants listed for these response values represent bit numbers.  

### Special Considerations

When passed one of the Apple-defined selector codes, the `Gestalt` function does not move or purge memory and therefore may be called even at interrupt time. However, selector functions associated with non-Apple selector codes might move or purge memory, and third-party software can alter the Apple-defined selector functions. Therefore, it is safest always to assume that `Gestalt` could move or purge memory.

### Version-Notes

The `ROMVersion`  and `machineType` selectors are not supported in Carbon.

In general, the `Gestalt` function returns a different result when called from a Carbon application running in macOS than it returns when called from a Classic application in macOS, because these are different environments. For example, Carbon does not use a ROM, so calling `Gestalt` from a Carbon application on a beige G3 Macintosh computer and passing the `ROMVersion` selector returns a  different result than Gestalt returns for a Classic application on the same computer.

## Parameters

- `selector`: The selector code for the information you need. You can provide any of the four-character sequences defined in [Constants](./carbon_core/gestalt_manager.md#1667886).
- `response`: On input, `Gestalt` interprets this parameter as an address at which it is to place the result returned by the selector function. `Gestalt` ignores any information already at this address. 

  On return, a pointer to the requested information whose format depends on the selector code specified in the selector parameter. Note that the `Gestalt` function returns the response from all selectors in a long word, which occupies 4 bytes. When not all 4 bytes are needed, the significant information appears in the low-order byte or bytes.

## See Also

### Getting and Setting Gestalt Selector Codes and Values
- [NewGestaltValue](./api-1472055-newgestaltvalue.md)
  Installs a new `Gestalt` selector code and a value that `Gestalt` returns for that selector.
- [SetGestaltValue](./api-1470991-setgestaltvalue.md)
  Sets the value the function `Gestalt` will return for a specified selector code, installing the selector if it was not already installed.
- [ReplaceGestaltValue](./api-1472000-replacegestaltvalue.md)
  Replaces the value that the function `Gestalt` returns for a specified selector code with the value provided to the function.
- [DeleteGestaltValue](./api-1472699-deletegestaltvalue.md)
  Deletes a `Gestalt` selector code so that it is no longer recognized by `Gestalt`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471624-gestalt)*