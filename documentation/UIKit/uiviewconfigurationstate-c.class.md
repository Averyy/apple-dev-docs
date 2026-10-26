# UIViewConfigurationState

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A structure that encapsulates a view’s state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIViewConfigurationState : NSObject
```

#### Overview

A view configuration state encompasses a trait collection along with all of the common states that affect a view’s appearance — states like selected, focused, or disabled. A view configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a view configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](./uicollectionviewcell/updateconfiguration%28using%29.md) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [`configurationState`](./uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a view configuration state by defining a custom state key using [`UIConfigurationStateCustomKey`](./uiconfigurationstatecustomkey.md).

## Topics

### Managing view configuration states
- [traitCollection](./uiviewconfigurationstate-c.class/traitcollection.md)
  The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [selected](./uiviewconfigurationstate-c.class/selected.md)
  A Boolean value that indicates whether the view is in a selected state.
- [highlighted](./uiviewconfigurationstate-c.class/highlighted.md)
  A Boolean value that indicates whether the view is in a highlighted state.
- [focused](./uiviewconfigurationstate-c.class/focused.md)
  A Boolean value that indicates whether the view is in a focused state.
- [disabled](./uiviewconfigurationstate-c.class/disabled.md)
  A Boolean value that indicates whether the view is in a disabled state.
- [pinned](./uiviewconfigurationstate-c.class/pinned.md)
  A Boolean value that indicates whether the view is in a pinned state.
### Creating a configuration state manually
- [- initWithTraitCollection:](./uiviewconfigurationstate-c.class/initwithtraitcollection_.md)
  Creates a view configuration state with the specified trait collection.
- [- initWithCoder:](./uiviewconfigurationstate-c.class/initwithcoder_.md)
  Creates a view configuration state from data in an unarchiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UICellConfigurationState](./uicellconfigurationstate-c.class.md)
### Conforms To
- [UIConfigurationState](./uiconfigurationstate-1smq1.md)

## See Also

### Configuration states
- [UICellConfigurationState](./uicellconfigurationstate-c.class.md)
  An object that encapsulates a cell’s state.
- [UIConfigurationState](./uiconfigurationstate-1smq1.md)
  The requirements for an object that encapsulates a view’s state.
- [struct UIConfigurationStateCustomKey](./uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewconfigurationstate-c.class)*