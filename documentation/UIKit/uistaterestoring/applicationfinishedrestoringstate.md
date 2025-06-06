# applicationFinishedRestoringState()

**Framework**: UIKit  
**Kind**: method

Called after all objects have had a chance to decode their state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func applicationFinishedRestoringState()
```

#### Discussion

Implement this method, as needed, to perform additional configuration of the restored object. This method is called toward the end of the restoration process when all objects have been decoded. You might use this method to restore state that exists between multiple objects or in cases where you have dependencies that make decoding those objects in a specific order difficult.

The order in which this method is called on decoded objects is not guaranteed.

## See Also

- [func encodeRestorableState(with: NSCoder)](uistaterestoring/encoderestorablestate(with:).md)
  Encodes state-related information for the object.
- [func decodeRestorableState(with: NSCoder)](uistaterestoring/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring/applicationfinishedrestoringstate())*