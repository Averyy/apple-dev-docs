# encodeRestorableState(with:)

**Framework**: UIKit  
**Kind**: method

Encodes state-related information for the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func encodeRestorableState(with coder: NSCoder)
```

#### Discussion

If your app supports state preservation, you can override this method for any views that have state information that should be saved between launches of your app. You should save only the data required to return the view to its current configuration. Do not save the view object itself and do not save any data that could be determined by other means at launch time.

Few views should need to save state information. Most views should just be configured using the data from their view controller. However, this method is available for those views that have user-configurable state that would be otherwise lost between app launches.

Your implementation of this method can encode other restorable view and view controller objects that it needs to reference. Encoding a restorable view or view controller writes that object’s restoration identifier to the coder. (That identifier is used during the decode process to locate the new version of the object.) If the view or view controller defines its own version of this method, that method is also called at some point so that the object can encode its own state.

Apart from views and view controllers, other objects follow the normal serialization process and must adopt the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol before they can be encoded. Encoding such objects embeds the object’s contents in the archive directly. During the decode process, a new object is created and initialized with the data from the archive.

It is recommended that you call `super` at some point during your implementation to give parent classes an opportunity to save their state information.

## Parameters

- `coder`: The coder object to use to encode the state of the view.

## See Also

- [var restorationIdentifier: String?](uiview/restorationidentifier.md)
  The identifier that determines whether the view supports state restoration.
- [func decodeRestorableState(with: NSCoder)](uiview/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/encoderestorablestate(with:))*