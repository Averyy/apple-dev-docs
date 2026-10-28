# endUndoGroup()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Closes the current undo group.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func endUndoGroup() -> Bool
```

```objc
- (BOOL) endUndoGroup;
```

## Return Value

[`true`](../../Swift/true.md) if the undo group was successfully ended; otherwise [`false`](../../Swift/false.md).

## See Also

### Creating Undo Groups
- [func startUndoGroup(String!) -> Bool](./startundogroup%28_%29.md)
  Begins a new undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxundoapi/endundogroup())*