# UITraitNavigationTitleAlignment

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A trait that reports the alignment the navigation bar resolved for its title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```objc
@interface UITraitNavigationTitleAlignment : NSObject
```

#### Overview

Read this trait from a custom navigation bar title view to discover the alignment the system chose, so the view can lay out its content to match. When the system has resolved an alignment the trait reports it, Leading or Center; otherwise it is Automatic.

Use the trait to align content within the size your view already reported, not to decide that size. Overriding this trait’s value will not change the actual alignment in the navigation bar. That is controlled by `UINavigationItem.titleAlignment`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [UINSIntegerTraitDefinition](./uinsintegertraitdefinition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitnavigationtitlealignment-c.class)*