# applicationFinishedRestoringState()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called after all objects have had a chance to decode their state.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional func applicationFinishedRestoringState()
```

```objc
- (void) applicationFinishedRestoringState;
```

#### Discussion

Implement this method, as needed, to perform additional configuration of the restored object. This method is called toward the end of the restoration process when all objects have been decoded. You might use this method to restore state that exists between multiple objects or in cases where you have dependencies that make decoding those objects in a specific order difficult.

The order in which this method is called on decoded objects is not guaranteed.

## See Also

### Encoding and decoding the object
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Encodes state-related information for the object.
- [func decodeRestorableState(with: NSCoder)](./decoderestorablestate%28with%29.md)
  Decodes and restores state-related information for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring/applicationfinishedrestoringstate())*