# decodeRestorableState(with:)

**Framework**: UIKit  
**Kind**: method

Decodes and restores state-related information for the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func decodeRestorableState(with coder: NSCoder)
```

#### Discussion

If your app supports state restoration, you should override this method for any views for which you also overrode the [`encodeRestorableState(with:)`](uiview/encoderestorablestate(with:).md) method. Your implementation of this method should use any saved state information to restore the view to its previous configuration. If your [`encodeRestorableState(with:)`](uiview/encoderestorablestate(with:).md) method called `super`, this method should similarly call `super` at some point in its implementation.

## Parameters

- `coder`: The coder object to use to decode the state of the view.

## See Also

- [var restorationIdentifier: String?](uiview/restorationidentifier.md)
  The identifier that determines whether the view supports state restoration.
- [func encodeRestorableState(with: NSCoder)](uiview/encoderestorablestate(with:).md)
  Encodes state-related information for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/decoderestorablestate(with:))*