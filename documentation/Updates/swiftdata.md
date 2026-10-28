# SwiftData updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to SwiftData.

## Overview

Browse notable changes in [SwiftData](../SwiftData/SwiftData.md).

## June 2026

- Section your query results by creating your query with a macro that takes a `sectionBy` parameter, as listed on the [Additional query macros](../SwiftData/additionalquerymacros.md) page.
- Use types that conform to [`Codable`](../Swift/codable.md) in a model, including types you don’t control directly, by using the  [`codable`](../SwiftData/schema/attribute/option/codable.md) option for [`Schema.Attribute`](../SwiftData/schema/attribute.md).
- Receive real-time updates to models that match specified fetch criteria by using the [`ResultsObserver`](../SwiftData/resultsobserver.md) type.
- Observe remote model changes with the [`HistoryObserver`](../SwiftData/historyobserver.md) type.

## June 2025

- Increase the flexibility of your models by adopting inheritance through the [`Model()`](../SwiftData/model%28%29.md) macro.
- Gain added flexibility in accessing and sorting transaction history using [`sortBy`](../SwiftData/historydescriptor/sortby.md) in the [`HistoryDescriptor`](../SwiftData/historydescriptor.md).

## June 2024

### Macros

- Improve performance of sorts and predicate-based fetches by using the [`Index(_:)`](../SwiftData/index%28_%29-74ia2.md) macro to define individual and compound indexes.
- Define a unique constraint that includes one or more model attributes using the [`Unique(_:)`](../SwiftData/unique%28_%29.md) macro, enabling SwiftData to regard tuples of attributes as unique.
- Specify `nil` as a relationship’s `inverse` to create a unidirectional relationship.

### Persistent history

- Fetch historical changes for one or more persistent models using the model context’s [`fetchHistory(_:)`](../SwiftData/modelcontext/fetchhistory%28_%29.md) method.
- Delete stale model history from a persistent store by calling the context’s [`deleteHistory(_:)`](../SwiftData/modelcontext/deletehistory%28_%29.md) method.
- Provide an alternate change tracking strategy for your custom persistent store by adopting the [`HistoryProviding`](../SwiftData/historyproviding.md) protocol.

### Custom persistent stores

- Adopt the [`DataStore`](../SwiftData/datastore.md) protocol (and related protocols) to provide custom storage for your app’s persistent models.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/swiftdata)*