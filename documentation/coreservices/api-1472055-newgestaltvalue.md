# NewGestaltValue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Installs a new `Gestalt` selector code and a value that `Gestalt` returns for that selector.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr NewGestaltValue(OSType selector, SInt32 newValue);
```

#### Return Value

A result code. See [Gestalt Manager](./carbon_core/gestalt_manager.md).

#### Discussion

You call the function `NewGestaltValue` when the specified selector is not already installed and you don't want to override an existing value.

In macOS, the new selector and value are on a per-context basis. That means they are available only to the application or other code that installs them. You cannot use this function to make information available to another process. 

## Parameters

- `selector`: The selector code you want to add. This should be a four-character sequence similar to those defined in [Constants](./carbon_core/gestalt_manager.md#1667886).
- `newValue`: The value to return for the new selector code.

## See Also

### Getting and Setting Gestalt Selector Codes and Values
- [Gestalt](./api-1471624-gestalt.md)
  Obtains information about the operating environment.
- [SetGestaltValue](./api-1470991-setgestaltvalue.md)
  Sets the value the function `Gestalt` will return for a specified selector code, installing the selector if it was not already installed.
- [ReplaceGestaltValue](./api-1472000-replacegestaltvalue.md)
  Replaces the value that the function `Gestalt` returns for a specified selector code with the value provided to the function.
- [DeleteGestaltValue](./api-1472699-deletegestaltvalue.md)
  Deletes a `Gestalt` selector code so that it is no longer recognized by `Gestalt`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472055-newgestaltvalue)*