# ReplaceGestaltValue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Replaces the value that the function `Gestalt` returns for a specified selector code with the value provided to the function.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr ReplaceGestaltValue(OSType selector, SInt32 replacementValue);
```

#### Return Value

A result code. See [Gestalt Manager](./carbon_core/gestalt_manager.md).

#### Discussion

You use the function `ReplaceGestaltValue` to replace an existing value. You should not call this function to introduce a value that doesn't already exist; instead call the function [`NewGestaltValue`](./api-1472055-newgestaltvalue.md).

In macOS, the selector and replacement value are on a per-context basis. That means they are available only to the application or other code that installs them. You cannot use this function to make information available to another process. 

## Parameters

- `selector`: The selector code you want to add. This should be a four-character sequence similar to those defined in [Constants](./carbon_core/gestalt_manager.md#1667886).
- `replacementValue`: The replacement `Gestalt` value for the selector code.

## See Also

### Getting and Setting Gestalt Selector Codes and Values
- [Gestalt](./api-1471624-gestalt.md)
  Obtains information about the operating environment.
- [NewGestaltValue](./api-1472055-newgestaltvalue.md)
  Installs a new `Gestalt` selector code and a value that `Gestalt` returns for that selector.
- [SetGestaltValue](./api-1470991-setgestaltvalue.md)
  Sets the value the function `Gestalt` will return for a specified selector code, installing the selector if it was not already installed.
- [DeleteGestaltValue](./api-1472699-deletegestaltvalue.md)
  Deletes a `Gestalt` selector code so that it is no longer recognized by `Gestalt`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472000-replacegestaltvalue)*