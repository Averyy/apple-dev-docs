# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The identifier for the segue object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
var identifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identifier;
```

#### Discussion

You assign identifiers to your segues in Interface Builder. An identifier is a string that your application uses to distinguish one segue from another. For example, if you have a source view controller that can segue to two or more different destination view controllers, you’d assign different identifiers to each segue so that the source view controller’s [`prepare(for:sender:)`](../uiviewcontroller/prepare%28for,sender%29.md) method could tell them apart and prepare each segue appropriately.

## See Also

### Accessing the segue attributes
- [var source: UIViewController](./source.md)
  The source view controller for the segue.
- [var destination: UIViewController](./destination.md)
  The destination view controller for the segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue/identifier)*