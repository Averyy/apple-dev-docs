# UITextDropProposal.Performer

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The performers that are responsible for handling the drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Performer
```

```c
enum UITextDropPerformer : NSUInteger;
```

## Overview

A performer is responsible for:

- Proving a preview for the drop activity.
- Loading data from the item providers.
- Inserting the data into the text view.

## Topics

### Performers
- [UITextDropProposal.Performer.view](./performer/view.md)
  A performer type that indicates that the text view is responsible for doing the drop operation.
- [UITextDropProposal.Performer.delegate](./performer/delegate.md)
  A performer type that indicates the delegate object is responsible for doing the drop operation.
### Initializers
- [init?(rawValue: UInt)](./performer/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Drop management
- [protocol UITextDropRequest](../uitextdroprequest.md)
  The interface for specifying the attributes of a drop request for a text view.
- [class UITextDropProposal](../uitextdropproposal.md)
  A proposed configuration for the behavior of a text drop interaction.
- [UITextDropProposal.Action](./action.md)
  The text drop action styles for text views.
- [UITextDropProposal.ProgressMode](./progressmode.md)
  The text drop progress styles for user-visible progress indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/performer)*