# identifier

**Framework**: UIKit  
**Kind**: property

The identifier for the segue object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var identifier: String? { get }
```

#### Discussion

You assign identifiers to your segues in Interface Builder. An identifier is a string that your application uses to distinguish one segue from another. For example, if you have a source view controller that can segue to two or more different destination view controllers, you’d assign different identifiers to each segue so that the source view controller’s [`prepare(for:sender:)`](uiviewcontroller/prepare(for:sender:).md) method could tell them apart and prepare each segue appropriately.

## See Also

- [var source: UIViewController](uistoryboardsegue/source.md)
  The source view controller for the segue.
- [var destination: UIViewController](uistoryboardsegue/destination.md)
  The destination view controller for the segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/identifier)*