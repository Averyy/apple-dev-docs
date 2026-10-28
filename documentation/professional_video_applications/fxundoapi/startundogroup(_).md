# startUndoGroup(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Begins a new undo group.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func startUndoGroup(_ name: String!) -> Bool
```

```objc
- (BOOL) startUndoGroup:(NSString *) name;
```

## Return Value

[`true`](../../Swift/true.md) if the undo group was successfully started; otherwise [`false`](../../Swift/false.md).

## Discussion

A plug-in can use this method to collapse multiple operations into one undo operation. Subsequent undo operations will be coalesced into this group until [`endUndoGroup()`](./endundogroup%28%29.md) is called. Each call to [`startUndoGroup(_:)`](./startundogroup%28_%29.md) must be balanced with a call to [`endUndoGroup()`](./endundogroup%28%29.md).

For example, a plug-in may implement a “preset” popup, which changes the values of 20 other parameters using the FxParameterSettingAPI. By nesting the parameter changes in a `startUndoGroup`/`endUndoGroup` block, the 20 changes will be collapsed into one undo operation. This allows the user to undo the preset app by hitting undo once, instead of once per each changed parameter.

## Parameters

- `name`: The name of the undo group. Some hosts may display this name in their undo menu. This name should be localized and suitable for user display.

## See Also

### Creating Undo Groups
- [func endUndoGroup() -> Bool](./endundogroup%28%29.md)
  Closes the current undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxundoapi/startundogroup(_:))*