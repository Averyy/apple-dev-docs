# decodeRestorableState(with:)

**Framework**: UIKit  
**Kind**: method

Decodes and restores state-related information for the object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func decodeRestorableState(with coder: NSCoder)
```

## Mentions

- [About the UI restoration process](about-the-ui-restoration-process.md)

#### Discussion

If your app supports state restoration, you can implement this method on any object for which you also overrode the [`encodeRestorableState(with:)`](uistaterestoring/encoderestorablestate(with:).md) method. Your implementation of this method should read any saved state information from the archive and use it to restore the object to its previous configuration. If your [`encodeRestorableState(with:)`](uistaterestoring/encoderestorablestate(with:).md) method called `super`, this method should similarly call `super` at some point in its implementation.

## Parameters

- `coder`: The coder object to use to decode the state of the view.

## See Also

- [func encodeRestorableState(with: NSCoder)](uistaterestoring/encoderestorablestate(with:).md)
  Encodes state-related information for the object.
- [func applicationFinishedRestoringState()](uistaterestoring/applicationfinishedrestoringstate.md)
  Called after all objects have had a chance to decode their state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring/decoderestorablestate(with:))*