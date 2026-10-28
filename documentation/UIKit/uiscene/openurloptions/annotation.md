# annotation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A property-list object that contains the annotation data provided by a document interaction controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var annotation: Any? { get }
```

```objc
@property (nonatomic, readonly, nullable) id annotation;
```

## Discussion

This property contains the data that the originating app placed in the [`annotation`](../../uidocumentinteractioncontroller/annotation.md) property of its [`UIDocumentInteractionController`](../../uidocumentinteractioncontroller.md). The root object is always an [`NSDictionary`](../../../Foundation/nsdictionary.md) object. The contents of that dictionary may be any other property list types, including [`NSDictionary`](../../../Foundation/nsdictionary.md), [`NSArray`](../../../Foundation/nsarray.md), [`NSData`](../../../Foundation/nsdata.md), [`NSString`](../../../Foundation/nsstring.md), [`NSNumber`](../../../Foundation/nsnumber.md), or [`NSDate`](../../../Foundation/nsdate.md) objects.

## See Also

### Specifying the URL details
- [var sourceApplication: String?](./sourceapplication.md)
  The bundle ID of the app that originated the request.
- [var eventAttribution: UIEventAttribution?](./eventattribution.md)
  An event attribution associated with the URL to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions/annotation)*