# currentUpdateInfo()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an object that describes the current UI update state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func currentUpdateInfo() -> UIUpdateInfo?
```

```objc
- (UIUpdateInfo *) currentUpdateInfo;
```

## Return Value

During a UI update, returns a [`UIUpdateInfo`](../uiupdateinfo.md) object that describes the current UI update state. Outside a UI update, returns `nil`.

## See Also

### Getting the current UI update information
- [class UIUpdateInfo](../uiupdateinfo.md)
  An object that contains detailed information about the current UI update state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/currentupdateinfo())*