# annotation

**Framework**: UIKit  
**Kind**: property

A property-list object that contains the annotation data provided by a document interaction controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var annotation: Any? { get }
```

#### Discussion

This property contains the data that the originating app placed in the [`annotation`](uidocumentinteractioncontroller/annotation.md) property of its [`UIDocumentInteractionController`](uidocumentinteractioncontroller.md). The root object is always an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object. The contents of that dictionary may be any other property list types, including [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), or [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) objects.

## See Also

- [var sourceApplication: String?](uiscene/openurloptions/sourceapplication.md)
  The bundle ID of the app that originated the request.
- [var eventAttribution: UIEventAttribution?](uiscene/openurloptions/eventattribution.md)
  An event attribution associated with the URL to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions/annotation)*