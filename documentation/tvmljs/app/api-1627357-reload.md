# reload

**Framework**: TVMLKit JS  
**Kind**: instm

Reloads the app.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
void reload(
    in Object options, 
    in optional Object reloadData
);
```

#### Discussion

This function reloads the initial TVMLKit JS file without quitting the app. The optional `reloadData` parameter enables you to capture and restart the app in its current state. If the `reloadData` parameter is not present, the app is restarted in its initial state.

## Parameters

- `options`: The options used to determine when the app is reloaded. This parameter is a dictionary with a key-value pair. The key can have the value  . The value can have the values   or  .
- `reloadData`: An optional, developer-defined object that contains information about the current app state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app/1627357-reload)*