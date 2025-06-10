# SwiftData updates

**Framework**: Updates

Learn about important changes to SwiftData.

#### Overview

Browse notable changes in [`SwiftData`](https://developer.apple.com/documentation/SwiftData).

#### June 2025

- Increase the flexibility of your models by adopting inheritance through the [`Model()`](https://developer.apple.com/documentation/SwiftData/Model()) macro.
- Gain added flexibility in accessing and sorting transaction history using [`sortBy`](https://developer.apple.com/documentation/SwiftData/HistoryDescriptor/sortBy) in the [`HistoryDescriptor`](https://developer.apple.com/documentation/SwiftData/HistoryDescriptor).

#### June 2024

##### Macros

- Improve performance of sorts and predicate-based fetches by using the [`Index(_:)`](https://developer.apple.com/documentation/SwiftData/Index(_:)-74ia2) macro to define individual and compound indexes.
- Define a unique constraint that includes one or more model attributes using the [`Unique(_:)`](https://developer.apple.com/documentation/SwiftData/Unique(_:)) macro, enabling SwiftData to regard tuples of attributes as unique.
- Specify `nil` as a relationship’s `inverse` to create a unidirectional relationship.

##### Persistent History

- Fetch historical changes for one or more persistent models using the model context’s [`fetchHistory(_:)`](https://developer.apple.com/documentation/SwiftData/ModelContext/fetchHistory(_:)) method.
- Delete stale model history from a persistent store by calling the context’s [`deleteHistory(_:)`](https://developer.apple.com/documentation/SwiftData/ModelContext/deleteHistory(_:)) method.
- Provide an alternate change tracking strategy for your custom persistent store by adopting the [`HistoryProviding`](https://developer.apple.com/documentation/SwiftData/HistoryProviding) protocol.

##### Custom Persistent Stores

- Adopt the [`DataStore`](https://developer.apple.com/documentation/SwiftData/DataStore) protocol (and related protocols) to provide custom storage for your app’s persistent models.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/swiftdata)*