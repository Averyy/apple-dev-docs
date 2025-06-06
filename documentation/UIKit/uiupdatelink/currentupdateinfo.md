# currentUpdateInfo()

**Framework**: UIKit  
**Kind**: method

Returns an object that describes the current UI update state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func currentUpdateInfo() -> UIUpdateInfo?
```

#### Return Value

During a UI update, returns a [`UIUpdateInfo`](uiupdateinfo.md) object that describes the current UI update state. Outside a UI update, returns `nil`.

## See Also

- [class UIUpdateInfo](uiupdateinfo.md)
  An object that contains detailed information about the current UI update state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/currentupdateinfo())*