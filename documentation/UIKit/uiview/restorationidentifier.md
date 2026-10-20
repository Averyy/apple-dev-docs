# restorationIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The identifier that determines whether the view supports state restoration.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var restorationIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * restorationIdentifier;
```

#### Discussion

This property indicates whether state information in the view should be preserved; it is also used to identify the view during the restoration process. The value of this property is `nil` by default, which indicates that the view’s state does not need to be saved. Assigning a string object to the property lets the owning view controller know that the view has relevant state information to save.

Assign a value to this property only if you are implementing a custom view that implements the [`encodeRestorableState(with:)`](./encoderestorablestate%28with%29.md) and [`decodeRestorableState(with:)`](./decoderestorablestate%28with%29.md) methods for saving and restoring state. You use those methods to write any view-specific state information and subsequently use that data to restore the view to its previous configuration.

> ❗ **Important**:  Simply setting the value of this property is not enough to ensure that the view is preserved and restored. Its owning view controller, and all of that view controller’s parent view controllers, must also have a restoration identifier. For more information about the preservation and restoration process, see [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

## See Also

### Preserving and restoring state
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Encodes state-related information for the view.
- [func decodeRestorableState(with: NSCoder)](./decoderestorablestate%28with%29.md)
  Decodes and restores state-related information for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/restorationidentifier)*