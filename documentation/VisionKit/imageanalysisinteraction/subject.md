# ImageAnalysisInteraction.Subject

**Framework**: VisionKit  
**Kind**: struct  
**Role**: Structure

An area of interest in an image that the framework identifies as a primary focal point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Subject
```

## Overview

A *subject* is a foreground object in an image. A single image can have multiple subjects. For example, in an image of three different coffee mugs, the framework may classify all three mugs as separate subjects. In cases where the framework can’t separate overlapping objects in a photo as individual subjects, a subject may consist of two or more objects.

VisionKit enables your app to extract, or *lift*, the image subjects individually, or together, with the background removed. For more information, see [`image`](./subject/image.md).

An [`ImageAnalysisInteraction`](../imageanalysisinteraction.md) object contains an array of subjects ([`subjects`](./subjects.md)) that activates when [`preferredInteractionTypes`](./preferredinteractiontypes.md) contains a subject-related option, such as [`automatic`](./interactiontypes/automatic.md), or [`imageSubject`](./interactiontypes/imagesubject.md).

Your app can also present a button that gives more information on an image’s subjects by enabling the [`visualLookUp`](./interactiontypes/visuallookup.md) interaction type.

## Topics

### Acquiring the subject image
- [var image: UIImage](./subject/image.md)
  An image of the subjects with the background removed.
### Locating and sizing the subject
- [var bounds: CGRect](./subject/bounds.md)
  A rectangle that identifies the extremities of a subject within an image in relation to the interaction view’s bounds.
### Serializing a subject
- [func hash(into: inout Hasher)](./subject/hash%28into%29.md)
  Serializes a subject with the given hasher.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing image subjects
- [var subjects: Set<ImageAnalysisInteraction.Subject>](./subjects.md)
  The set of all subjects the framework identifies in an image.
- [func image(for: Set<ImageAnalysisInteraction.Subject>) async throws -> UIImage](./image%28for%29.md)
  Provides an image asynchronously that contains the given subjects with the background removed.
- [func subject(at: CGPoint) async -> ImageAnalysisInteraction.Subject?](./subject%28at%29.md)
  Returns the subject at the given point within the interaction’s image, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subject)*