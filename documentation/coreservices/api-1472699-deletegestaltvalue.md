# DeleteGestaltValue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Deletes a `Gestalt` selector code so that it is no longer recognized by `Gestalt`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr DeleteGestaltValue(OSType selector);
```

#### Return Value

A result code. See [Gestalt Manager](./carbon_core/gestalt_manager.md).

#### Discussion

After calling this function, subsequent query or replacement calls for the selector code will fail as if the selector had never been installed. 

In macOS, the selector is on a per-context basis. You cannot use this function to affect another process. 

## Parameters

- `selector`: The selector code you want to delete. This should be a four-character sequence similar to those defined in [Constants](./carbon_core/gestalt_manager.md#1667886).

## See Also

### Getting and Setting Gestalt Selector Codes and Values
- [Gestalt](./api-1471624-gestalt.md)
  Obtains information about the operating environment.
- [NewGestaltValue](./api-1472055-newgestaltvalue.md)
  Installs a new `Gestalt` selector code and a value that `Gestalt` returns for that selector.
- [SetGestaltValue](./api-1470991-setgestaltvalue.md)
  Sets the value the function `Gestalt` will return for a specified selector code, installing the selector if it was not already installed.
- [ReplaceGestaltValue](./api-1472000-replacegestaltvalue.md)
  Replaces the value that the function `Gestalt` returns for a specified selector code with the value provided to the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472699-deletegestaltvalue)*